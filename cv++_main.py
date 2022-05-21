# imports
import keyboard as k
import pyperclip as pyp
import pyautogui as pya
import time as t
import tkinter as tk
import threading as th

# dict for caching all lines of text
copy_dict = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: ''}

# baseline for text and integers
user_txt = ''
user_num = 1

# single class based for all worker functions, GUI separate

class Worker: # grabs values needed for external use case

    #
    # copies text from dictionary to user's clipboard
    # gets user input for which text to copy
    # outputs text to user's clipboard
    #

    def __init__(self, copy_dict=copy_dict, user_num=user_num, user_txt=user_txt): # grabs dictionary values
        self.copy_dict = copy_dict
        print(self.copy_dict)
        self.usr_num = user_num
        print(self.usr_num)
        self.user_txt = user_txt
        print(self.user_txt)
        self.out_txt = ''


    def cache_copy(self): # copies user's clipboard to a dictionary value based on hotkey
        if user_num != 0:
            k.press_and_release('ctrl+c')
            pyp.copy(self.user_txt)
            pyp.paste()
            self.copy_dict[self.usr_num] = self.user_txt
            print('copied to cache')
            copy_dict.update(self.copy_dict)
            print('cache' + str(copy_dict))

        else: # only for tenth copy or paste due to keyboard formatting irl
            k.press_and_release('ctrl+c')
            pyp.copy(self.user_txt)
            pyp.paste()
            self.copy_dict[10] = self.user_txt
            print('copied to cache')
            copy_dict.update(self.copy_dict)
            print('cache' + str(copy_dict))
            # confirm text cached


    def cache_clear(self): # clears entire cache
        self.copy_dict = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: ''}
        copy_dict.update(self.copy_dict)
        # clears cache

    def listener_copy(self):
        for i in range(1, 10):
            print('run-copy')
            if k.is_pressed(f'ctrl+alt+{str(i)}'): # uses previously compiled function to cache text selected
                print('caching')
                self.usr_num = i
                self.user_txt = pyp.paste()
                self.cache_copy(self)
                print('cached')
                print(copy_dict)
                t.sleep(0.1)
            
            else:
                continue

    def listener_paste(self):
        for i in range(1, 10):
            print('run-paste')
            if k.is_pressed(f'shift+ctrl+alt+{str(i)}'): # uses previously compiled function to paste text selected
                print('pasting')
                pyp.copy(str(copy_dict[i]))
                k.press_and_release('ctrl+v')
                t.sleep(0.1)
                
            else:
                continue


# establish and run threads/main body

if __name__ == '__main__':

    # establish __init__ passes for worker class
    Worker.__init__(Worker, copy_dict)
    print('worker init')

    while 1:
        th.Thread(target=Worker.listener_copy(Worker)).start()
        th.Thread(target=Worker.listener_paste(Worker)).start()