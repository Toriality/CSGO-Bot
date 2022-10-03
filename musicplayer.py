import vlc
import pafy
import keyboards
from time import sleep

# Starts the VLC instance and media player
instance = vlc.Instance()
player = instance.media_player_new()
device = b'{0.0.0.00000000}.{7ee6e415-46bf-442f-a002-4ca3b8ea07e8}'
print(player.audio_get_volume())

def get_pafy_url(youtube_link):
    """
    Return audio URL from YouTube to start streaming it
    """
    audio = pafy.new(youtube_link)
    best = audio.getbestaudio()
    playurl = best.url
    return playurl

def start(media_link, mode):
    """
    Load media into VLC with VB-Cable output
    """
    # Check if VLC is already playing audio
    if player.is_playing():
        player.set_media(None)
        sleep(1)
    
    # Load media into VLC player
    media = instance.media_new(media_link)
    media.get_mrl()
    player.set_media(media)
    player.audio_output_device_set(None, device)
    if mode == 'text': player.audio_set_volume(100)
    if mode == 'yt': player.audio_set_volume(58)
    if mode == 'radio': player.audio_set_volume(55)

async def record():
    """
    Force voicerecord
    """
    # Configure keyboard
    Key =  keyboards.get_keys()
    keyboard,kb = keyboards.get_keyboard_kb()

    # Force voice record button
    kb.send('z', True, False)
    kb.block_key('z')
    player.play()
    sleep(7)
    while player.is_playing():
        sleep(0.5)
    kb.unblock_key('z')
    kb.release('z')
    player.set_media(None)

def stop():
    """
    Stop media
    """
    # Return false if no media is playing
    if player.is_playing() == False:
        return False
    
    # Stop and return true
    player.stop()
    return True