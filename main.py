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
    def __init__(self, width, height, background):
        self.width = width
        self.height = height
        self.background = background
    
    def create(self):
        return Text(window,
                    width = self.width,
                    height = self.height,
                    foreground=field_font_color,
                    background=self.background,
                    font=(font_style, "14", "bold"))

# TITLE
class Title:
    def __init__(self, text, font_style, font_size):
        self.text = text
        self.font_style = font_style
        self.font_size = font_size
    
    def create(self):
        return Label(window,
                     text = self.text,
                     font = (self.font_style, self.font_size, 'bold'),
                     foreground=font_color,
                     background=background_color)

# LOAD DB
database = open_json("database.json")

background_color = database['settings']['background_color']
field_background_color = database['settings']['field_background_color']
field_font_color = database['settings']['field_font_color']
font_style = database['settings']['font_style']
font_size = database['settings']['font_size']
font_color = database['settings']['font_color']

# WINDOW
window = Tk()
window.title(database['settings']['window_title'])
window_width = database['settings']['window_width']
window_length = database['settings']['window_length']
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/2-275, screen_height/5))    #   position to the middle of the screen
window.resizable(0,0)   # locks the main window
window.configure(background=background_color)

### WIDGETS
x_base=30
y_base=40
y_base_right_side = window_width-300
y_gap=40
self = {}

def y_location(gap):
    location = y_base + 40 * gap
    return location

def create_text(text, x, y):
    self[text] = Title(text, font_style, font_size).create()
    self[text].place(x=x, y=y)

def create_field(dic_name, width, height, x, y):
    self[dic_name] = Fields(width, height, field_background_color).create()
    self[dic_name].place(x=x, y=y)
    if dic_name != 'contacts':
        self[dic_name].insert(END,database[dic_name])
    else:
        self[dic_name].insert(END,database['contacts'][item])


# FULL NAME
create_text('FULL NAME', x_base, y_location(0))
create_field('full_name', 22, 1, x_base, y_location(1))

# INTRO
create_text('INTRO', x_base, y_location(2))
create_field('intro', 80, 5, x_base, y_location(3))

# CONTACTS
create_text('CONTACTS', y_base_right_side, y_location(2))
n=3
for item in database['contacts']:
    create_field('contacts', 26, 1, y_base_right_side, y_location(n))
    n += 1









mainloop()