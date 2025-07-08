import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
from pathlib import Path
from config import FRAME_INTERVAL, VIDEO_EXTENSIONS, VIDEO_DIR, FRAME_OUTPUT_DIR, TRANSLATION_MAP
from unidecode import unidecode
import re

def extract_frames(video_path, output_folder, interval_sec):
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print(f"❌ Failed to open: {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval_sec)
    frame_count = 0
    saved_count = 0

    output_folder.mkdir(parents=True, exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            filename = output_folder / f"frame_{saved_count:04d}.jpg"
            success = cv2.imwrite(str(filename), frame)
            if not success:
                print(f"❌ Failed to save frame to {filename}")

            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"✅ {video_path.name}: {saved_count} frames saved.")







def safe_translit(name):
    t = unidecode(name)
    t = re.sub(r'[^\w\-_. ]', '_', t)
    return t.replace(' ', '_')           # replace spaces with underscores

def get_safe_name(name):
    if name in TRANSLATION_MAP:
        return TRANSLATION_MAP[name]
    else:
        return safe_translit(name)



def main():
    video_dir = Path(VIDEO_DIR)
    out_dir = Path(FRAME_OUTPUT_DIR)
    out_dir.mkdir(exist_ok=True)
    
    for video_path in video_dir.iterdir():
        if video_path.suffix.lower() in VIDEO_EXTENSIONS:
            raw_name = video_path.stem
            video_name = get_safe_name(raw_name)
            video_out = out_dir / video_name
            extract_frames(video_path, video_out, FRAME_INTERVAL)


if __name__ == "__main__":
    main()
