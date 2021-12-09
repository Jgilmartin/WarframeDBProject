from sqlite3 import dbapi2
import PySimpleGUI as sg
import sqlite3 as db
#------Database Initialization----------
conn = db.connect('warframeDB.sqlite')
conn.row_factory = lambda cursor, row: None
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

layout2 = [[sg.Text('Weapon Editor ')],
           *[[sg.Combo(allWeapons, key = 'editedWeapon', enable_events=True)]],
           [sg.Button('UpdateWeapon')],
           [sg.Button('AddWeapon')],

           [sg.Text('Warframe Editor ')],
           *[[sg.Combo(warframeNames, key = 'editedWarframe', enable_events=True)]],
           [sg.Button('UpdateWarframe')],
           [sg.Button('AddWaframe')]]

testList = [['string', 'another string'], [2]]
testHeadings = ['Heading 1', 'Heading 2']

layout3 = [[sg.Text('Loadout Viewer', key = 'test1')], [sg.Table(values = testList, headings=testHeadings)]]

weaponEditLayout = [[sg.Button('Back')]]

warframeEditLayout = [[sg.Button('Back')]]


# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), 
           sg.Column(layout2, visible=False, key='-COL2-'), 
           sg.Column(layout3, visible=False, key ='-COL3-'),
           sg.Column(weaponEditLayout, visible=False, key ='-EditWeapon-'),
           sg.Column(warframeEditLayout, visible=False, key ='-EditWarframe-')],
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
        
        if event == '3':
            result = c.execute('SELECT * FROM weaponsS').fetchall()
            print(result)



    elif event == 'UpdateLoadout':
        query = "UPDATE loadouts SET l_primaryweapon = '"+ values['primarySelect'] +"', l_secondaryWeapon = '"+ values['secondarySelect'] +"', l_meleeWeapon = '"+ values['meleeSelect'] +"', l_warframe = '"+ values['warframeSelect'] +"' WHERE l_name = '"+values['allLoadouts']+ "';"
        print(query)
        c.execute(query)
        conn.commit()
        print('Loadout Selected: '+ values['allLoadouts'])
        print('Primary Weapon Selected: ' + values['primarySelect'])
        print('Secondary Weapon Selected: ' + values['secondarySelect'])
        print('Melee Weapon Selected: ' + values['meleeSelect'])

    elif event == 'editedWeapon':
        pass
    elif event == 'editedWarframe':
        pass


    elif event == 'UpdateWeapon':
        window[f'-COL2-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)

    elif event == 'UpdateWarframe':
        window[f'-COL2-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)

    elif event == 'Back':
        window[f'-EditWeapon-'].update(visible=False)
        window[f'-EditWarframe-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)

window.close()