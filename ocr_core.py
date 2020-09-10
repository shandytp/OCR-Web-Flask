from PIL import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # pytesseract.pytesseract.tesseract_cmd = r'D:/Tesseract-OCR/tesseract.exe'

    text = pytesseract.image_to_string(Image.open(filename))

    if text == 'PET' or text == '1':
        print('PET adalah bla bla bla') 

    elif text == 'PE-HD' or text == 'PE HD' or text == '2':
        print('PE-HD adalah bla bla bla')

    elif text == 'PVC' or text == '3':
        print('PVC adalah ')
    
    elif text == 'PE-LD' or text == 'PE LD' or text == '4':
        print('PE-LD adalah')

    elif text == 'PP' or text == '5':
        print('PP adalah ')
    
    elif text == 'PS' or text == '6':
        print('PS adalah ...')

    elif text == 'Other' or text == 'o' or text == 'O' or text == '7':
        print('Other adalah ...')
        
    return text

# print(ocr_core('images/ocr_example.png'))

