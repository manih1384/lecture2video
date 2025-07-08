from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import os
from argparse import ArgumentParser

def images_to_pdf(image_dir: Path, output_pdf_path: Path, add_numbers=True, font_path=None, font_size=20):
    image_paths = sorted(image_dir.glob("*.jpg"))
    if not image_paths:
        print(f"⚠️ No images found in {image_dir}.")
        return

    pdf_pages = []

    print(f"🖼️ Converting {len(image_paths)} images from '{image_dir}' to PDF...")
    for idx, img_path in enumerate(tqdm(image_paths, desc="Processing images")):
        image = Image.open(img_path).convert("RGB")

        if add_numbers:
            draw = ImageDraw.Draw(image)
            try:
                font = ImageFont.truetype(font_path or "arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
            text = f"Page {idx + 1}"
            draw.text((10, image.height - font_size - 10), text, fill=(0, 0, 0), font=font)

        pdf_pages.append(image)

    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_pages[0].save(output_pdf_path, save_all=True, append_images=pdf_pages[1:])
    print(f"✅ PDF saved to: {output_pdf_path}")


def main():
    # Auto-detect slides directory and create PDFs for all subfolders
    slides_dir = Path('slides')
    output_dir = Path('pdfs')
    output_dir.mkdir(exist_ok=True)
    
    if not slides_dir.exists():
        print(f"❌ Slides directory '{slides_dir}' not found.")
        return
    
    print(f"📁 Looking for slide folders in {slides_dir}...")
    slide_folders = [d for d in slides_dir.iterdir() if d.is_dir()]
    
    if not slide_folders:
        print(f"⚠️ No slide folders found in {slides_dir}.")
        return
    
    print(f"📄 Found {len(slide_folders)} slide folders. Creating PDFs...")
    
    for slide_folder in tqdm(slide_folders, desc="Processing slide folders"):
        output_pdf = output_dir / f"{slide_folder.name}.pdf"
        images_to_pdf(slide_folder, output_pdf)
    
    print(f"✅ All PDFs created in {output_dir}/")


if __name__ == "__main__":
    main()