# 📤 Arabic OCR - Text Extraction Tool

Extract text from Arabic documents with automatic red stamp/seal removal.

## ✨ Features

- 📄 Extract Arabic text from images (JPG, PNG, etc.)
- 🔴 Automatic red stamp/seal removal
- 🎯 High accuracy text recognition using EasyOCR
- 💾 UTF-8 output compatible with Word and text editors
- ⚡ GPU acceleration support (optional)
- 🔧 Flexible command-line interface

## 🚀 Quick Start

### Prerequisites

- **Python 3.11 or 3.12** (Required! Python 3.13+ is not yet supported)
- Windows, macOS, or Linux
- 2GB+ free disk space (for models and dependencies)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Ahmed2002-rak/arabic-ocr.git
cd arabic-ocr
```

2. **Verify your Python version**
```bash
python --version
```
If you have multiple Python versions, use:
```bash
# Windows
py -3.12 --version

# macOS/Linux
python3.12 --version
```

3. **Create a virtual environment** (recommended)
```bash
# Windows - if you have Python 3.12
py -3.12 -m venv venv
venv\Scripts\activate

# Windows - if Python 3.12 is your default
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3.12 -m venv venv
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

**Note:** First installation takes 5-10 minutes as it downloads large ML models (~500MB).

## 📖 Usage

### Basic Usage

Extract text from an image with automatic stamp removal:
```bash
python arabic_ocr.py document.jpg
```

This creates `document_output.txt` with the extracted Arabic text.

### Advanced Options

```bash
# Custom output file
python arabic_ocr.py document.jpg --output result.txt

# Skip stamp removal (for documents without stamps - faster!)
python arabic_ocr.py document.jpg --no-stamp-removal

# Use GPU acceleration (requires CUDA-compatible GPU)
python arabic_ocr.py document.jpg --gpu

# Combine options
python arabic_ocr.py document.jpg --output result.txt --no-stamp-removal
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `--output <path>` | Specify custom output file path |
| `--no-stamp-removal` | Skip red stamp removal (faster for clean documents) |
| `--gpu` | Enable GPU acceleration (requires CUDA) |

## 📁 Project Structure

```
arabic-ocr/
├── arabic_ocr.py       # Main OCR script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## 🔧 How It Works

1. **Image Preprocessing**
   - Scales image 2x for better recognition
   - Removes red stamps/seals (optional)
   - Converts to grayscale
   - Applies denoising
   - Enhances contrast using CLAHE

2. **Text Extraction**
   - Uses EasyOCR with Arabic language model
   - First attempts paragraph-based grouping
   - Falls back to line-by-line detection if needed

3. **Output**
   - Saves as UTF-8 with BOM for maximum compatibility
   - Works with Microsoft Word, Notepad++, and other editors

## 🎯 Tips for Best Results

- ✅ Use high-resolution images (300 DPI or higher)
- ✅ Ensure good lighting and contrast
- ✅ Keep the document flat when scanning/photographing
- ✅ Use `--no-stamp-removal` for documents without stamps (faster processing)
- ✅ For best quality, photograph documents in good daylight

## ⚠️ Troubleshooting

### Installation Issues

#### "Python version not supported" or pip installation fails
**Problem:** You're using Python 3.13+ or Python 3.10 or older.

**Solution:** Install Python 3.11 or 3.12:
1. Download from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Use `py -3.12 -m venv venv` to create environment with correct version

#### "No module named 'distutils'" error
**Problem:** Using old requirements with new Python version.

**Solution:**
```bash
# Delete and recreate virtual environment
deactivate
rmdir /s venv  # Windows
rm -rf venv    # macOS/Linux

# Create with Python 3.12
py -3.12 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### "Failed to build numpy" or compiler errors
**Problem:** Pip is trying to build packages from source.

**Solution:**
```bash
# Install with pre-built wheels only
pip install --only-binary :all: easyocr opencv-python numpy torch torchvision
```

### Runtime Issues

#### "Cannot read image" error
- ✅ Check if the image file exists and path is correct
- ✅ Supported formats: JPG, JPEG, PNG, BMP, TIFF
- ✅ Remove special characters from filename

#### Text appears garbled in terminal
**This is normal!** Windows CMD doesn't render Arabic correctly.
- ✅ Open the output `.txt` file in Microsoft Word or Notepad++
- ✅ The text file contains proper Arabic text

#### "Permission denied" when saving
- ✅ Close the output file if it's open in another program
- ✅ Run terminal as administrator (Windows)
- ✅ Check folder write permissions

#### Low accuracy / Poor text recognition
- ✅ Try `--no-stamp-removal` if your document has no stamps
- ✅ Increase image resolution before processing
- ✅ Ensure good contrast between text and background
- ✅ Make sure the document is flat (no wrinkles or curves)
- ✅ Retake the photo in better lighting

#### "Using CPU" warning
**This is normal!** The tool works fine on CPU, just slower.
- GPU acceleration requires an NVIDIA GPU with CUDA
- Most users don't need GPU - CPU works well for occasional use

## 💡 Example Workflow

```bash
# 1. Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 2. Process a document
python arabic_ocr.py my_document.jpg

# 3. Open the result
# Windows: my_document_output.txt (double-click to open in Notepad)
# Or open in Microsoft Word for best Arabic text rendering

# 4. When done, deactivate environment
deactivate
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR) - Powerful OCR engine
- [OpenCV](https://opencv.org/) - Image processing library
- [PyTorch](https://pytorch.org/) - Deep learning framework

## 📧 Support

Having issues? Please:
1. Check the troubleshooting section above
2. Open an issue on GitHub with:
   - Your Python version (`python --version`)
   - Error message (full text)
   - Operating system

## 🔗 Links

- **Repository:** https://github.com/Ahmed2002-rak/arabic-ocr
- **Issues:** https://github.com/Ahmed2002-rak/arabic-ocr/issues

---

Made with ❤️ for the Arabic-speaking community

**⭐ If this tool helped you, please star the repository!**