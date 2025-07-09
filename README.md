Absolutely, Mani — here’s a **refined and more polished version of your README**, with a tone that balances clarity and humility (since it’s a hobby project):

---

# 📘 Slide Extractor from Lecture Videos

A lightweight, Python-based tool for extracting clean slides from educational videos. It works by converting video frames into images, detecting slide transitions using OCR and image hashing, and exporting distinct slides into PDF documents.

This is a personal hobby project, and while it works well for my needs, it's still evolving — so expect occasional quirks or room for improvement. Feedback and suggestions are welcome!

---

## ✨ Features

* ⏱️ Configurable frame extraction (e.g., every N seconds)
* 🔍 OCR-based and hash-based filtering to keep only **distinct slides**
* 🌐 Multilingual support (can be edited in cofig file)
* 📄 Export selected slides as clean PDFs
* ⚙️ customizable via `config.py`
* 🗃️ Basic batch processing for multiple videos

---

## 🛠 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/lecture2video.git
   cd lecture2video
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR (if using default OCR engine):**

   * Windows: [Download here](https://github.com/tesseract-ocr/tesseract)
   * Alternative: Use `easyocr` by changing the `OCR_ENGINE` option in `config.py`

---

## ▶️ Usage

1. **Put your videos** inside the `videos/` folder (formats: `.mp4`, `.mkv`, `.avi`, etc.)

2. **Configure settings** in `config.py`. You'll find clear comments explaining each option.

3. **Run the pipeline:**

   ```bash
   python run_pipline.py
   ```

   This will:

   * Extract frames into `frames/`
   * Filter out repetitive frames and save key slides in `slides/`
   * (Optional) Export to PDF using a script or manually

4. **Get your final slides** in PDF format — either run the export manually or extend the pipeline to automate this step.

---

## ⚙️ Configuration Highlights (`config.py`)

* `FRAME_INTERVAL`: Time (in seconds) between extracted frames
* `OCR_ENGINE`: Choose `"tesseract"` or `"easyocr"`
* `TRANSLATION_MAP`: Map non-English video titles to safe folder names
* `CLEAN_TEXT_PATTERNS`: Regex patterns to clean noisy OCR output
* `CROP_MARGIN`, `HASH_SIM_THRESHOLD`, `OCR_SIM_THRESHOLD`: Finetune filtering sensitivity

---

## 📁 Project Structure

```
lecture2video/
├── videos/          # Input videos
├── frames/          # Auto-generated raw frames
├── slides/          # Filtered slides (clean and distinct)
├── pdfs/            # Final exported PDFs
├── scripts/         # Supporting scripts for processing
├── run_pipline.py   # Main entry point
├── config.py        # All the settings
├── requirements.txt
```

---

## 💡 Tips & Notes

* 📺 Use clean, high-resolution videos for best OCR performance
* 🧪 Play with `FRAME_INTERVAL`, OCR thresholds, and hash tolerance to tune results
* 🈷 If working with non-English titles, use the `TRANSLATION_MAP` to avoid folder naming issues

---

## 📌 Known Limitations

* Minor OCR inconsistencies (like confusing `O` with `0`, or `l` with `1`) may affect similarity detection — normalization is handled, but not perfect
* Frame comparison relies on both text and visual hash — tweaking thresholds might be necessary
* Some false positives/negatives may occur depending on slide layout or video compression

---

## 🧪 Status

> 🚧 This is a personal, hobby-grade project and **not production-ready**. I'm sharing it in the hope that others might find it useful or build upon it. Use at your own discretion :)