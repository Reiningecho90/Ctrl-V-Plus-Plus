# imports
import keyboard as k
import pyperclip as pyp
import pyautogui as pya
import time as t
import tkinter as tk
import threading as th
import logging
    
class clipboard:
    def __init__(self, loglevel):
        self.clipboard = {}
        self.clipboard_logger = logging.getLogger('clipboard')
        self.clipboard_logger.setLevel(loglevel)

        # log to predetermined file
        self.handler = logging.FileHandler('logs.log')

        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.clipboard_logger.addHandler(self.handler)

        # track release of keys so that someone can't
        # overwrite clipboard content by holding
        # key.
        self.keybinds = {
            'copy_down': False,
            'paste_down': False
        }

        # store if key was pressed at last loop
        # to copy when it isn't.
        self.last_iter = {
            'copy': False,
            'paste': False
        }

    def add(self, value:str, index:int) -> dict:
        self.clipboard[index] = value

        return self.clipboard

    def listen_continuously(self) -> None:
        # to copy - CTRL+ALT+NUM
        # compensate for held keys
        self.clipboard_logger.info("listening...")

        while True:
            # paste with ctrl+alt+v+{num}
            # check from 1-9. 10 can't be typed as a single key
            # so we use 0 and replace as 10.
            for i in range(1,11):
                i2 = 0 if i == 10 else i

                if k.is_pressed(f'ctrl+c+{str(i2)}'):
                    self.keybinds['copy_down'] = True
                    self.last_iter['copy'] = True
                else:
                    self.keybinds['copy_down'] = False

                if k.is_pressed(f'ctrl+alt+{str(i2)}'):
                    self.keybinds['paste_down'] = True
                    self.last_iter['paste'] = True
                else:
                    self.keybinds['paste_down'] = False

                if not self.keybinds['copy_down']:
                    if self.last_iter['copy']:
                        # subtract 1 from i2 since the listener for keyup
                        # always fires after the actual keypress.

                        self.last_iter['copy'] = False
                        t.sleep(0.5)

                        self.add(pyp.paste(), i2-1)
                        self.clipboard_logger.info("Added "+pyp.paste()+" to cache at "+str(i2-1))
                elif not self.keybinds['paste_down']:
                    if self.last_iter['paste']:
                        self.last_iter['paste'] = False

                        pyp.copy(self.clipboard[i2-1])
                        pya.hotkey('ctrl', 'v')

                        self.clipboard_logger.info("Pasted "+pyp.paste())

            t.sleep(0.01)


if __name__ == "__main__":
    # expandable listener function which calls
    # copy/paste class based on keyboard
    # action for more readability.
    clipboard = clipboard(logging.INFO)

    th.Thread(target=clipboard.listen_continuously()).start()
