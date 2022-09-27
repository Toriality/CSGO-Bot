
import os
import re
from pydub import AudioSegment
from pygame import mixer, time, USEREVENT
from gtts import gTTS
from youtubesearchpython import VideosSearch
from pynput.keyboard import Controller

meme_path = './csgobot/sound/fake/'
out_path = './csgobot/sound/outpath/'
meme_files = os.listdir(meme_path)

for file in meme_files:
    print(file)
    AudioSegment.from_file(meme_path + file).export(out_path + file, format='mp3')