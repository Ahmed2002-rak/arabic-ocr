# 🔤 Arabic OCR - Text Extraction Tool

Extract text from Arabic documents with automatic red stamp/seal removal.

## ✨ Features

- 📄 Extract Arabic text from images (JPG, PNG, etc.)
- 🔴 Automatic red stamp/seal removal
- 🎯 High accuracy text recognition
- 💾 UTF-8 output compatible with Word and text editors
- ⚡ GPU acceleration support (optional)
- 🔧 Flexible command-line interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Windows, macOS, or Linux

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/arabic-ocr.git
cd arabic-ocr
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

Extract text from an image with automatic stamp removal:
```bash
python arabic_ocr.py document.jpg
```

This creates `document_output.txt` with the extracted text.

### Advanced Options
```bash
# Custom output file
python arabic_ocr.py document.jpg --output result.txt

# Skip stamp removal (for documents without stamps)
python arabic_ocr.py document.jpg --no-stamp-removal

# Use GPU acceleration (requires CUDA)
python arabic_ocr.py document.jpg --gpu

# Combine options
python arabic_ocr.py document.jpg --output result.txt --no-stamp-removal
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `--output <path>` | Specify custom output file path |
| `--no-stamp-removal` | Skip red stamp removal (faster for clean documents) |
| `--gpu` | Enable GPU acceleration |

## 📁 Project Structure
```
arabic-ocr/
├── arabic_ocr.py       # Main script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore file
```

## 🔧 How It Works

1. **Image Preprocessing**
   - Scales image 2x for better recognition
   - Removes red stamps/seals (optional)
   - Converts to grayscale
   - Applies denoising
   - Enhances contrast

2. **Text Extraction**
   - Uses EasyOCR with Arabic language model
   - Detects text with paragraph grouping
   - Falls back to line-by-line detection if needed

3. **Output**
   - Saves as UTF-8 with BOM
   - Compatible with Microsoft Word, Notepad++, and other editors

## 🎯 Tips for Best Results

- Use high-resolution images (300 DPI or higher)
- Ensure good lighting and contrast
- Keep the document flat when scanning/photographing
- Use `--no-stamp-removal` for documents without stamps (faster processing)

## ⚠️ Troubleshooting

### "Cannot read image" error
- Check if the image file exists and path is correct
- Supported formats: JPG, JPEG, PNG, BMP, TIFF

### Text appears garbled in terminal
- This is normal! The Windows CMD doesn't render Arabic correctly
- Open the output `.txt` file in Microsoft Word or a proper text editor

### Permission denied when saving
- Close the output file if it's open in another program
- The script will create an alternative filename automatically

### Low accuracy
- Try with `--no-stamp-removal` if your document has no stamps
- Increase image resolution before processing
- Ensure good contrast between text and background

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR) - OCR engine
- [OpenCV](https://opencv.org/) - Image processing

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

Made with ❤️ for the Arabic-speaking community