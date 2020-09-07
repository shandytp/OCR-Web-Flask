from PIL import Image
import pytesseract
import cv2
import numpy as np

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # pytesseract.pytesseract.tesseract_cmd = r'D:/Tesseract-OCR/tesseract.exe'
    # nparray = np.array(filename)
    # img = Image.fromarray(nparray)

    # Read image with CV2
    img = cv2.imread(filename)

    # Resize image to 150x150
    resize = cv2.resize(img, (150, 150))

    # Convert image to grayscale
    grayscale = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    # Give image blur to noise image
    blur = cv2.medianBlur(grayscale, (5,5))

    # Remove noise with Otsu
    adaptive_thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Process OCR
    text = pytesseract.image_to_string(adaptive_thresh)

    return text



