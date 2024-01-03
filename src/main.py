import PySimpleGUI as sg
import os
import mbox
from file import FileHandler

file = FileHandler()

def show_error(title, text):
    """ Shows an error message box based on the provided parameters.

    Parameters
    ----------
    title: str
        The title shown on message box.

    text: str
        The text shown on message box.

    Returns
    -------
    None
    """
    mbox.show(title=title, text=text, button='OK', icon='ICONERROR')

def get_keywords(text, separator='', case=False):
    """ Retrieves the list of keywords to search.

    Parameters
    ----------
    text: str
        The single keyword or multiple keywords to search.
            ex: ``keyword`` or ``keyword1, keyword2``

    separator: str
        Optional parameter, the separator to differentiate multiple keywords.

    case: boolean
        Optional parameter, the case sensitivity of keywords to search.

    Returns
    -------
    list
        The list of keywords to search.
    """
    keywords = []
    if not separator:
        keywords.append(text.strip().lower() if not case else text.strip())
    elif separator in text:
        for keyword in [item for item in text.split(separator) if item]:
            keywords.append(keyword.strip().lower() if not case else keyword.strip())
    return keywords

def read_lines(path):
    """ Reads the contents of the file.

    Parameters
    ----------
    path: str
        The path of the file to read.
            ex: ``'C:\\Users\\example\\file.txt'``

    Returns
    -------
    str
        The file contents.
    """
    file.path = path
    return file.read_lines()

def get_write_file(path):
    """ Retrieves the name of the write file.

    Parameters
    ----------
    path: str
        The path of the read file.
            ex: ``'C:\\Users\\example\\file.txt'``

    Returns
    -------
    str
        The write file path.
            ex: ``'C:\\Users\\example\\file (filtered).txt'``
    """
    extension = os.path.splitext(path)[1]
    return path.replace(extension, ' (filtered).txt')

def write_lines(title, path, lines):
    """ Writes the provided lines to the file.

    Parameters
    ----------
    title: str
        The title shown on message box.

    path: str
        The path of the file.
            ex: ``'C:\\Users\\example\\file.txt'``

    lines: str
        The lines to write.

    Returns
    -------
    None
    """
    if lines:
        file.path = get_write_file(path)
        file.write_lines(lines)
        mbox.show(title=title, text='File Generated', button='OK', icon='ICONINFORMATION')
    else:
        show_error(title, 'No keywords found')

def search_lines(title, path, keywords, case):
    """ Searches the file based on the provided path and keywords.

    Parameters
    ----------
    title: str
        The title shown on message box.

    path: str
        The path of the file.
            ex: ``'C:\\Users\\example\\file.txt'``

    keywords: list
        The list of keywords to search.
            ex: ``['keyword']`` or ``['keyword1', 'keyword2']``

    case: boolean
        The case sensitivity of keywords to search.

    Returns
    -------
    None
    """
    lines = ''
    for number, line in enumerate(read_lines(path), 1):
        for keyword in keywords:
            keyword = keyword.lower() if not case else keyword
            if keyword in (line.lower() if not case else line):
                lines += f'{number}: {line}'
                break
    write_lines(title, path, lines)
    
def define_layout(path='', keywords=''):
    """ Defines the layout of the GUI.

    Parameters
    ----------
    path: str
        Optional parameter, used for caching user input.

    keywords: str or list
        Optional parameter, used for caching user input.

    Returns
    -------
    list
        The GUI layout.
    """
    layout = [
        [sg.Text('Path')],
        [
            sg.InputText(key='Path', default_text=path, tooltip='The path of the file to search'),
            sg.FileBrowse(initial_folder=os.getcwd())
        ],
        [sg.Text('Keywords')],
        [sg.InputText(key='Keywords', default_text=keywords, tooltip='Single or multiple keywords')],
        [sg.Text('Separator')],
        [sg.InputText(key='Separator', tooltip='Required if using multiple keywords')],
        [sg.Checkbox('Case Sensitive', key='Case Sensitive', tooltip='Case sensitivity of keywords')],
        [sg.Push(), sg.Button('Generate'), sg.Push(), sg.Text('v1.2.0')]
    ]
    return layout

def create_window(title, layout, icon):
    """ Creates the GUI window based on the provided parameters.

    Parameters
    ----------
    title: str
        The GUI title.

    layout: list
        The GUI layout.

    icon: str
        The GUI icon file path.

    Returns
    -------
    PySimpleGUI.PySimpleGUI.Window
        The GUI window object.
    """
    return sg.Window(title, layout, icon=icon)

def start_event(title, window):
    """ Starts the event loop of the GUI window object.

    Parameters
    ----------
    title: str
        The GUI title.

    window: PySimpleGUI.PySimpleGUI.Window
        The GUI window object.

    Returns
    -------
    None
    """
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Generate':
            path = values['Path']
            if path and os.path.isfile(path):
                text = values['Keywords']
                if text:
                    separator = values['Separator']
                    case = values['Case Sensitive']
                    keywords = get_keywords(text, separator, case)
                    if keywords:
                        search_lines(title, path, keywords, case)
                    else:
                        show_error(title, 'Separator not found')
                else:
                    show_error(title, 'Missing keywords')
            else:
                show_error(title, 'Missing or invalid path')
    window.close()

def main():
    gui_title = 'Filter Trace File'
    gui_layout = define_layout()
    gui_icon = 'filtering.ico'
    gui_window = create_window(gui_title, gui_layout, gui_icon)
    start_event(gui_title, gui_window)

if __name__ == '__main__':
    main()
