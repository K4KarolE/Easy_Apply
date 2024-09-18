from dataclasses import dataclass
from pathlib import Path
from json import load, dump


def get_path_json():
    path_json = Path(Path().resolve(), "pyqt", "database_pyqt.json")
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
    WINDOW_TITLE: str = db['settings']['window_title']
    WINDOW_WIDTH: int = db['settings']['window_width']
    WINDOW_HEIGHT: int = db['settings']['window_height']

    BACKGROUND_COLOR: str = db['settings']['background_color']
    FIELD_BACKGROUND_COLOR: str = db['settings']['field_background_color']
    FIELD_FONT_COLOR: str = db['settings']['field_font_color']
    FONT_STYLE: str = db['settings']['font_style']
    FONT_SIZE: str = db['settings']['font_size']
    FONT_COLOR: str = db['settings']['font_color']
    COPY_TO_CLIPBOARD: bool = db['settings']['copy_to_clipboard']


cv = Data()