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
user_num = 0

# define boolean values for frontend use
copy_bool = False
clear_bool = False
paste_bool = False

# single class based for all worker functions, GUI separate

class Worker(copy_dict, user_num, user_txt): #grabs values needed for external use case

    #
    # copies text from dictionary to user's clipboard
    # gets user input for which text to copy
    # outputs text to user's clipboard
    #

    def __init__(self, copy_dict, user_num, user_txt): # grabs dictionary values
        self.copy_dict = copy_dict
        self.user_num = user_num
        self.user_txt = user_txt
        self.out_txt = ''
        self.grab_bool = False

    def __init__(self, copy_dict): # grabs dict, creates self bool values
        self.copy_dict = copy_dict
        self.copy_bool = False
        self.clear_bool = False


    def cache_copy(self, user_num, user_txt): # copies user's clipboard to a dictionary value based on hotkey
        if user_num != 0:
            self.copy_dict[user_num] = user_txt
            copy_dict.update(self.copy_dict)
            self.copy_bool = True
            copy_bool
            copy_bool = True
            return self.copy_bool
        else: # only for tenth copy or paste due to keyboard formatting irl
            self.copy_dict[10] = user_txt
            copy_dict.update(self.copy_dict)
            self.copy_bool = True
            copy_bool
            copy_bool = True
            return self.copy_bool
        # confirm text cached


    def cache_clear(self): # clears entire cache
        self.copy_dict = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: ''}
        copy_dict.update(self.copy_dict)
        self.clear_bool = True
        clear_bool
        clear_bool = True
        # clears cache


    def listener_copy(self):
        while 1:
            for i in range(0, 10):
                if k.is_pressed(f'ctrl+c+{str(i)}'): # uses previously compiled function to cache text selected
                    self.user_num = i
                    self.user_txt = pyp.paste()
                    self.cache_copy(self.user_num, self.user_txt)
                    self.out_txt = self.user_txt
                    return self.out_txt
                else:
                    continue

    def listener_paste(self):
        while 1:
            for i in range(0, 10):
                if k.is_pressed(f'ctrl+v+{str(i)}'): # uses previously compiled function to paste text selected
                    pya.hotkey('ctrl', 'v')
                    pyp.copy(self.copy_dict[i])
                    self.paste_bool = True
                    paste_bool
                    paste_bool = True
                    return self.paste_bool # returns for frontend use (tkinter listener loop)
                else:
                    continue


# establish and run threads/main body

if __name__ == '__main__':
    th.Thread(target=Worker.listener_copy, args=(Worker)).start()
    print('t1 started')
    th.Thread(target=Worker.listener_paste, args=(Worker)).start()
    print('t2 started')