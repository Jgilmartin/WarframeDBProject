from sqlite3 import dbapi2
import PySimpleGUI as sg
import sqlite3 as db
#------Database Initialization----------
conn = db.connect('warframeDB.sqlite')
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()

allLoadouts = c.execute('SELECT l_name FROM loadouts').fetchall()
primaryWeapons = c.execute('SELECT wp_name FROM weaponsP').fetchall()
secondaryWeapons = c.execute('SELECT wp_name FROM weaponsS').fetchall()
meleeWeapons = c.execute('SELECT wp_name FROM weaponsM').fetchall()
warframeNames = c.execute('SELECT DISTINCT wf_name FROM warframe').fetchall()
allWeapons = meleeWeapons + primaryWeapons + secondaryWeapons


# ----------- Create the 3 layouts this Window will display -----------
layout1 = [[sg.Text('Loadout Select')],*[[sg.Combo(allLoadouts, key = 'allLoadouts', enable_events=True)]], 
            [sg.Text('Primary Weapon Select')],*[[sg.Combo(primaryWeapons, key = 'primarySelect', enable_events=True)]],
            [sg.Text('Secondary Weapon Select')],*[[sg.Combo(secondaryWeapons, key = 'secondarySelect', enable_events=True)]],
            [sg.Text('Melee Weapon Select')],*[[sg.Combo(meleeWeapons, key = 'meleeSelect', enable_events=True)]],
            [sg.Text('WarframeSelect', enable_events=True)], *[[sg.Combo(warframeNames, key = 'warframeSelect', enable_events=True)]], 
            [sg.Button('UpdateLoadout')]]

layout2 = [[sg.Text('Item Editor')],
           [sg.Input(key='-IN-')],
           [sg.Input(key='-IN2-')]]

layout3 = [[sg.Text('Loadout Viewer')],
           *[[sg.R(f'Radio {i}', 1)] for i in range(8)]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key ='-COL3-')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('Exit')]]


window = sg.Window('Warframe App', layout, size =(600,400))



layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event)
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
    elif event == 'UpdateLoadout':
        query = "UPDATE loadouts SET l_primaryweapon = '"+ values['primarySelect'] +"', l_secondaryWeapon = '"+ values['secondarySelect'] +"', l_meleeWeapon = '"+ values['meleeSelect'] +"', l_warframe = '"+ values['warframeSelect'] +"' WHERE l_name = '"+values['allLoadouts']+ "';"
        print(query)
        c.execute(query)
        conn.commit()
        print('Loadout Selected: '+ values['allLoadouts'])
        print('Primary Weapon Selected: ' + values['primarySelect'])
        print('Secondary Weapon Selected: ' + values['secondarySelect'])
        print('Melee Weapon Selected: ' + values['meleeSelect'])

window.close()