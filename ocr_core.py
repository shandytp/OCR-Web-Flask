from PIL import Image
import pytesseract
import cv2

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = r'D:/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename)) # Open image with PIL

    return text

def resizeImg(filename):
    """
    This function will handle resize image
    """
    return cv2.resize(filename, (150, 150))

def grayscaleImg(filename):
    """
    This function will process image to grayscale
    """
    return cv2.cvtColor(filename, cv2.COLOR_BGR2GRAY)

def adaptive_thresholding(filename):
    """
    This function will handle noises in the image and convert it to thresholding
    """
    blur = cv2.medianBlur(filename, (5, 5))
    return cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
