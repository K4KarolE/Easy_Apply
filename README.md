# Easy Apply
- Have you ever been annoyed by the repetitive nature of the job applications?
    - Most of the time the data extraction from your resume (if there is an option at all) do not work properly, so you need to select and copy-paste the same information over and over again every time you apply for a new role
- `Easy Apply` let you add the information into your clipboard by just clicking on a button of the selected field
- Versions: `PyQt6` and `Tkinter`

<br>
<div align="center">
    <img src="pictures/screenshot.png"</img> 
</div>
<br>

# Requirements
### Install packages\dependencies
#### PyQT6
``` pip install -r requirements_pyqt.txt ```
#### Tkinter
``` pip install -r requirements.txt ```

### Python 3 - used: 3.12
- https://www.python.org/

### OS
- `Windows` (tested on 11)

# Guide - Tkinter (older version)
- The app window opens at the right, top corner of the screen
    - optimised for `27" - 2560x1440` monitor
    - for smaller display, the `PyQt` version recommended
- The first row of the `Contacts` automatically added to the clipboard at the start of the app when the `copy_to_clipboard_page_1` set to true in `json/settings`
- `Skills`:
    - the 1st button copies the skill list in bulk/together
    - the 2nd button copies the skills one by one, pop-up message displaying the current skill in clipboard, jumps to the next skill, once the pop-up message is closed
- At the launch of the 2nd page the `Achievements` field value automatically added to the clipboard when the `copy_to_clipboard_page_2` set to true in `json/settings`

# Guide - PyQt (latest version)
- Buttons behave the same way as in the `Tkinter` version
- Window is scrollable, the window size is not fixed
- Once a field (QTextEdit) overloaded with text, scrollbar is displayed on the widget

<br>
<div align="center">
    <img src="pictures/screenshot_skills.png"</img> 
</div>
<br>

## Thank you all who worked on the modules used in this project!