import PySimpleGUI as sg   

class GUI:
    def __init__(self):
        pass

    def create(self):
        choices=('Java','Python','MATLAB','VHDL','PHPbyPrzemo')
        values=('Numpy','Pandas','Małe zwierzątka')
        layout = [  [sg.Text('')],
                    [sg.Text('Programming language:',size=(19, 1),justification='right'), sg.Combo(choices, size=(16, len(choices)))],
                    [sg.Text('')],
                   [sg.Text('Subject:',size=(19, 1),justification='left')],
                   [sg.InputText(),sg.Button('Search')],
                   [sg.Text('Best matches:',size=(19, 1),justification='right')],
                   [sg.Listbox(['','',''],size=(30, 8),key='-OUTPUT-')]
                   
                   ]

        window = sg.Window('Dependencies finder', layout)


        while True:
            event, values = window.read()
            if event=='Search':
                val=('Numpy','Pandas','Małe zwierzątka')
                window['-OUTPUT-'].update(val)
            elif event==sg.WIN_CLOSED:
                break
        window.close()


    def update(self):
        pass