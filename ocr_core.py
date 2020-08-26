from PIL import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename)) # Open image with PIL

    return text

# print(ocr_core('images/ocr_example.png'))