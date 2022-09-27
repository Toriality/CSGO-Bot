import console
import spelling
import yt_dlp
import random
import os
import re
import keyboard as kb
from datetime import datetime
from pydub import AudioSegment
from pygame import mixer, time as pytime, USEREVENT
from gtts import gTTS
from youtubesearchpython import VideosSearch
from pynput.keyboard import Controller

keyboard = Controller()

TTS_PATH = './csgobot/sound/tts.mp3'
MUSIC_TEMP_PATH = '../csgobot/sound/tmp.mp3'
MUSIC_OUTPUT_PATH = '../csgobot/sound/out.mp3'
MEME_PATH = './csgobot/sound/meme/'
FAKE_PATH = './csgobot/sound/fake/'
LANGS = ['pt','en','fr','zh-CN','zh-TW','es','af','ar','bg','hr','el','it','ko','sv','vi']

async def check_audio_playing(is_cancelling=False):
    if mixer.get_init():
        if not is_cancelling:
            await console.write("say ERRO: Canal de audio ocupado. Use !CANCEL")
        return True
    return False


async def text(fullstr):
    """
    Converts text to speech, randomly choosing Google's TTS voices/languages.\n
    """
    if await check_audio_playing(): return

    # Split user's name and their message
    #str_tts = fullstr.re().split("!TEXT")[1]
    str_tts = re.split('!text', fullstr,flags=re.I)[1]

    # This try-except avoids "no text inserted" error if someone types !TEXT with no text after the command call
    try:
        str_tts = spelling.correct_spell(str_tts, True)
        tts = gTTS(text=str_tts, lang=random.choice(LANGS))
        tts.save(TTS_PATH)
    except:
        return
    
    # Call event when music ends
    MUSIC_END = USEREVENT+1
    mixer.music.set_endevent(MUSIC_END)

    # Mixer config
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(TTS_PATH)

    # Force voicerecord button while TTS is playing
    keyboard.press('z')
    kb.block_key('z')
    mixer.music.play()
    while mixer.music.get_busy():
        pytime.wait(100)
        continue
    kb.unblock_key('z')
    keyboard.release('z')

    # Quit mixer when music ends
    mixer.quit()

async def tts(fullstr):
    """
    Same as TEXT command, but it also says who made the command.
    """
    # Split user's name and their message
    str_tts = re.split('!tts', fullstr,flags=re.I)[1]
    str_user = re.split('!tts', fullstr,flags=re.I)[0].replace(':','')

    # This try-except avoids "no text inserted" error if someone types !TEXT with no text after the command call
    try:
        str_tts = spelling.correct_spell(str_tts, True)
        tts = gTTS(text="{} disse: {}".format(str_user,str_tts), lang=random.choice(LANGS))
        tts.save(TTS_PATH)
    except:
        return
    
    # Call event when music ends
    MUSIC_END = USEREVENT+1
    mixer.music.set_endevent(MUSIC_END)

    # Mixer config
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(TTS_PATH)

    # Force voicerecord button while TTS is playing
    keyboard.press('z')
    kb.block_key('z')
    mixer.music.play()
    while mixer.music.get_busy():
        pytime.wait(100)
        continue
    kb.unblock_key('z')
    keyboard.release('z')

    # Quit mixer when music ends
    mixer.quit()

async def play(fullstr):
    """
    Play music from YouTube
    """
    if await check_audio_playing(): return

    # Split username and their music request
    str_music = fullstr.split("!PLAY")[1]
    str_user = fullstr.split("!PLAY")[0].replace(':','')

    # Search text on YouTube
    str_music = spelling.correct_spell(str_music, True)
    search_result = VideosSearch(str_music, 1)
    search_result = search_result.result()

    # If no results were found, return with error
    if not search_result['result']:
        await console.write("say ERRO: Nenhum resultado encontrado para {}".format(str_music))
        return
    
    # Get first search result's URL
    url = search_result['result'][0]['link']
    title = search_result['result'][0]['title']
    title = spelling.remove_non_ascii(title)

    # Chat announcement
    await console.write("say {} solicitou a musica {}. Pesquisando...".format(str_user, str_music))
    
    # Download audio from video
    ydl_opts = {
        'outtmpl': MUSIC_TEMP_PATH,
        'format': 'worstaudio/worst',
        'fixup': 'never'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        await console.write("say ERRO: Erro desconhecido ao baixar a musica")
        os.remove(MUSIC_TEMP_PATH)
        return
    
    # Ignore if file is too long (>8MB)
    if os.path.getsize(MUSIC_TEMP_PATH) > 8388608:
        await console.write("say ERRO: Musica muito longa")
        os.remove(MUSIC_TEMP_PATH)
        return
    
    # Compress MP3 and delete tmp file
    AudioSegment.from_file(MUSIC_TEMP_PATH).export(MUSIC_OUTPUT_PATH, format='mp3')
    os.remove(MUSIC_TEMP_PATH)

    # Play audio in VB-Cable
    await console.write("say Tocando: {};+voicerecord".format(title))
    MUSIC_END = USEREVENT+1
    mixer.music.set_endevent(MUSIC_END)
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(MUSIC_OUTPUT_PATH)
    mixer.music.play()
    while mixer.music.get_busy():
        pytime.wait(100)
        continue
    await console.write("say Fim da musica!;-voicerecord")
    mixer.quit()

async def cancel():
    if await check_audio_playing(True):
        mixer.music.stop()
    else:
        await console.write("say Nenhuma musica sendo tocada no momento.")

async def meme():
    """
    Play a random meme.
    """

    # Load random meme
    meme = random.choice(os.listdir(MEME_PATH))
    
    # Call event when music ends
    MUSIC_END = USEREVENT+1
    mixer.music.set_endevent(MUSIC_END)

    # Mixer config
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(MEME_PATH + meme)

    # Force voicerecord button while TTS is playing
    keyboard.press('z')
    kb.block_key('z')
    mixer.music.play()
    while mixer.music.get_busy():
        pytime.wait(100)
        continue
    kb.unblock_key('z')
    keyboard.release('z')

    # Quit mixer when music ends
    mixer.quit() 

async def fake():
    """
    Play a fake sound.
    """

    # Load random meme
    fake = random.choice(os.listdir(FAKE_PATH))
    
    # Call event when music ends
    MUSIC_END = USEREVENT+1
    mixer.music.set_endevent(MUSIC_END)

    # Mixer config
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(FAKE_PATH + fake)

    # Force voicerecord button while TTS is playing
    keyboard.press('z')
    kb.block_key('z')
    mixer.music.play()
    while mixer.music.get_busy():
        pytime.wait(100)
        continue
    kb.unblock_key('z')
    keyboard.release('z')

    # Quit mixer when music ends
    mixer.quit() 

async def time():
    """
    Say the current time
    """
    now = datetime.now().strftime('%H:%M:%S').split(':')
    hours = now[0]
    minutes = now[1]
    seconds = now[2]

    tts = gTTS(text="São {} horas, {} minutos e {} segundos".format(hours,minutes,seconds), lang='pt')
    tts.save(TTS_PATH)

    
    # Call event when music ends
    MUSIC_END = USEREVENT+1
    mixer.music.set_endevent(MUSIC_END)

    # Mixer config
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(TTS_PATH)

    # Force voicerecord button while TTS is playing
    keyboard.press('z')
    kb.block_key('z')
    mixer.music.play()
    while mixer.music.get_busy():
        pytime.wait(100)
        continue
    kb.unblock_key('z')
    keyboard.release('z')

    # Quit mixer when music ends
    mixer.quit()

