from dataclasses import dataclass
from pathlib import Path
from json import load, dump
from copy import deepcopy


def get_path_json():
    path_json = Path(Path().resolve(), 'pyqt', 'database_pyqt.json')
    return path_json

def open_db():
    f = open(path_json)
    json_dictionary = load(f)
    return json_dictionary

def save_db():
    with open(path_json, 'w') as f:
        dump(db, f, indent=2)



path_json = get_path_json()
db = open_db()

@dataclass
class Data:
    window_widgets: object = None
    
    WINDOW_WIDTH: int = db['settings']['window_width']
    WINDOW_HEIGHT: int = db['settings']['window_height']
    
    BACKGROUND_COLOR: str = db['settings']['background_color']
    FIELD_BACKGROUND_COLOR: str = db['settings']['field_background_color']
    TEXT_FIELD_FONT_STYLE: str = db['settings']['text_field_font_style']
    TEXT_FIELD_FONT_SIZE: int = db['settings']['text_field_font_size']
    TEXT_FIELD_FONT_COLOR: str = db['settings']['text_field_font_color']
    SKILLS_POP_UP_WINDOW_POS_X: int = db['settings']['skills_pop_up_window_pos_x']
    SKILLS_POP_UP_WINDOW_POS_Y: int = db['settings']['skills_pop_up_window_pos_y']
    BUTTON_AND_LINE_FIELD_HEIGHT: int = db['settings']['button_and_line_field_height']
    INTRO_AND_JOBDESC_WIDTH: int = db['settings']['intro_and_jobdesc_width']


    ''' 
        Field objects placed the below "dic" in the
        src / text_field classes to able to
        iterate over at save
    '''
    dic = deepcopy(db)
    dic.pop('settings')


cv = Data()