import cv2
import pytesseract
from pathlib import Path
from difflib import SequenceMatcher
from PIL import Image
import numpy as np
import imagehash
from tqdm import tqdm
import easyocr
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Levenshtein import distance as levenshtein_distance
import re
from config import (
    FRAME_OUTPUT_DIR as INPUT_DIR,
    SLIDE_OUTPUT_DIR as OUTPUT_DIR,
    OCR_SIM_THRESHOLD,
    HASH_SIM_THRESHOLD,
    CLEAN_TEXT_PATTERNS,
    TOP_IGNORE,
    BOTTOM_IGNORE,
    RIGHT_IGNORE,
    LEFT_IGNORE,
    BLACK_THRESH,
    BLACK_RATIO,
    OCR_ENGINE,
    EASY_OCR_LANG,
    TESSERACT_LANG,
    LEV_DIST,
    LEN_THRES
)

reader = easyocr.Reader(EASY_OCR_LANG) if OCR_ENGINE == "easyocr" else None


def clean_text(text):
    for phrase in CLEAN_TEXT_PATTERNS:
        text = text.replace(phrase, "")
    return text.strip()


def ocr_text(img_path):
    image = cv2.imread(str(img_path))
    height, width = image.shape[:2]

    # Crop for OCR
    top = TOP_IGNORE
    bottom = height - BOTTOM_IGNORE if height - BOTTOM_IGNORE > TOP_IGNORE else height
    left = LEFT_IGNORE
    right = width - RIGHT_IGNORE if RIGHT_IGNORE < width else width
    cropped = image[top:bottom, left:right]
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

    text = None

    # Try preferred OCR engine
    if OCR_ENGINE == "easyocr":
        try:
            result = reader.readtext(gray, detail=0)
            text = " ".join(result)
        except Exception as e:
            print(f"⚠️ EasyOCR failed: {e}")
            try:
                text = pytesseract.image_to_string(gray, lang=TESSERACT_LANG)
            except Exception as e2:
                print(f"⚠️ Tesseract also failed: {e2}")
                text = ""  # Empty OCR result, fallback handled elsewhere
    else:  # OCR_ENGINE == "tesseract"
        try:
            text = pytesseract.image_to_string(gray, lang=TESSERACT_LANG)
        except Exception as e:
            print(f"⚠️ Tesseract failed: {e}")
            try:
                result = reader.readtext(gray, detail=0)
                text = " ".join(result)
            except Exception as e2:
                print(f"⚠️ EasyOCR also failed: {e2}")
                text = ""

    return text or ""


def similar_text_ratio(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()


def image_hash(path):
    with Image.open(path) as img:
        return imagehash.phash(img)



def normalize(text: str) -> str:
    replacements = {
        'o': '0', 'q': '0',
        'l': '1', 'i': '1', ']': '1', '|': '1',
        's': '5',
        'z': '2',
        'b': '8',
    }

    # Normalize digits and case
    text = text.lower()
    text = text.replace("۰", "0").replace("۱", "1").replace("۲", "2") \
               .replace("۳", "3").replace("۴", "4").replace("۵", "5") \
               .replace("۶", "6").replace("۷", "7").replace("۸", "8") \
               .replace("۹", "9")

    for k, v in replacements.items():
        text = text.replace(k, v)

    # Remove spaces and basic punctuation
    text = re.sub(r'[\s\-\.\_]', '', text)
    
    return text.strip()




def similar_text_ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

def is_similar(prev_text, curr_text, prev_hash, curr_hash):
    if curr_text.strip() and prev_text.strip():
        norm_prev = normalize(prev_text)
        norm_curr = normalize(curr_text)
        log_file_path = os.path.join(OUTPUT_DIR, "similarity_log.txt")

        ratio = similar_text_ratio(norm_prev, norm_curr)
        lev_dist = levenshtein_distance(norm_prev, norm_curr)
        len_diff = abs(len(norm_prev) - len(norm_curr))
        sim= (
            ratio >= OCR_SIM_THRESHOLD or
            lev_dist <= LEV_DIST or
            (len_diff <= LEN_THRES and ratio >= 0.75)
        )
        if 0.75 < ratio < 0.92:
            with open(log_file_path, "a", encoding="utf-8") as f:
                f.write("🧐 Suspicious similarity range:\n")
                f.write(curr_text + "\n")
                f.write("#######################################\n")
                f.write(prev_text + "\n")
                f.write("#######################################\n")
                f.write(f"🔍 Ratio: {ratio:.4f}, Levenshtein: {lev_dist}, Length Diff: {len_diff}, sim? {sim}")

        return sim
    else:
        print("🔁 Fallback to hash comparison")
        return prev_hash - curr_hash <= HASH_SIM_THRESHOLD


def filter_slides():
    for subdir in INPUT_DIR.iterdir():
        if not subdir.is_dir():
            continue

        output_subdir = OUTPUT_DIR / subdir.name
        output_subdir.mkdir(parents=True, exist_ok=True)

        sorted_images = sorted(subdir.glob("*.jpg"))
        prev_text = None
        prev_hash = None
        kept_count = 0

        for img_path in tqdm(sorted_images, desc=f"📂 Processing {subdir.name}"):
            curr_text = clean_text(ocr_text(img_path))
            curr_hash = image_hash(img_path)

            if prev_text is None or not is_similar(prev_text, curr_text, prev_hash, curr_hash):
                new_path = output_subdir / f"slide_{kept_count:03d}.jpg"
                img = cv2.imread(str(img_path))
                img = auto_crop_black_borders(img)
                cv2.imwrite(str(new_path), img)

                kept_count += 1

                prev_text = curr_text
                prev_hash = curr_hash
        print(f"✅ Kept {kept_count} slides")



def auto_crop_black_borders(image, black_threshold=BLACK_THRESH, ratio_threshold=BLACK_RATIO):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    top, bottom, left, right = 0, height, 0, width

    for y in range(height):
        row = gray[y, :]
        if np.sum(row < black_threshold) / width < ratio_threshold:
            break
        top = y + 1

    for y in range(height - 1, -1, -1):
        row = gray[y, :]
        if np.sum(row < black_threshold) / width < ratio_threshold:
            break
        bottom = y

    for x in range(width):
        col = gray[:, x]
        if np.sum(col < black_threshold) / height < ratio_threshold:
            break
        left = x + 1

    for x in range(width - 1, -1, -1):
        col = gray[:, x]
        if np.sum(col < black_threshold) / height < ratio_threshold:
            break
        right = x

    if right <= left or bottom <= top:
        return image

    return image[top:bottom, left:right]


if __name__ == "__main__":
    filter_slides()
