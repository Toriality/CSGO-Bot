from time import sleep
import asyncio
import stringfy
import spelling
import commands
import threading

last_cmd = ''

async def track():
    """
    Keep taking pictures of the screen to keep on track of the in-game chat. Run command when tracker finds a string with a command.\n
    Arguments:
        mode: 'normal' for most of purposes. 'music' for execute the tracker parallel with music player function.
    """
    # Tracks last command read
    global last_cmd
    # Loop
    while(True):
        clear_cmd_thread = threading.Thread(target=clear_cmd)
        str = stringfy.stringfy()   
        str = spelling.correct_spell(str)
        for command in commands.COMMANDS_LIST:
            if command in str.upper():
                if command != last_cmd:
                    last_cmd = command
                    task = asyncio.create_task(commands.execute(command, str))
                    await asyncio.gather(task)
                    clear_cmd_thread.start()
             
def clear_cmd():
    """
        Avoid the same command being executed every new screenshot.
    """
    global last_cmd
    sleep(10)
    last_cmd = ''

# Calling the function
asyncio.run(track())







