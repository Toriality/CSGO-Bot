import pytesseract
import spelling
from PIL import ImageGrab, Image, ImageEnhance

def stringfy(mode='normal'):
    """
    Captures the last message of the in-game chat.\n
    Arguments:
        mode: can either be 'normal' or 'debug'. If 'normal', if will correct possible command misspells and return.
    Returns:
        Chat message string
    """
    # ImageGrab to capture the screen image in a loop
    # Bbox used to capture specific area 
    cap = ImageGrab.grab(bbox=(20, 892, 532, 912)).convert('L').resize([1920,62], Image.LANCZOS)
    cap.save('./photo.jpg')
    str = pytesseract.image_to_string(cap)
    str = str.replace('\n', '')


    if mode == 'normal':
        # Correct spelling mistakes
        str = spelling.correct_spell(str)
    
    print(str)
    return(str)

