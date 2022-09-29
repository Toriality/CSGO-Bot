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
        
    drop = ['DRDP', 'DRUP', 'DRlJP', 'DREIP', 'ldrop', 'sump' ]
    kill = ['KlLL', 'kil', 'kii', 'lkill' ]
    click = ["CLlCK", "BLICK", "CLl3K", "CL1CK", "CL3K", 'lcllcit', 'lclick']
    knife = ["KNlFE", "lkNFE", "KNFE", "kmFE", 'lknife', 'lknlfa', 'knifa', 'lknlfa']
    invert = ["IINVERT", "NVERT", "smvem", "smvsm", "umvem", "amvem", 'invart','in9ert', 'zlinvert', ]
    text = ["ITEXT", 'taxt']
    help = ['hep', 'hap', 'halp','shalp']
    discord = ['ciscord', 'discorc', 'dlcord', 'dicord', 'DSCURQ', 'DSCDRD', 'DSCORD', 'DLSCURD', 'DLSCORD', 'DSL3DRD', 'DSBlJRD', 'DISBEIRD', 'DSCJRD']
    play = ['pay']
    tts = ['tfs','fts','tft']
    cancel = ['cance', 'canca', 'cancal', 'cafeaiet']
    meme = ['mame','mema']
    fake = ['faka']
    time = ['tima', 'tim4', 'TME', 'TlME']
    duck = ['DUC', 'IJLIcK']
    stop = ['stup', 'STlJP', 'STDP', 'STElP']
    joke = ['J0KE', 'lJKE', 'JUKE', 'JJKE', 'JlJKE', 'JlJE', 'JDKE', 'joka', 'joko']
    bye = ['bya']
    radio = ['radlo', 'rauio', 'radin', 'rndlo', 'RADD', 'RAD0', 'RADU', 'RADlJ', 'RAlJU', 'RADllJ', 'RADlU', 'RADIU', 'RADEI', 'RAD0', 'RADE', 'RADI0']
    weather = ['waather', 'weathar', 'waathar', 'WEATER', 'WEATHE']
    jump = ['jLImp', 'jum']
    score = ['scopa', 'SCUPE', 'scnpe', 'SCDPE', 'SClJPE', 'Sl3lJPE']
    reload = ['relnad', 'raload', 'raoad', 'raluad', 'rauad', 'RELlJAD', 'RELOAIJ', 'RELUAD', 'RELEIAD', 'RELUAD', 'REILEAO']
    trivia = ['trlvla', 'TRVA', 'TRVlA']
    allah = ['alah', 'ALLAI']
    paste = ['pate', 'pasta', 'paata', 'piaste']


    str = re.sub('[^A-Za-z0-9 :áéóúêâãç!]+', '', str)

    for word in drop: str = str.replace(word, 'DROP')
    for word in kill: str = str.replace(word, 'KILL')
    for word in click: str = str.replace(word, 'CLICK')
    for word in knife: str = str.replace(word, 'KNIFE')
    for word in invert: str = str.replace(word, 'INVERT')
    for word in text: str = str.replace(word, "TEXT")
    for word in help: str = str.replace(word, 'HELP')
    for word in discord: str = str.replace(word, 'DISCORD')
    for word in play: str = str.replace(word, 'PLAY')
    for word in tts: str = str.replace(word, 'TTS')
    for word in cancel: str = str.replace(word, 'CANCEL')
    for word in meme: str = str.replace(word, 'MEME')
    for word in fake: str = str.replace(word, 'FAKE')
    for word in time: str = str.replace(word, 'TIME')
    for word in duck: str = str.replace(word, 'DUCK')
    for word in stop: str = str.replace(word, 'STOP')
    for word in joke: str = str.replace(word, 'JOKE')
    for word in bye: str = str.replace(word,'BYE')

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