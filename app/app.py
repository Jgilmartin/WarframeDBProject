from sqlite3 import dbapi2
import PySimpleGUI as sg
import sqlite3 as db

sg.theme("DarkAmber")
#------Database Initialization----------
conn = db.connect('warframeproject.sqlite')
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
allLoadouts = c.execute('SELECT l_name FROM loadouts').fetchall()
primaryWeapons = c.execute('SELECT wp_name FROM weaponsP').fetchall()
secondaryWeapons = c.execute('SELECT wp_name FROM weaponsS').fetchall()
meleeWeapons = c.execute('SELECT wp_name FROM weaponsM').fetchall()
warframeNames = c.execute('SELECT DISTINCT wf_name FROM warframe').fetchall()
allWeapons = meleeWeapons + primaryWeapons + secondaryWeapons

allItems = allWeapons + warframeNames
filteredResult = allItems


# ----------- Create various layouts this Window will display -----------
layout1 = [[sg.Text('Loadout Select')],*[[sg.Combo(allLoadouts, key = 'allLoadouts', enable_events=True)]], 
            [sg.Text('Primary Weapon Select')],*[[sg.Combo(primaryWeapons, key = 'primarySelect', enable_events=True)]],
            [sg.Text('Secondary Weapon Select')],*[[sg.Combo(secondaryWeapons, key = 'secondarySelect', enable_events=True)]],
            [sg.Text('Melee Weapon Select')],*[[sg.Combo(meleeWeapons, key = 'meleeSelect', enable_events=True)]],
            [sg.Text('WarframeSelect', enable_events=True)], *[[sg.Combo(warframeNames, key = 'warframeSelect', enable_events=True)]], 
            [sg.Button('UpdateLoadout')]]


layout2 = [[sg.Text('Weapon Editor ')],
           *[[sg.Combo(allWeapons, key = 'editedWeapon', enable_events=True)]],
           [sg.Text("Enter new value:", size = (15,1)), sg.Input(key='weaponEdit')],
           [sg.Button('UpdateWeapon')],
           [sg.Button('AddWeapon')],

           [sg.Text('Warframe Editor ')],
           *[[sg.Combo(warframeNames, key = 'editedWarframe', enable_events=True)]],
           [sg.Text("Enter new value:", size = (15,1)), sg.Input(key='warframeEdit')],
           [sg.Button('UpdateWarframe')],
           [sg.Button('AddWaframe')]]

testList = [['string', 'another string'], [2]]
testHeadings = ['Heading 1', 'Heading 2']

layout3 = [[sg.Text('Loadout Viewer', key = 'test1')], [sg.Table(values = testList, headings=testHeadings)]]


weaponEditLayout = [[sg.Button('Back')]]


warframeEditLayout = [[sg.Button('Back')]]


ItemViewAndFilters =[[sg.Text('Item View and Filters')], 
                    [sg.Text('Sort By'), sg.Button('Name', key = 'f_Name'), sg.Button('Damage Type', key = 'f_DamageType'), sg.Button('Fire Rate', key = 'f_FireRate'), sg.Button('Noise', key = 'f_Noise')],
                    [sg.Text('Filter By: '), sg.Checkbox('Warfames', key = 'f_Warframes'), sg.Checkbox('Weapons', key = 'f_Weapons'), sg.Checkbox('Primary', key = 'f_Primary'), sg.Checkbox('Secondary', key = 'f_Secondary'), sg.Checkbox('Melee', key = 'f_Melee')],
                    [sg.Text('Damge Type '), sg.Checkbox('electric', key = 'f_Electric'), sg.Checkbox('heat', key = 'f_Heat'), sg.Checkbox('magnetic', key = 'f_Magnetic'), sg.Checkbox('radiation', key = 'f_Radiation'), sg.Checkbox('slash', key = 'f_Slash'), sg.Checkbox('puncture', key = 'f_Puncture'), sg.Checkbox('impact', key = 'f_Impact')],
                    [sg.Text('Weapon Class '), sg.Checkbox('rifle', key = 'f_Rifle'), sg.Checkbox('shotgun', key = 'f_Shotgun'), sg.Checkbox('sniper', key = 'f_Sniper')],
                    [sg.Button('Update List')],
                    [sg.Text('Items: '), sg.Listbox(filteredResult, key ='filteredResult', enable_events=True, size= (60,10))]]



# ----------- Create full layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), 
           sg.Column(layout2, visible=False, key='-COL2-'), 
           sg.Column(layout3, visible=False, key ='-COL3-'),
           sg.Column(weaponEditLayout, visible=False, key ='-EditWeapon-'),
           sg.Column(warframeEditLayout, visible=False, key ='-EditWarframe-'),
           sg.Column(ItemViewAndFilters, visible=False, key = '-COL4-')],
          [sg.Button('1', size = (4, 1)), sg.Button('2', size = (4, 1)), sg.Button('3', size = (4, 1)), sg.Button('4', size = (4, 1)), sg.Button('Exit')]]



window = sg.Window('Warframe App', layout, size =(800,600))

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

    elif event in '1234':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
        
        if event == '3':
            result = c.execute('SELECT l_name FROM loadouts').fetchall()
            names = c.execute('SELECT l_name FROM loadouts').fetchall()
            l_primaryweapons = c.execute('SELECT l_primaryWeapon FROM loadouts').fetchall()
            print(result)
            print (l_primaryweapons)
    

    elif event == 'UpdateLoadout':
        verified = 1
        if (values['primarySelect'] == '' or values['secondarySelect'] == '' or values['meleeSelect'] == '' or values['warframeSelect'] == '' or values['allLoadouts'] == ''): 
            sg.popup('ERROR: Missing Selection')
            verified = 0
        if verified == 1:    
            query = "UPDATE loadouts SET l_primaryweapon = '"+ values['primarySelect'] +"', l_secondaryWeapon = '"+ values['secondarySelect'] +"', l_meleeWeapon = '"+ values['meleeSelect'] +"', l_warframe = '"+ values['warframeSelect'] +"' WHERE l_name = '"+values['allLoadouts']+ "';"
            print(query)
            c.execute(query)
            conn.commit()
            print('Loadout Selected: '+ values['allLoadouts'])
            print('Primary Weapon Selected: ' + values['primarySelect'])
            print('Secondary Weapon Selected: ' + values['secondarySelect'])
            print('Melee Weapon Selected: ' + values['meleeSelect'])
            sg.popup('Loadout', "Primary weapon: " + values['primarySelect'] +"\nSecondary Weapon: "+ values['secondarySelect'] +"\nMelee Weapon: "+ values['meleeSelect'] +"\nWarframe: "+ values['warframeSelect'] +"\nLoadout Number: "+values['allLoadouts'])


    # Don't think these are necessary, the update button triggers the event, not the list selection
    elif event == 'editedWeapon':
        pass
    elif event == 'editedWarframe':
        pass



    elif event == 'UpdateWeapon':
        verified = 1
        if (values['editedWeapon'] == ''):
            verified = 0
            sg.popup('ERROR: Please Select a Weapon Before Editing.')
        if verified == 1:
            window[f'-COL2-'].update(visible=False)
            window[f'-EditWeapon-'].update(visible=True)

    elif event == 'UpdateWarframe':
        verified = 1
        if (values['editedWarframe'] == ''):
            verified = 0
            sg.popup('ERROR: Please Select a Warframe Before Editing.')
        if verified == 1:
            window[f'-COL2-'].update(visible=False)
            window[f'-EditWeapon-'].update(visible=True)

    elif event == 'Back':
        window[f'-EditWeapon-'].update(visible=False)
        window[f'-EditWarframe-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)
        
# --------------------FILTERS-------------------- 
    elif event == 'f_Name':
        filteredResult.sort()
        window['filteredResult'].Update(filteredResult)
        
    elif event == 'Update List':
        pass
window.close()
