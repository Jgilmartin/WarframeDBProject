from sqlite3 import dbapi2
import PySimpleGUI as sg
import sqlite3 as db
#------Database Initialization----------
conn = db.connect('warframeDB.sqlite')
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()

meleeWeapons = c.execute('SELECT wp_name FROM weaponsM').fetchall()


# ----------- Create the 3 layouts this Window will display -----------
layout1 = [[sg.Text('Item Selector')],
           *[[sg.Combo(meleeWeapons),]]]

layout2 = [[sg.Text('Item Editor')],
           [sg.Input(key='-IN-')],
           [sg.Input(key='-IN2-')]]

layout3 = [[sg.Text('Loadout Viewer')],
           *[[sg.R(f'Radio {i}', 1)] for i in range(8)]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key ='-COL3-')],
          [sg.Button('Cycle Layout'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('Exit')]]


window = sg.Window('Swapping the contents of a window', layout)



layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Cycle Layout':
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 3 else 1
        window[f'-COL{layout}-'].update(visible=True)
    elif event in '123':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
window.close()