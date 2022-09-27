import pytesseract
import spelling
from PIL import ImageGrab

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
    cap = ImageGrab.grab(bbox=(20, 890, 400, 920)).convert('L').resize([2200,200])
    str = pytesseract.image_to_string(cap)
    str = str.replace('\n', '')

    if mode == 'normal':
        # Correct spelling mistakes
        str = spelling.correct_spell(str)
    
    print(str)
    return(str)

