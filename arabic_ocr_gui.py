"""
Arabic OCR GUI
Uses the SAME ArabicOCR engine from arabic_ocr.py
Adds a Tkinter interface for non-Python users
"""

import os
from pathlib import Path
from tkinter import Tk, filedialog, messagebox

# Import your existing OCR engine
from arabic_ocr import ArabicOCR


def run_gui():
    # Hide main window
    root = Tk()
    root.withdraw()

    messagebox.showinfo(
        "Arabic OCR",
        "Select an image file to extract Arabic text"
    )

    image_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )

    if not image_path:
        messagebox.showwarning("Arabic OCR", "No image selected")
        return

    try:
        # Initialize OCR (CPU by default for EXE safety)
        ocr = ArabicOCR(use_gpu=False)

        # Extract text (stamp removal ON by default)
        text = ocr.extract_text(image_path, remove_stamp=True)

        if not text.strip():
            messagebox.showwarning("Arabic OCR", "No text detected in the image")
            return

        # Output file next to image
        output_path = Path(image_path).with_suffix("").name + "_output.txt"
        output_path = os.path.join(
            os.path.dirname(image_path),
            output_path
        )

        ocr.save_text(text, output_path)

        messagebox.showinfo(
            "Arabic OCR - Done",
            f"Text extracted successfully!\n\nSaved to:\n{output_path}"
        )

    except Exception as e:
        messagebox.showerror("Arabic OCR - Error", str(e))


if __name__ == "__main__":
    run_gui()
