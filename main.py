from tkinter import *
import json
import os
from pathlib import Path
import pyperclip

import second_page


def main_directory():
    functions_directory = os.path.dirname(__file__)  
    directory = functions_directory.replace("functions",'')
    return directory


def path_json(name_json):
    path_json = Path(main_directory(), name_json)
    return path_json


def open_db(name_json):
    f = open(path_json(name_json))
    json_dictionary = json.load(f)
    return json_dictionary

def save_db(database):
    with open(path_json('database.json'), 'w') as f:
        json.dump(database, f, indent=2)


# BUTTONS
class Buttons:
        def __init__(self, text, command):
            self.text = text
            self.command = command
        
        def create(self):
            return Button(window, 
                            height=1,
                            width=5,
                            text = self.text,
                            command = self.command,
                            foreground=font_color,
                            background=background_color,
                            activeforeground=background_color,
                            activebackground=field_background_color,
                            font=(font_style, 16, "bold"))

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
                    font=(font_style, "14")) #(font_style, "14", "bold") 

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
database = open_db("database.json")

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
# screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/1.9, 0))    # (screen_width/2-275, screen_height/8) - position to the middle of the screen
window.resizable(0,0)   # locks the main window
window.configure(background=background_color)

# WINDOW ICON
working_directory = os.path.dirname(__file__)
path_icon = Path(working_directory, "pictures", "icon.ico") 
window.iconbitmap(path_icon)

# COPY TO CLIPBOARD AT START
pyperclip.copy(database['contacts']['email'])


### WIDGETS
self = {}   # to able to save the updates + for the copy buttons

def create_text(text, x, y):
    self[text] = Title(text, font_style, font_size).create()
    self[text].place(x=x, y=y)


def create_field(dic_name,width, height, x, y):     # for FULL NAME, INTRO
    self[dic_name] = Fields(width, height, field_background_color).create()
    self[dic_name].insert(END,database[dic_name])
    self[dic_name].place(x=x, y=y)


def create_contacts_field(contacts_type, width, height, x, y):
    self[contacts_type] = Fields(width, height, field_background_color).create()
    self[contacts_type].insert(END,database['contacts'][contacts_type])
    self[contacts_type].place(x=x, y=y)


def create_field_plus(dic_name, field_name, width, height, x, y):   # for EXPEREIENCE, EDUCATION
    unique_name = f'{item}_{field_name}'
    self[unique_name] = Fields(width, height, field_background_color).create()
    self[unique_name].insert(END,database[dic_name][item][field_name])
    self[unique_name].place(x=x, y=y)
    # SCROLLBAR - unnecessary, text is already scrollable
    # if field_name == 'description':
    #     scrollbar = ttk.Scrollbar(window, orient='vertical', command=self[dic_name].yview)
    #     self[dic_name].configure(yscrollcommand = scrollbar.set)
    #     # scrollbar.place(x=x, y=y) #(relx=1, rely=0, relheight=1, anchor='ne')

# COPY BUTTON
def copy(field_value):
    pyperclip.copy(field_value)

def copy_button(field_value, x, y):
    c_button = Buttons('', lambda:[copy(self[field_value].get("1.0", "end-1c"))]).create()
    c_button.configure(height=1, width=2, font=(font_style, 10))
    c_button.place(x=x, y=y)

def y_location(gap):
    location = y_base + 40 * gap
    return location


# PACING
y_base=40
x_left_side_field = 55
x_left_side_button = 25
x_right_side_field = window_width-295
x_right_side_button = window_width-325


# FULL NAME
create_text('FULL NAME', x_left_side_button-5, y_location(0))
create_field('full_name', 25, 1, x_left_side_field, y_location(1))
copy_button('full_name', x_left_side_button, y_location(1))

# INTRO
create_text('INTRO', x_left_side_button-5, y_location(2))
create_field('intro', 80, 5, x_left_side_field, y_location(3))
copy_button('intro', x_left_side_button, y_location(3))

# CONTACTS
create_text('CONTACTS', x_right_side_button-5, y_location(2))
n=3
for item in database['contacts']:
    create_contacts_field(item, 26, 1, x_right_side_field, y_location(n))
    copy_button(item, x_right_side_button, y_location(n))
    n += 1

# EDUCATION
create_text('EDUCATION', x_right_side_button-5, y_location(9))
n=10
for item in database['education']:
    # SUBJECT
    create_field_plus('education', "subject", 26, 1, x_right_side_field, y_location(n))
    copy_button(f'{item}_subject', x_right_side_button, y_location(n))
    # SCHOOL
    create_field_plus('education', "school", 26, 1, x_right_side_field, y_location(n+1))
    copy_button(f'{item}_school', x_right_side_button, y_location(n+1))
    # FROM
    gap = 50
    create_field_plus('education', "from_edu", 8, 1, x_right_side_field+gap, y_location(n+2))
    copy_button(f'{item}_from_edu', x_right_side_button+gap, y_location(n+2))
    # TO
    create_field_plus('education', "to_edu", 8, 1, x_right_side_field+180, y_location(n+2))
    copy_button(f'{item}_to_edu', x_right_side_field+150, y_location(n+2))
    n += 3

# SKILLS
create_text('SKILLS', x_right_side_button-5, y_location(17))
create_field('skills', 26, 12, x_right_side_field, y_location(18))
copy_button('skills', x_right_side_button, y_location(18))

# EXPEREIENCE
create_text('EXPERIENCE', x_left_side_button-5, y_location(7))
n=8
for item in database['experience']:
    #TITLE
    create_field_plus('experience', "title", 25, 1, x_left_side_field, y_location(n))
    copy_button(f'{item}_title', x_left_side_button, y_location(n))
    #COMPANY
    create_field_plus('experience', "company", 25, 1, x_left_side_field, y_location(n+1))
    copy_button(f'{item}_company', x_left_side_button, y_location(n+1))
    # DESCRIPTION
    create_field_plus('experience', "description", 80, 5, x_left_side_field, y_location(n+2))
    copy_button(f'{item}_description', x_left_side_button, y_location(n+2))
    # FROM
    create_field_plus('experience', "from", 9, 1, x_left_side_field+300, y_location(n))
    copy_button(f'{item}_from', x_left_side_button+300, y_location(n))
    # TO
    create_field_plus('experience', "to", 9, 1, x_left_side_field+300, y_location(n+1))
    copy_button(f'{item}_to', x_left_side_button+300, y_location(n+1))
    n += 6

# SAVE BUTTON
def save_update():
    # FULL NAME
    database['full_name'] = self['full_name'].get("1.0", "end-1c")
    # INTRO
    database['intro'] = self['intro'].get("1.0", "end-1c")
    # CONTACTS
    for contacts_type in database['contacts']:
        database['contacts'][contacts_type] = self[contacts_type].get("1.0", "end-1c")
    # EDUCATION
    for item in database['education']:
        for field_name in database['education'][item]:
            unique_name = f'{item}_{field_name}'
            database['education'][item][field_name] = self[unique_name].get("1.0", "end-1c")
    # SKILLS
    database['skills'] = self['skills'].get("1.0", "end-1c")
    # EXPERIENCE
    for item in database['experience']:
        for field_name in database['experience'][item]:
            unique_name = f'{item}_{field_name}'
            database['experience'][item][field_name] = self[unique_name].get("1.0", "end-1c")
    save_db(database)

save_button = Buttons('Save', save_update).create()
save_button.place(x=window_width-95, y=y_location(0)+10)

# 2ND PAGE BUTTON
second_page_button = Buttons('2nd', lambda: [second_page.launch(window)]).create()
second_page_button.place(x=window_width-165, y=y_location(0)+10)

mainloop()