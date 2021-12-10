from sqlite3 import dbapi2
import PySimpleGUI as sg
import sqlite3 as db

sg.theme("DarkGreen3")
#------Database Initialization----------
conn = db.connect('warframeproject.sqlite')
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
allLoadouts = c.execute('SELECT l_name FROM loadouts').fetchall()
primaryWeapons = c.execute('SELECT wp_name FROM weaponsP').fetchall()
primaryWeaponsDamageTypes = c.execute('SELECT wp_DamageTypes FROM weaponsP').fetchall()
primaryWeaponsFireRate = c.execute('SELECT wp_fireRate FROM weaponsP').fetchall()
primaryWeaponsFireTypes = c.execute('SELECT wp_fireType FROM weaponsP').fetchall()
primaryWeaponsNoise = c.execute('SELECT wp_noise FROM weaponsP').fetchall()
secondaryWeapons = c.execute('SELECT wp_name FROM weaponsS').fetchall()
secondaryWeaponsDamageTypes = c.execute('SELECT wp_DamageTypes FROM weaponsS').fetchall()
secondaryWeaponsFireRate = c.execute('SELECT wp_fireRate FROM weaponsS').fetchall()
secondaryWeaponsFireTypes = c.execute('SELECT wp_fireType FROM weaponsP').fetchall()
secondaryWeaponsNoise = c.execute('SELECT wp_noise FROM weaponsP').fetchall()
meleeWeapons = c.execute('SELECT wp_name FROM weaponsM').fetchall()
meleeWeaponsDamageTypes = c.execute('SELECT wp_DamageTypes FROM weaponsS').fetchall()
meleeWeaponsFireRate = c.execute('SELECT wp_fireRate FROM weaponsS').fetchall()
meleeWeaponsFireTypes = c.execute('SELECT wp_fireType FROM weaponsP').fetchall()
meleeWeaponsNoise = c.execute('SELECT wp_noise FROM weaponsP').fetchall()
warframeNames = c.execute('SELECT DISTINCT wf_name FROM warframe').fetchall()
warframeId = c.execute('SELECT wf_id FROM warframe').fetchall()
warframeArmor = c.execute('SELECT wf_armor FROM warframe_armor').fetchall()
warframeEnergy = c.execute('SELECT wf_energy FROM warframe_energy').fetchall()
warframeHealth = c.execute('SELECT wf_health FROM warframe_health').fetchall()
warframeRelease = c.execute('SELECT wf_release FROM warframe_release').fetchall()
warframeShields = c.execute('SELECT wf_shields FROM warframe_shields').fetchall()
warframeSpeed = c.execute('SELECT wf_speed FROM warframe_speed').fetchall()

#nameConversion = c.execute('SELECT wf_id FROM warframe').fetchall()

allWeapons = meleeWeapons + primaryWeapons + secondaryWeapons



# ----------- Create the 3 layouts this Window will display -----------
layout1 = [[sg.Text('Loadout Select')],*[[sg.Combo(allLoadouts, key = 'allLoadouts', enable_events=True)]], 
            [sg.Text('Primary Weapon Select')],*[[sg.Combo(primaryWeapons, key = 'primarySelect', enable_events=True)]],
            [sg.Text('Secondary Weapon Select')],*[[sg.Combo(secondaryWeapons, key = 'secondarySelect', enable_events=True)]],
            [sg.Text('Melee Weapon Select')],*[[sg.Combo(meleeWeapons, key = 'meleeSelect', enable_events=True)]],
            [sg.Text('WarframeSelect', enable_events=True)], *[[sg.Combo(warframeNames, key = 'warframeSelect', enable_events=True)]], 
            [sg.Button('UpdateLoadout')]]


layout2 = [[sg.Text('Primary Weapon Editor ')],
           [sg.Text('Primary Weapons ')],
           *[[sg.Combo(primaryWeapons, key = 'editedWeaponP', enable_events=True)]],
           [sg.Text("Damage type:", size = (15,1)), sg.Input(key='DamageTypeP')],
           [sg.Text("Fire rate:", size = (15,1)), sg.Input(key='fireRateP')],
           [sg.Text("Fire type:", size = (15,1)), sg.Input(key='fireTypeP')],
           [sg.Text("Noise type:", size = (15,1)), sg.Input(key='noiseP')],
           [sg.Button('UpdateWeaponStatsPrimary')]]
           
           
           #[sg.Button('UpdateWeapon')],
           #[sg.Button('AddWeapon')],

           
           #[sg.Text("Enter new value:", size = (15,1)), sg.Input(key='warframeEdit')],
           #[sg.Button('UpdateWarframe')],
           #[sg.Button('AddWaframe')]]

layout3 = [[sg.Text('Secondary Weapon Editor ')],
           
           [sg.Text('Secondary Weapons ')],
           *[[sg.Combo(secondaryWeapons, key = 'editedWeaponS', enable_events=True)]],
           [sg.Text("Damage type:", size = (15,1)), sg.Input(key='DamageTypeS')],
           [sg.Text("Fire rate:", size = (15,1)), sg.Input(key='fireRateS')],
           [sg.Text("Fire type:", size = (15,1)), sg.Input(key='fireTypeS')],
           [sg.Text("Noise type:", size = (15,1)), sg.Input(key='noiseS')],
           [sg.Button('UpdateWeaponStatsSecondary')]]
           
           #[sg.Button('UpdateWeapon')],
           #[sg.Button('AddWeapon')],

           
           #[sg.Text("Enter new value:", size = (15,1)), sg.Input(key='warframeEdit')],
           #[sg.Button('UpdateWarframe')],
           #[sg.Button('AddWaframe')]]

layout4 = [[sg.Text('Melee Weapon Editor ')],
           
           [sg.Text('Melee Weapons ')],
           *[[sg.Combo(meleeWeapons, key = 'editedWeaponM', enable_events=True)]],
           [sg.Text("Damage type:", size = (15,1)), sg.Input(key='DamageTypeM')],
           [sg.Text("Fire rate:", size = (15,1)), sg.Input(key='fireRateM')],
           [sg.Text("Fire type:", size = (15,1)), sg.Input(key='fireTypeM')],
           [sg.Text("Noise type:", size = (15,1)), sg.Input(key='noiseM')],
           [sg.Button('UpdateWeaponStatsMelee')]]
           #[sg.Button('UpdateWeapon')],
           #[sg.Button('AddWeapon')],

           
           #[sg.Text("Enter new value:", size = (15,1)), sg.Input(key='warframeEdit')],
           #[sg.Button('UpdateWarframe')],
           #[sg.Button('AddWaframe')]]

layout5 = [[sg.Text('Warframe Editor ')],
           [sg.Text('Warframes ')],
           #[sg.Text("Legend: 1=", size = (15,1))],
           *[[sg.Combo(warframeId, key = 'editedWarframe', enable_events=True)]],
           [sg.Text("Armor Value:", size = (15,1)), sg.Input(key='armor')],
           [sg.Button('UpdateWarframeArmor')],
           [sg.Text("Energy Value:", size = (15,1)), sg.Input(key='energy')],
           [sg.Button('UpdateWarframeEnergy')],
           [sg.Text("Health Value:", size = (15,1)), sg.Input(key='health')],
           [sg.Button('UpdateWarframeHealth')],
           [sg.Text("Release Date:", size = (15,1)), sg.Input(key='release')],
           [sg.Button('UpdateWarframeRelease')],
           
           [sg.Text("Shield Value:", size = (15,1)), sg.Input(key='shield')],
           [sg.Button('UpdateWarframeShields')],
           [sg.Text("Speed Value:", size = (15,1)), sg.Input(key='speed')],
           [sg.Button('UpdateWarframeSpeed')]]
           
           #[sg.Button('UpdateWeapon')],
           #[sg.Button('AddWeapon')],

           
           #[sg.Text("Enter new value:", size = (15,1)), sg.Input(key='warframeEdit')],
           #[sg.Button('UpdateWarframe')],
           #[sg.Button('AddWaframe')]]

testList = [['string', 'another string'], [2]]
testHeadings = ['Heading 1', 'Heading 2']

layout6 = [[sg.Text('Loadout Viewer', key = 'test1')], [sg.Table(values = testList, headings=testHeadings)]]

weaponEditLayout = [[sg.Button('Back')]]

warframeEditLayout = [[sg.Button('Back')]]


# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), 
           sg.Column(layout2, visible=False, key='-COL2-'),
           sg.Column(layout3, visible=False, key='-COL3-'), 
           sg.Column(layout4, visible=False, key='-COL4-'),
           sg.Column(layout5, visible=False, key='-COL5-'),
           sg.Column(layout6, visible=False, key ='-COL6-'),
           sg.Column(weaponEditLayout, visible=False, key ='-EditWeapon-'),
           sg.Column(warframeEditLayout, visible=False, key ='-EditWarframe-')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'),sg.Button('Exit')]]


window = sg.Window('Warframe App', layout, size =(1000,800))



layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event)
    if event in (None, 'Exit'):
        break
    if event == 'Cycle Layout':
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 6 else 1
        window[f'-COL{layout}-'].update(visible=True)

    elif event in '123456':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
        
        if event == '6':
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
        sg.popup('Loadout', "Primary weapon: " + values['primarySelect'] +"\nSecondary Weapon: "+ values['secondarySelect'] +"\nMelee Weapon: "+ values['meleeSelect'] +"\nWarframe: "+ values['warframeSelect'] +"\nLoadout Number: "+values['allLoadouts'])

    elif event == 'UpdateWeaponStatsPrimary':
        query = "UPDATE weaponsP SET wp_name = '"+ values['editedWeaponP'] +"',wp_DamageTypes = '"+ values['DamageTypeP'] +"', wp_fireRate = '"+ values['fireRateP'] +"', wp_fireType = '"+ values['fireTypeP'] +"', wp_noise = '"+ values['noiseP'] +"' WHERE wp_name = '"+values['editedWeaponP']+ "';" 
        print(query)
        c.execute(query)
        conn.commit()
        sg.popup('Primary', "Primary weapon: " + values['editedWeaponP'] +"\nDamageType: "+ values['DamageTypeP'] +"\nFireRate: "+ values['fireRateP'] + "\nfireType: "+ values['fireTypeP'] + "\nnoise: "+ values['noiseP'])
    elif event == 'UpdateWeaponStatsSecondary':
        query = "UPDATE weaponsS SET wp_name = '"+ values['editedWeaponS'] +"',wp_DamageTypes = '"+ values['DamageTypeS'] +"', wp_fireRate = '"+ values['fireRateS'] +"', wp_fireType = '"+ values['fireTypeS'] +"', wp_noise = '"+ values['noiseS'] +"' WHERE wp_name = '"+values['editedWeaponS']+ "';" 
        print(query)
        c.execute(query)
        conn.commit()
        sg.popup('Secondary', "Secondary weapon: " + values['editedWeaponS'] +"\nDamageType: "+ values['DamageTypeS'] +"\nFireRate: "+ values['fireRateS'] + "\nfireType: "+ values['fireTypeS'] + "\nnoise: "+ values['noiseS'])
    elif event == 'UpdateWeaponStatsMelee':
        query = "UPDATE weaponsM SET wp_name = '"+ values['editedWeaponM'] +"',wp_DamageTypes = '"+ values['DamageTypeM'] +"', wp_fireRate = '"+ values['fireRateM'] +"', wp_fireType = '"+ values['fireTypeM'] +"', wp_noise = '"+ values['noiseM'] +"' WHERE wp_name = '"+values['editedWeaponM']+ "';" 
        print(query)
        c.execute(query)
        conn.commit()
        sg.popup('Melee', "Melee weapon: " + values['editedWeaponM'] +"\nDamageType: "+ values['DamageTypeM'] +"\nFireRate: "+ values['fireRateM'] + "\nfireType: "+ values['fireTypeM'] + "\nnoise: "+ values['noiseM'])        
    elif event == 'UpdateWarframeArmor':
        query = "UPDATE warframe_armor SET wf_id = '"+ values['editedWarframe'] +"',wf_armor = '"+ values['armor'] + "' WHERE wf_id = '"+values['editedWarframe']+ "';"
        print(query)
        c.execute(query)
        conn.commit()
        sg.popup('Warframe', "Armor: "+ values['armor'])        


    elif event == 'UpdateWeaponStatsPrimary':
        window[f'-COL2-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)
    elif event == 'UpdateWeaponStatsSecondary':
        window[f'-COL3-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)
    elif event == 'UpdateWeaponStatsMelee':
        window[f'-COL4-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)    

    elif event == 'UpdateWarframeArmor':
        window[f'-COL5-'].update(visible=False)
        window[f'-EditWarframe-'].update(visible=True)

    elif event == 'Back':
        window[f'-EditWeapon-'].update(visible=False)
        window[f'-EditWarframe-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)

window.close()
