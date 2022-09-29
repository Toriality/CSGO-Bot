import console
import spelling
import yt_dlp
import random
import os
import re
import vlc
import python_weather
import keyboard as kb
from time import sleep
from datetime import datetime
from pydub import AudioSegment
from pygame import mixer, time as pytime, USEREVENT
from gtts import gTTS
from youtubesearchpython import VideosSearch
from pynput.keyboard import Controller

keyboard = Controller()
instance = vlc.Instance()
player = instance.media_player_new()

TTS_PATH = './csgobot/sound/tts.mp3'
MUSIC_TEMP_PATH = '../csgobot/sound/tmp.mp3'
MUSIC_OUTPUT_PATH = '../csgobot/sound/out.mp3'
MEME_PATH = './csgobot/sound/meme/'
FAKE_PATH = './csgobot/sound/fake/'
LANGS = ['pt','en','fr','zh-CN','zh-TW','es','af','ar','bg','hr','el','it','ko','sv','vi']
RADIOS = {
    1: {
        'name': 'Radio Gazeta FM 88,1 (SP)',
        'url': 'https://shout25.crossradio.com.br:18156/1'
    },
    2: {
        'name': 'Radio BEAT 98 (RJ)',
        'url': 'http://stream-11.zeno.fm/342u05cu92quv?zs=qcppd3MyQmyNlNOvjvU7_Q&rj-ttl=5&rj-tok=AAABcGAtmasAMWLGevIIOR2B1g'
    },
    3: {
        'name': 'Radio NATIVA 95,3 (SP)',
        'url': 'http://audio8.cmaudioevideo.com:8886/stream'
    },
    4: {
        'name': 'Radio TUPI 96,5 FM (RJ)',
        'url': 'https://8923.brasilstream.com.br/stream'
    },
    5: {
        'name': 'Radio Mix 102.1 (RJ)',
        'url': 'https://22823.live.streamtheworld.com/MIXRIO_SC?DIST=TuneIn&TGT=TuneIn&maxServers=2&gdpr=0&us_privacy=1YNY&partnertok=eyJhbGciOiJIUzI1NiIsImtpZCI6InR1bmVpbiIsInR5cCI6IkpXVCJ9.eyJ0cnVzdGVkX3BhcnRuZXIiOnRydWUsImlhdCI6MTYxNDM1MjgxNSwiaXNzIjoidGlzcnYifQ.Sy0Yz7hGYogNuLrQA5XwsRHiz4iXe5I3ejbJJMNgy88'
    },
    6: {
        'name': 'Antena 1 - 103,7 (RJ)',
        'url': 'http://linux1.rd8.com.br:8000/antena1rio'
    },
    7: {
        'name': 'Antena 1 - 94,7 (SP)',
        'url': 'http://antena1.newradio.it/stream2'
    },
    8: {
        'name': '91 Rock - 96,3 (PR)',
        'url': 'https://servidor40-4.brlogic.com:8044/live'
    },
    9: {
        'name': 'Radio Eldourado FM 107,3',
        'url': 'http://cast4.audiostream.com.br:8652/mp3'
    },
    10: {
        'name': 'Radio Grenal FM 95,9',
        'url': 'http://cast4.audiostream.com.br:8649/mp3'
    },
    11: {
        'name': 'Antena Mais (Esch sur Alzette)',
        'url': 'https://sp0.redeaudio.com/8084/stream/1/'
    },
    12: {
        'name': 'Country Radio Gilsdorf',
        'url': 'http://5.35.250.101:8000/crgilsdorf'
    },
    13: {
        'name': 'L-essentiel radio 107.7',
        'url': 'http://lessentielradio.ice.infomaniak.ch/lessentielradio-128.mp3'
    },
    14: {
        'name': 'FRL- Free Radio Luxembourg',
        'url': 'https://listen.radioking.com/radio/66160/stream/103807'
    },
    15: {
        'name': 'CCFM 107.5 - Cape Community FM',
        'url': 'http://edge.iono.fm/xice/69_medium.mp3'
    }
}


async def check_audio_playing(is_cancelling=False):
    if mixer.get_init():
        if not is_cancelling:
            await console.write("say ERRO: Canal de audio ocupado. Use !CANCEL")
        return True
    if player.get_media() != None:
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
    if await check_audio_playing(): return

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
    str_music = re.split('!PLAY', fullstr, flags=re.I)[1]
    str_user = re.split('!PLAY', fullstr,flags=re.I)[0].replace(':','')

    # Search text on YouTube
    #str_music = spelling.correct_spell(str_music, True)
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
        try:
            mixer.music.stop()
        except:
            player.stop()
            player.set_media(None)
    else:
        await console.write("say Nenhuma musica sendo tocada no momento.")

async def meme():
    """
    Play a random meme.
    """
    if await check_audio_playing(): return

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
    if await check_audio_playing(): return

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
    if await check_audio_playing(): return

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

async def weather(fullstr):
    """
    Get weather of a place
    """
    if await check_audio_playing(): return

    # Declare the client
    try:
        async with python_weather.Client() as client:
            # Get location
            str_loc = re.split('!WEATHER', fullstr,flags=re.I)[1]

            # Fetch a weather forecast from location
            weather = await client.get(str_loc)
            if weather.location == None:
                await console.write("say ERRO: Não encontrei o clima de {}".format(str_loc))
                return

            # Speech string
            str_tts = "O clima para {} é de {} graus".format(str_loc, weather.current.temperature)
            await client.close()

            # Audioz
            tts = gTTS(text=str_tts, lang='pt')
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
    except Exception as e:
        await console.write("say ERRO: Ocorreu algum erro ao conectar-se com o servidor.")
        return

async def radio(fullstr):
    """
    Play radio stream
    """
    if await check_audio_playing(): return

    # Get requested id number
    # Split string after !radio
    radio_id = re.split('!radio', fullstr, flags=re.I)[1]
    # Remove non-digit characters from string
    radio_id = re.sub(r'[^0-9]', '', radio_id)
    # Pick the first two characters
    radio_id = int(radio_id[:2])

    # Check if it is a valid ID
    try: RADIOS[radio_id]
    except: return await console.write('say ERROR: ID invalido. Use um numero de 1 a 15')

    # Radio information
    radio_url = RADIOS[radio_id]['url']
    radio_name = RADIOS[radio_id]['name']

    # Config VLC
    media = instance.media_new(radio_url)
    print(radio_url)
    player.set_media(media)
    device = b'{0.0.0.00000000}.{7ee6e415-46bf-442f-a002-4ca3b8ea07e8}'
    player.audio_output_device_set(None, device)

    # Chat announce
    await console.write('say Tocando: {}'.format(radio_name))

    # Force voicerecord
    keyboard.press('z')
    kb.block_key('z')
    player.play()
    sleep(10)
    while player.is_playing():
        sleep(1)
        continue
    kb.unblock_key('z')
    keyboard.release('z')
