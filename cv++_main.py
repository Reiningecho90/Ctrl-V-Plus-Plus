# imports
import keyboard as k
import pyperclip as pyp
import pyautogui as pya
import time as t
import tkinter as tk
import threading as th

class clipboard:
    def __init__(self):
        self.clipboard = {}
        self.clipboard_length = 0

    def add(self, value:str) -> dict:
        self.clipboard[self.clipboard_length+1] = value
        self.clipboard_length = self.clipboard_length+1

        return self.clipboard

    def clear(self) -> dict:
        self.clipboard = {}
        self.clipboard_length = 0

        return self.clipboard

    def listen_continuously(self) -> None:
        # to copy - CTRL+ALT+NUM
        # compensate for held keys
        held = {'copy': False,'paste': False}
        print('listening')

        while True:
            if k.is_pressed(f'ctrl+c'):
                if not held['copy']:
                    # 0-9 (10 objects)
                    if self.clipboard_length >= 10:
                        self.clear()

                    self.add(pyp.paste())
                    print('added ' + pyp.paste() + ' to cache at ' + str(self.clipboard_length))
                held['copy'] = True
            else:
                held['copy'] = False

            # paste with ctrl+alt+v+{num}
            # check from 1-9. 10 can't be typed as a single key
            # so we use 0 and replace as 10.
            for i in range(1,9):
                i2 = 0 if i == 10 else i

                if k.is_pressed(f'ctrl+alt+{str(i2)}'):
                    if not held['paste']:
                        t.sleep(0.5)
                        pyp.copy(self.clipboard[i])
                        pya.hotkey('ctrl', 'v')

                        held['paste'] = True
                        print('pasted ' + self.clipboard[i])
                    else:
                        held['paste'] = False

            t.sleep(0.01)


if __name__ == "__main__":
    # expandable listener function which calls
    # copy/paste class based on keyboard
    # action for more readability.
    clipboard = clipboard()

    th.Thread(target=clipboard.listen_continuously()).start()
