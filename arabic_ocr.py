"""
Arabic OCR - Extract text from Arabic documents
Supports documents with or without red stamps/seals
"""

import easyocr
import cv2
import numpy as np
import os
import sys
from pathlib import Path


class ArabicOCR:
    def __init__(self, use_gpu=False):
        """Initialize EasyOCR reader"""
        print("Loading EasyOCR model...")
        print("=" * 60)
        self.reader = easyocr.Reader(['ar'], gpu=use_gpu)
        print("✓ Model loaded successfully\n")
    
    def remove_red_stamp(self, img):
        """Remove red stamps/seals from image"""
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Define red color ranges
        lower_red1 = np.array([0, 40, 40])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 40, 40])
        upper_red2 = np.array([180, 255, 255])
        
        # Create masks for red regions
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        red_mask = mask1 | mask2
        
        # Dilate mask to cover stamp completely
        kernel = np.ones((5, 5), np.uint8)
        red_mask = cv2.dilate(red_mask, kernel, iterations=3)
        
        # Replace red regions with white
        img_no_stamp = img.copy()
        img_no_stamp[red_mask > 0] = (255, 255, 255)
        
        return img_no_stamp
    
    def preprocess_image(self, img, remove_stamp=True):
        """Preprocess image for better OCR accuracy"""
        # Scale up for better recognition
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        
        # Remove red stamp if requested
        if remove_stamp:
            img = self.remove_red_stamp(img)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Denoise
        gray = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
        
        # Enhance contrast
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        
        return enhanced
    
    def extract_text(self, image_path, remove_stamp=True):
        """Extract text from image"""
        # Read image
        img = cv2.imread(str(image_path))
        if img is None:
            raise ValueError(f"Cannot read image: {image_path}")
        
        print(f"Processing image: {image_path}")
        
        # Preprocess
        processed = self.preprocess_image(img, remove_stamp)
        
        # Save temporary processed image
        temp_file = "temp_processed.jpg"
        cv2.imwrite(temp_file, processed)
        
        print("Extracting text...")
        
        # Perform OCR with paragraph mode
        result = self.reader.readtext(
            temp_file,
            detail=0,
            paragraph=True,
            contrast_ths=0.1,
            adjust_contrast=0.5,
            width_ths=0.7
        )
        
        text = '\n\n'.join(result)
        
        # If no text detected, try without paragraph mode
        if not text.strip():
            print("Retrying without paragraph grouping...")
            result = self.reader.readtext(temp_file, detail=0)
            text = '\n'.join(result)
        
        # Cleanup
        if os.path.exists(temp_file):
            os.remove(temp_file)
        
        return text
    
    def save_text(self, text, output_path):
        """Save extracted text to file"""
        with open(output_path, 'w', encoding='utf-8-sig') as f:
            f.write(text)
        print(f"✓ Text saved to: {output_path}")


def main():
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python arabic_ocr.py <image_path> [options]")
        print("\nOptions:")
        print("  --no-stamp-removal    Skip red stamp removal")
        print("  --output <path>       Custom output file path")
        print("  --gpu                 Use GPU acceleration")
        print("\nExample:")
        print("  python arabic_ocr.py document.jpg")
        print("  python arabic_ocr.py document.jpg --output result.txt")
        sys.exit(1)
    
    image_path = sys.argv[1]
    remove_stamp = '--no-stamp-removal' not in sys.argv
    use_gpu = '--gpu' in sys.argv
    
    # Get output path
    if '--output' in sys.argv:
        output_idx = sys.argv.index('--output') + 1
        output_path = sys.argv[output_idx] if output_idx < len(sys.argv) else 'output.txt'
    else:
        # Create output filename based on input
        input_name = Path(image_path).stem
        output_path = f"{input_name}_output.txt"
    
    # Check if image exists
    if not os.path.exists(image_path):
        print(f"Error: Image not found: {image_path}")
        sys.exit(1)
    
    # Initialize OCR
    ocr = ArabicOCR(use_gpu=use_gpu)
    
    # Extract text
    try:
        text = ocr.extract_text(image_path, remove_stamp=remove_stamp)
        
        if not text.strip():
            print("⚠ Warning: No text detected in image")
            sys.exit(1)
        
        # Save text
        ocr.save_text(text, output_path)
        
        print("\n" + "=" * 60)
        print("Processing completed successfully!")
        print(f"Input:  {image_path}")
        print(f"Output: {output_path}")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()