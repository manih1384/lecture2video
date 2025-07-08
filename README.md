# Slide Extractor from Lecture Videos

This project extracts slides from educational videos by converting videos to frames, filtering unique slides, and exporting them as PDFs. It is designed for lecture or presentation videos, supporting slides in multiple languages (e.g., Farsi, English).

## Features
- Extracts frames from videos at configurable intervals
- Filters frames to keep only unique slides (using OCR and image hashing)
- Supports multilingual slide text (e.g., Farsi, English)
- Exports slides as PDFs with optional page numbers
- Easy configuration and batch processing

## Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Statiscal_Inference
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Install Tesseract (if using default OCR):**
   - Windows: Download from [here](https://github.com/tesseract-ocr/tesseract)
   - Or use `easyocr` by changing `OCR_ENGINE` in `config.py`

## Usage
1. **Place your videos** in the `videos/` folder. Supported formats: `.mp4`, `.mkv`, `.avi` (configurable).
2. **Configure settings** in `config.py` as needed (see comments in the file).
3. **Run the pipeline:**
   ```bash
   python run_pipline.py
   ```
   This will:
   - Extract frames to `frames/`
   - Filter slides to `slides/`
   - (You may need to run the PDF export manually for each folder, or modify the pipeline to do so.)

4. **Find your PDFs** in the output folder you specify (or add a step to export all slides to PDFs).

## Configuration
All settings are in `config.py` with detailed comments. Key options:
- `FRAME_INTERVAL`: Seconds between frames
- `OCR_ENGINE`: "tesseract" or "easyocr"
- `TRANSLATION_MAP`: Map non-English video names to safe folder names
- `CLEAN_TEXT_PATTERNS`: Remove these from OCR before comparing slides
- Border and threshold settings for OCR and cropping

## Project Structure
```
Statiscal_Inference/
├── videos/      # Input videos
├── frames/      # Extracted frames (auto-generated)
├── slides/      # Filtered slides (auto-generated)
├── pdfs/        #Final PDFs go here
├── scripts/     # Processing scripts
├── run_pipline.py  # Main pipeline runner
├── config.py    # Configuration file
├── requirements.txt
```

## Tips
- For best results, use high-quality videos with clear slides.
- Adjust `FRAME_INTERVAL` and thresholds in `config.py` for your content.
- If you have non-English video names, add them to `TRANSLATION_MAP`.

## License
MIT License (add a LICENSE file if you want to specify this)

## Acknowledgements
- OpenCV, Tesseract, EasyOCR, Pillow, imagehash, tqdm 