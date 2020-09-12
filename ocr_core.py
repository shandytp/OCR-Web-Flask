from PIL import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    text = pytesseract.image_to_string(Image.open(filename))

    if 'PET' in text:
        result = 'PET'
        return result
    
    elif 'PE-HD' in text:
        result = 'PE-HD'
        return result
    
    elif 'PVC' in text:
        result = 'PVC'
        return result
    
    elif 'PE-LD' or 'LDPE' in text:
        result = 'PE-LD'
        return result

    elif 'PP' in text:
        result = 'PP'
        return result

    elif 'PS' in text:
        result = 'PS'
        return result
    elif 'Other' or 'O' in text:
        result = 'Other'
        return result

    else:
        result = """No Plastic"""
        return result
