# imports
import keyboard as k
import pyperclip as pyp
import pyautogui as pya
import time as t
import tkinter as tk

# dict for caching all lines of text
copy_dict = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: ''}

# baseline for text and integers
user_txt = ''
user_num = 0

# define boolean values for frontend use
copy_bool = False
clear_bool = False
paste_bool = False

# FINICKY WITH METACLASS ERRORS, REFORMAT TO FUNCTION BASED!

class Externals(copy_dict, user_num, user_txt): #grabs values needed for external use case

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
        self.int = self.Internals()
        return 0

    class Internals(copy_dict, user_txt, user_num, clear_bool, copy_bool): #grabs values needed for internal use case

        #
        # creates  copies of user's clipboard and saves to a dictionary above
        # can also fully clear cache by making everything standard again
        #


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
            else:
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



    def listener(self):
        if k.is_pressed(f'ctrl+c+1'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 0, user_txt)
        elif k.is_pressed(f'ctrl+c+2'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 1, user_txt)
        elif k.is_pressed(f'ctrl+c+3'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 2, user_txt)
        elif k.is_pressed(f'ctrl+c+4'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 3, user_txt)
        elif k.is_pressed(f'ctrl+c+5'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 4, user_txt)
        elif k.is_pressed(f'ctrl+c+6'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 5, user_txt)
        elif k.is_pressed(f'ctrl+c+7'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 6, user_txt)
        elif k.is_pressed(f'ctrl+c+8'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 7, user_txt)
        elif k.is_pressed(f'ctrl+c+9'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 8, user_txt)
        elif k.is_pressed(f'ctrl+c+0'):
            pya.hotkey('ctrl', 'c')
            user_txt = pyp.paste()
            self.int.cache_copy(self, 9, user_txt)

        if k.is_pressed(f'ctrl+v+1'):
            pyp.paste(self.copy_dict[0])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+2'):
            pyp.paste(self.copy_dict[1])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+3'):
            pyp.paste(self.copy_dict[2])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+4'):
            pyp.paste(self.copy_dict[3])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+5'):
            pyp.paste(self.copy_dict[4])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+6'):
            pyp.paste(self.copy_dict[5])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+7'):
            pyp.paste(self.copy_dict[6])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+8'):
            pyp.paste(self.copy_dict[7])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+9'):
            pyp.paste(self.copy_dict[8])
            pya.hotkey('ctrl', 'v')
        if k.is_pressed(f'ctrl+v+0'):
            pyp.paste(self.copy_dict[9])
            pya.hotkey('ctrl', 'v')
        
while 1:
    Externals.listener()