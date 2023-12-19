import PySimpleGUI as sg
import os

def create(title='Filter Trace File'):
    layout = [
        [sg.Text('Path')],
        [
            sg.InputText(key='Path', tooltip='The path of the file to search'),
            sg.FileBrowse(initial_folder=os.getcwd(), file_types=[('Text Files', '*.txt')])
        ],
        [sg.Text('Keywords')],
        [sg.InputText(key='Keywords', tooltip='Single keyword or multiple separated by commas')],
        [sg.Push(), sg.Button('Generate'), sg.Push()]
    ]

    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Generate':
            if values['Path'] and os.path.isfile(values['Path']):
                path = values['Path']
                if values['Keywords']:
                    keywords = [keyword.strip() for keyword in values['Keywords'].split(',')]
                    print('Path:', path, '\n' 'Keywords:', keywords)
                    return (path, keywords)
                else:
                    print('Missing keywords')
            else:
                print('Missing or invalid path')
    window.close()

if __name__ == '__main__':
    create()
