from tkinter import *  
import json
import os
from pathlib import Path


def main_directory():
    functions_directory = os.path.dirname(__file__)  
    directory = functions_directory.replace("functions",'')
    return directory


def path_json(name_json):
    path_json = Path(main_directory(), name_json)
    return path_json


def open_json(name_json):
    f = open(path_json(name_json))
    json_dictionary = json.load(f)
    return json_dictionary

database = open_json("database.json")

background_color = database['settings']['background_color']
font_style = database['settings']['font_style']
font_size = database['settings']['font_size']
font_color = database['settings']['font_color']

# BUTTONS
class Buttons:
        def __init__(self, text, command):
            self.text = text
            self.command = command
        
        def create(self):
            return Button(window, 
                            height=1,
                            width=2,
                            text = self.text,
                            command = self.command,
                            foreground=font_color,
                            background=background_color,
                            activeforeground=background_color,
                            activebackground=font_color,
                            font=(font_style, font_size))
        # CELSIUS - FAHRENHEIT
        def standard(self):
            return self.configure(foreground=background_color,
                            background="#505050",
                            activeforeground=background_color,
                            activebackground=background_color)
        
        def selected(self):
            return self.configure(foreground=font_color,
                            background=background_color,
                            activeforeground=background_color,
                            activebackground=font_color)
# FIELDS
class Fields:
    def __init__(self, width, background):
        self.width = width
        self.background = background
    
    def create(self):
        return Text(window,
                    height = 1,
                    width = self.width,
                    foreground="#303030",
                    background=self.background,
                    font=(font_style, "14", "bold"))

window = Tk()  
sb = Scrollbar(window)  
sb.pack(side = RIGHT, fill = Y)  
 
mylist = Listbox(window, yscrollcommand = sb.set )  
 
for line in range(60):  
 mylist.insert(END, "Number " + str(line))  
 
mylist.pack( side = LEFT )  
sb.config( command = mylist.yview )

mainloop()