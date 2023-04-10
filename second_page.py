# 2ND BUTTON - POP UP WINDOW

from tkinter import *
import json
import os
from pathlib import Path
import pyperclip


def launch(window):
        
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
                return Button(top_window, 
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
            return Text(top_window,
                        width = self.width,
                        height = self.height,
                        foreground=field_font_color,
                        background=self.background,
                        font=(font_style, "14"))

    # TITLE
    class Title:
        def __init__(self, text, font_style, font_size):
            self.text = text
            self.font_style = font_style
            self.font_size = font_size
        
        def create(self):
            return Label(top_window,
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
    top_window = Toplevel(window)
    top_window.title("Easy Apply - Second Page")
    window_width = database['settings']['window_width']
    window_length = database['settings']['window_length']-30
    screen_width = window.winfo_screenwidth()
    top_window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width/1.9, 30))    # (screen_width/2-275, screen_height/8) - position to the middle of the screen
    top_window.resizable(0,0)   # locks the main window
    top_window.configure(background=background_color)
    # WINDOW ICON
    working_directory = os.path.dirname(__file__)
    path_icon = Path(working_directory, "pictures", "icon.ico") 
    top_window.iconbitmap(path_icon)
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

    def create_field_plus(dic_name, field_name, width, height, x, y):   # for EXPEREIENCE, EDUCATION
        unique_name = f'{item}_{field_name}'
        self[unique_name] = Fields(width, height, field_background_color).create()
        self[unique_name].insert(END,database[dic_name][item][field_name])
        self[unique_name].place(x=x, y=y)

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

    # EXPERIENCE - CONTINUED
    create_text('EXPERIENCE - CONTINUED', x_left_side_button-5, y_location(0)-10)
    n=1
    for item in database['experience_2nd']:
        #TITLE
        create_field_plus('experience_2nd', "title", 25, 1, x_left_side_field, y_location(n))
        copy_button(f'{item}_title', x_left_side_button, y_location(n))
        #COMPANY
        create_field_plus('experience_2nd', "company", 25, 1, x_left_side_field, y_location(n+1))
        copy_button(f'{item}_company', x_left_side_button, y_location(n+1))
        # DESCRIPTION
        create_field_plus('experience_2nd', "description", 80, 5, x_left_side_field, y_location(n+2))
        copy_button(f'{item}_description', x_left_side_button, y_location(n+2))
        # FROM
        create_field_plus('experience_2nd', "from", 9, 1, x_left_side_field+300, y_location(n))
        copy_button(f'{item}_from', x_left_side_button+300, y_location(n))
        # TO
        create_field_plus('experience_2nd', "to", 9, 1, x_left_side_field+300, y_location(n+1))
        copy_button(f'{item}_to', x_left_side_button+300, y_location(n+1))
        n += 6
    
    # ACHIEVEMENTS
    create_text('ACHIEVEMENTS', x_right_side_button-5, y_location(1))
    create_field('achievements_2nd', 26, 20, x_right_side_field, y_location(2))
    copy_button('achievements_2nd', x_right_side_button, y_location(2))

    # EXTRA
    gap=-10
    create_text('EXTRA', x_right_side_button-5, y_location(14)+gap)
    create_field('extra_2nd', 26, 16, x_right_side_field, y_location(15)+gap)
    copy_button('extra_2nd', x_right_side_button, y_location(15)+gap)

    # SAVE BUTTON
    def save_update():
        # ACHIEVEMENTS
        database['achievements_2nd'] = self['achievements_2nd'].get("1.0", "end-1c")        
        # EXTRA
        database['extra_2nd'] = self['extra_2nd'].get("1.0", "end-1c")
        # EXPERIENCE
        for item in database['experience_2nd']:
            for field_name in database['experience_2nd'][item]:
                unique_name = f'{item}_{field_name}'
                database['experience_2nd'][item][field_name] = self[unique_name].get("1.0", "end-1c")
        save_db(database)

    save_button = Buttons('Save', save_update).create()
    save_button.place(x=window_width-95, y=y_location(0))
