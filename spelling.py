import re
from spellchecker import SpellChecker
from commands import COMMANDS_LIST

def correct_spell(str, use_spellchecker=False):
    """
    This function corrects possible misspellings of words and commands.\n
    Arguments:
        str: string to be examined and have its words corrected
        use_spellchecker: bool. If True, it will look for misspelled words, if False, the function will only try to correct misspelled command calls.
    Returns:
        A string with fixed words or fixed command.
    """
    if use_spellchecker:
        portuguese = SpellChecker(language='pt')
        portuguese.word_frequency.load_words(COMMANDS_LIST)
        str_list = str.split()
        new_str = []

        for word in str_list:
            # If correction fails, use original word
            if portuguese.correction(word) == None:
                new_str.append(word)
                continue
            # Else, use correct spelled word
            new_str.append(portuguese.correction(word))

        str = ' '.join(new_str)
        return str
        
    drop = ['DRDP', 'DRUP']
    kill = ['K|LL', 'KlLL']
    click = ["CL|CK", "CLlCK", "BL|CK", "CL|l3K", "CL1CK", "CL||3K"]
    knife = ["KN|fE", "KNlFE", "l_(N|FE", "KN|FE", "kmFE"]
    invert = ["IINVERT", "|NVERT", "smvem", "smvsm", "umvem", "amvem"]
    text = ["ITEXT"]

    str = re.sub('[^A-Za-z0-9 :áéóúêâãç!]+', '', str)

    for word in drop:
        str = str.replace(word, 'DROP')
    for word in kill:
        str = str.replace(word, 'KILL')
    for word in click:
        str = str.replace(word, 'CLICK')
    for word in knife:
        str = str.replace(word, 'KNIFE')
    for word in invert:
        str = str.replace(word, 'INVERT')
    for word in text:
        str = str.replace(word, "TEXT")
    return str

def remove_non_ascii(str):
    """
    Use this function if you want to get YouTube titles. Sometimes they contain special characters that may cause a bug or a crash. With this function, non-ascii characters are removed from the given string.\n
    Arguments:
        str: string to be modified
    Returns:
        A new string without non-ascii characters.
    """
    return str.encode('ascii', errors='ignore').decode()