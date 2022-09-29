# import vlc
# import time

# p = vlc.MediaPlayer("https://shout25.crossradio.com.br:18156/1")

# p.play()

# device = p.audio_output_device_enum()
# while device:
#     print ("playing on...")
#     print (device.contents.device)
#     print (device.contents.description)

#     p.audio_output_device_set(None, device.contents.device)
#     time.sleep(5)

#     device = device.contents.next

# p.stop()





import vlc
from time import sleep

url = "http://audio8.cmaudioevideo.com:8886/stream"

# Create VLC instance, media player and media
instance = vlc.Instance()
player = instance.media_player_new()
print(player.get_media() != None)   
media = instance.media_new(url)
player.set_media(media)

# Get list of output devices
def get_device():
    mods = player.audio_output_device_enum()
    if mods:
        mod = mods
        while mod:
            mod = mod.contents
            # If VB-Cable is found, return it's module and device id
            if 'CABLE Input (VB-Audio Virtual Cable)' in str(mod.description):
                device = mod.device
                module = mod.description
                return device,module
            mod = mod.next

# Sets the module and device id to VB-Cable           
device,module = get_device()

# Sets VB-Cable as output device
player.audio_output_device_set(None, device)

# Audio plays in default output device, which is incorrect
player.play()

while player.is_playing():
    sleep(2)
    player.get_media()
    sleep(2)
    player.stop()
    continue
#player.release()
sleep(2)
player.get_media()