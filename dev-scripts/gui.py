import PySimpleGUI as sg
import os

GUI_TITLE = 'Filter Trace File'

layout = [
    [sg.Text('Path')],
    [
        sg.InputText(key='Path'),
        sg.FileBrowse(initial_folder=os.getcwd(), file_types=[('Text Files', '*.txt')])
    ],
    [sg.Text('Keywords')],
    [sg.InputText(key='Keywords')],
    [sg.Push(), sg.Button('Generate'), sg.Push()]
]

window = sg.Window(GUI_TITLE, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Generate':
        path_ = values['Path']
        if not path_:
            print('Missing path')
        elif not os.path.isfile(path_):
            print('Invalid path')
        else:
            if not values['Keywords']:
                print('Missing keywords')
            else:
                keywords = [keyword.strip() for keyword in values['Keywords'].split(',')]
                print('Path:', path_, '\n' 'Keywords:', keywords)

window.close()
