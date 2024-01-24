import PySimpleGUI as sg
import mbox
from filemanager import FileManager

VERSION = 'v1.2.1'
GUI_TITLE = 'Filter Trace File'
GUI_ICON = 'filtering.ico'

file_manager = FileManager()

def define_layout():
    """ Defines the layout of the GUI.

    Returns
    -------
    list
        The GUI layout.
    """
    layout = [
        [sg.Text('Path')],
        [
            sg.InputText(key='Path', tooltip='The path of the file to search'),
            sg.FileBrowse(initial_folder=file_manager.get_current_directory())
        ],
        [sg.Text('Keywords')],
        [sg.InputText(key='Keywords', tooltip='Single or multiple keywords')],
        [sg.Text('Separator')],
        [sg.InputText(key='Separator', tooltip='Required if using multiple keywords')],
        [sg.Checkbox('Case Sensitive', key='Case Sensitive', tooltip='Case sensitivity of keywords')],
        [sg.Push(), sg.Button('Generate', bind_return_key=True), sg.Push(), sg.Text(VERSION)]
    ]
    return layout

def create_window(layout):
    """ Creates the GUI window based on the GUI layout.

    Parameters
    ----------
    layout: list
        The GUI layout.

    Returns
    -------
    PySimpleGUI.PySimpleGUI.Window
        The GUI window object.
    """
    return sg.Window(title=GUI_TITLE, layout=layout, icon=GUI_ICON)

def start_event(window):
    """ Starts the event loop for the GUI window object.

    Parameters
    ----------
    window: PySimpleGUI.PySimpleGUI.Window
        The GUI window object.
    """
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Generate':
            path = values['Path']
            if not path:
                show_error('Missing path')
            elif not file_manager.is_file(path):
                show_error('Invalid path')
            else:
                if not values['Keywords']:
                    show_error('Missing keywords')
                else:
                    separator = values['Separator']
                    case = values['Case Sensitive']
                    keywords = get_keywords(values['Keywords'], separator, case)
                    if not keywords:
                        show_error('Missing separator in keywords')
                    else:
                        data = get_lines(path)                            
                        if data:
                            lines = search_lines(data, keywords, case)
                            if not lines:
                                show_error('No keywords found')
                            else:
                                write_new_lines(path, lines)
                                show_info('File Generated')
                        elif isinstance(data, list):
                            show_error('No file data found')
    window.close()

def get_keywords(text, separator='', case=False):
    """ Retrieves the list of keywords to search.

    Parameters
    ----------
    text: str
        The single keyword or multiple keywords to search.
            ex: ``keyword`` or ``keyword1, keyword2``

    separator: str
        Optional parameter, the separator to differentiate multiple keywords.

    case: bool
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

def get_lines(path):
    """ Retrieves the lines of the file (if any).

    Parameters
    ----------
    path: str
        The path of the file to read.
            ex: ``'C:\\Users\\johndoe\\Documents\\trace.txt'``

    Returns
    -------
    str
        The lines of the file.
    """
    try:
        return file_manager.read_all_lines(path)
    except Exception as e:
        show_error(str(e))

def search_lines(data, keywords, case):
    """ Searches the file data based on the provided keywords and case.

    Parameters
    ----------
    data: list
        The lines of the file.

    keywords: list
        The list of keywords to search.
            ex: ``['keyword']`` or ``['keyword1', 'keyword2']``

    case: bool
        The case sensitivity of keywords to search.

    Returns
    -------
        list
            The new lines to write.
    """
    lines = []
    for number, line in enumerate(data, start=1):
        for keyword in keywords:
            keyword = keyword.lower() if not case else keyword
            if keyword in (line.lower() if not case else line):
                lines.append(f'{number}: {line}')
                break
    return lines

def get_write_file(path):
    """ Retrieves the name of the write file.

    Parameters
    ----------
    path: str
        The path of the read file.
            ex: ``'C:\\Users\\johndoe\\Documents\\trace.txt'``

    Returns
    -------
    str
        The write file path.
            ex: ``'C:\\Users\\johndoe\\Documents\\trace (filtered).txt'``
    """
    extension = file_manager.get_file_extension(path)
    if not extension or extension == '.':
        return path.rstrip('.') + ' (filtered).txt'
    else:
        return path.replace(extension, ' (filtered).txt')

def write_new_lines(path, lines):
    """ Writes the provided lines to the file.

    Parameters
    ----------
    path: str
        The path of the file.
            ex: ``'C:\\Users\\johndoe\\Documents\\trace.txt'``

    lines: list
        The lines to write.
    """
    try:
        file_manager.write_lines(lines, get_write_file(path))
    except Exception as e:
        show_error(str(e))

def show_error(text):
    """ Shows an error message box based on the provided text.

    Parameters
    ----------
    text: str
        The text shown on message box.
    """
    mbox.show(title=GUI_TITLE, text=text, icon='ICONERROR')

def show_info(text):
    """ Shows an informative message box based on the provided text.

    Parameters
    ----------
    text: str
        The text shown on message box.
    """
    mbox.show(title=GUI_TITLE, text=text)

def main():
    gui_layout = define_layout()
    gui_window = create_window(gui_layout)
    start_event(gui_window)

if __name__ == '__main__':
    main()
