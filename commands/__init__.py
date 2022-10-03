from commands import info, audio, controls, chat, misc
from time import sleep
from worker import async_worker

# List of commands
COMMANDS_LIST = [
    # DEBUG
    "!DEBUG",
    # INFO
    "!HELP", "!DISCORD",
    # AUDIO
    "!PLAY", "!TEXT", "!TTS", "!CANCEL", "!MEME", "!FAKE", "!TIME", "!WEATHER", "!RADIO",
    # CONTROLS
    "!DROP",  "!KNIFE", "!CLICK", "!DUCK", "!INVERT", "!STOP", "!JUMP", "!SCOPE", "!RELOAD",
    # CHAT
    "!JOKE", "!TRIVIA", "!ALLAH", "!PASTE",
    # MISC
    "!KILL", "!BYE",
]

# Command execution
@async_worker
async def execute(cmd, fullstr=''):
    match cmd:
        # DEBUG
        case "!DEBUG": await debug()
        # INFO  
        case "!HELP": await info.help()
        case "!DISCORD": await info.discord()
        # AUDIO
        case "!TEXT": await audio.text(fullstr)
        case "!TTS": await audio.tts(fullstr)
        case "!PLAY": await audio.play(fullstr)
        case "!CANCEL": await audio.cancel()
        case "!MEME": await audio.meme()
        case "!FAKE": await audio.fake()
        case "!TIME": await audio.time()
        case "!WEATHER": await audio.weather(fullstr)
        case "!RADIO": await audio.radio(fullstr)
        # CONTROLS
        case "!DROP": controls.drop()
        case "!STOP": await controls.stop()
        case "!CLICK": controls.click()
        case "!SCOPE": controls.scope()
        case "!KNIFE": controls.knife()
        case "!DUCK": await controls.duck()
        case "!INVERT": await controls.invert()
        case "!JUMP": controls.jump()
        case "!RELOAD": controls.reload()
        # CHAT
        case "!JOKE": await chat.joke()
        case "!TRIVIA": await chat.trivia()
        case "!ALLAH": await chat.allah()
        case "!PASTE": await chat.paste()
        # MISC
        case "!BYE": await misc.bye()
        case "!KILL": await misc.kill()
        # ---
        case _: pass

async def debug():
    print('debug start')
    sleep(100)
    print('debug end')