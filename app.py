from ctypes import sizeof
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

loadoutNames = c.execute('SELECT l_name FROM loadouts').fetchall()
loadoutPrimaries = c.execute('SELECT l_primaryWeapon FROM loadouts').fetchall()
loadoutSecondaries = c.execute('SELECT l_secondaryWeapon FROM loadouts').fetchall()
loadoutMelee = c.execute('SELECT l_meleeWeapon FROM loadouts').fetchall()
loadoutWarframe = c.execute('SELECT l_warframe FROM loadouts').fetchall()
result = c.execute('SELECT * FROM weaponsS').fetchall()


filterSelections = []
for i in range(0,13):
    filterSelections.append(False)
print (filterSelections)

def resetFilterView():
    print('reset')
    c.execute('DROP TABLE filterView')
    c.execute(""" 
    CREATE TABLE filterView AS 
    SELECT * FROM weaponsM
    UNION 
    SELECT * FROM weaponsP
    UNION 
    SELECT * FROM weaponsS;
    """)
    print('reached')
    c.execute("INSERT INTO filterView(wp_id, wp_name, wp_class, wp_DamageTypes, wp_fireRate, wp_fireType, wp_noise) VALUES ('99', '', '', '', '', '', '')")
    conn.commit()

#, , loadoutSecondaries, loadoutMelee, loadoutWarframe]
loadoutViewHeadings = 'Loadout Name       Primary Weapon      Secondary Weapon    Melee Weapon    Warframe'

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
           [sg.Text('Primary Weapons ')],
           *[[sg.Combo(primaryWeapons, key = 'editedWeaponP', enable_events=True)]],
           [sg.Text("Damage type:", size = (15,1)), sg.Input(key='DamageTypeP')],
           [sg.Text("Fire rate:", size = (15,1)), sg.Input(key='fireRateP')],
           [sg.Text("Fire type:", size = (15,1)), sg.Input(key='fireTypeP')],
           [sg.Text("Noise type:", size = (15,1)), sg.Input(key='noiseP')],
           [sg.Button('UpdateWeaponStatsPrimary')],
           [sg.Text('Secondary Weapons ')],
           *[[sg.Combo(secondaryWeapons, key = 'editedWeaponS', enable_events=True)]],
           [sg.Text("Damage type:", size = (15,1)), sg.Input(key='DamageTypeS')],
           [sg.Text("Fire rate:", size = (15,1)), sg.Input(key='fireRateS')],
           [sg.Text("Fire type:", size = (15,1)), sg.Input(key='fireTypeS')],
           [sg.Text("Noise type:", size = (15,1)), sg.Input(key='noiseS')],
           [sg.Button('UpdateWeaponStatsSecondary')],
           [sg.Text('Melee Weapons ')],
           *[[sg.Combo(meleeWeapons, key = 'editedWeaponM', enable_events=True)]],
           [sg.Text("Damage type:", size = (15,1)), sg.Input(key='DamageTypeM')],
           [sg.Text("Fire rate:", size = (15,1)), sg.Input(key='fireRateM')],
           [sg.Text("Fire type:", size = (15,1)), sg.Input(key='fireTypeM')],
           [sg.Text("Noise type:", size = (15,1)), sg.Input(key='noiseM')],
           [sg.Button('UpdateWeaponStatsMelee')],
           #[sg.Button('UpdateWeapon')],
           #[sg.Button('AddWeapon')],

           [sg.Text('Warframe Editor ')],
           *[[sg.Combo(warframeNames, key = 'editedWarframe', enable_events=True)]]]
           #[sg.Text("Enter new value:", size = (15,1)), sg.Input(key='warframeEdit')],
           #[sg.Button('UpdateWarframe')],
           #[sg.Button('AddWaframe')]]



layout6 = [[sg.Text('Loadout Viewer', key = 'test1')], 
            [sg.Text(loadoutViewHeadings)],
            [sg.Listbox(loadoutNames, size= (15,30) ,no_scrollbar=True), sg.Listbox(loadoutPrimaries, size= (15,30), no_scrollbar=True, key = 'l_primaries'), 
            sg.Listbox(loadoutSecondaries, size= (15,30), no_scrollbar=True, key = 'l_secondaries'), sg.Listbox(loadoutMelee, size= (15,30), no_scrollbar=True, key = 'l_melee'), sg.Listbox(loadoutWarframe, size= (15,30), no_scrollbar=True, key = 'l_warframes')],
            ]

#--------------CREATE FILTERS-----------------
filNames = c.execute('SELECT wp_name from filterView').fetchall()
filClass = c.execute('SELECT wp_class from filterView').fetchall()
filDamageTypes = c.execute('SELECT wp_DamageTypes from filterView').fetchall()
filFireRate = c.execute('SELECT wp_FireRate from filterView').fetchall()
filFireType = c.execute('SELECT wp_FireType from filterView').fetchall()
filNoise = c.execute('SELECT wp_noise from filterView').fetchall()
filterValues =['f_Primary', 'f_Secondary', 'f_Melee', 'f_Electric', 'f_Heat', 'f_Magnetic', 'f_Radiation', 'f_Slash', 'f_Puncture', 'f_Impact', 'f_Rifle', 'f_Shotgun', 'f_Sniper']



ItemViewAndFilters =[[sg.Text('Item View and Filters')], 
                    [sg.Text('Sort By'), sg.Checkbox('Name', key = 'f_Name'), sg.Checkbox('Damage Type', key = 'f_DamageType'), sg.Checkbox('Fire Rate', key = 'f_FireRate')],
                    [sg.Text('Filter By: '), sg.Checkbox('Primary', key = 'f_Primary'), sg.Checkbox('Secondary', key = 'f_Secondary'), sg.Checkbox('Melee', key = 'f_Melee')],
                    [sg.Text('Damge Type '), sg.Checkbox('electric', key = 'f_Electric'), sg.Checkbox('heat', key = 'f_Heat'), sg.Checkbox('magnetic', key = 'f_Magnetic'), sg.Checkbox('radiation', key = 'f_Radiation'), sg.Checkbox('slash', key = 'f_Slash'), sg.Checkbox('puncture', key = 'f_Puncture'), sg.Checkbox('impact', key = 'f_Impact')],
                    [sg.Text('Weapon Class '), sg.Checkbox('rifle', key = 'f_Rifle'), sg.Checkbox('shotgun', key = 'f_Shotgun'), sg.Checkbox('sniper', key = 'f_Sniper')],
                    [sg.Button('Update List'), sg.Text('Items:     '), sg.Text('Weapon Class:    '), sg.Text('DamageType:    '), sg.Text('Fire Rate:  ')], 
                    [sg.Text('       '), sg.Listbox(filNames, key ='filNames', enable_events=True, size= (15,25), no_scrollbar=True ),
                     sg.Listbox(filClass, key ='filClass', enable_events=True, size= (15,25), no_scrollbar=True ),
                     sg.Listbox(filDamageTypes, key ='filDamageTypes', enable_events=True, size= (15,25), no_scrollbar=True ),
                     sg.Listbox(filFireRate, key ='filFireRate', enable_events=True, size= (15,25), no_scrollbar=True )]]

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
           sg.Column(warframeEditLayout, visible=False, key ='-EditWarframe-'),
           sg.Column(ItemViewAndFilters, visible=False, key = '-COL7-')],
          [sg.Button('1', size = (4, 1)), sg.Button('2', size = (4, 1)), sg.Button('3', size = (4, 1)), sg.Button('4', size = (4, 1)), sg.Button('5', size = (4, 1)), sg.Button('6', size = (4, 1)),sg.Button('7', size = (4, 1)),sg.Button('Exit')]]


window = sg.Window('Warframe App', layout, size =(800,700), resizable=True)



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

    elif event in '1234567':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
        
        if event == '6':
            newloadoutNames = c.execute('SELECT l_name FROM loadouts').fetchall()
            newloadoutPrimaries = c.execute('SELECT l_primaryWeapon FROM loadouts').fetchall()
            newloadoutSecondaries = c.execute('SELECT l_secondaryWeapon FROM loadouts').fetchall()
            newloadoutMelee = c.execute('SELECT l_meleeWeapon FROM loadouts').fetchall()
            newloadoutWarframe = c.execute('SELECT l_warframe FROM loadouts').fetchall()
            result = c.execute('SELECT * FROM weaponsS').fetchall()
            window['l_primaries'].Update(values=newloadoutPrimaries)
            window['l_secondaries'].Update(values=newloadoutSecondaries)
            window['l_melee'].Update(values=newloadoutMelee)
            window['l_warframes'].Update(values=newloadoutWarframe)

        if event == '7':
            resetFilterView()
            


    
    elif event == 'Update List':
        reset = True
        for i in range(0,13):
            if filterSelections[i] == True:
                reset = False
        if reset == True:
            resetFilterView()

        deleteQuery = "SELECT wp_name FROM filterView WHERE wp_id == 99"
        for i in range(0,13):
            print(values[(filterValues[i])])
            print(i)
            if values[(filterValues[i])] == True:
                filterSelections[i] = True
            elif values[(filterValues[i])] == False:
                filterSelections[i] = False
        
        if filterSelections[0] == True and reset ==False: #Primary select
            deleteQuery += " OR wp_class == 'secondary' OR wp_class == 'melee' "
        elif filterSelections[1] == True and reset ==False: #Secondary Select
                deleteQuery += " OR wp_class != 'secondary' "  
        elif filterSelections[2] == True and reset ==False: #Melee Select
                deleteQuery += " OR wp_class != 'melee' " 
        if filterSelections[3] == True and reset ==False: #Electric Select
                deleteQuery += " OR wp_DamageTypes NOT LIKE  '%electricity%' " 
        elif filterSelections[4] == True and reset ==False: #Heat Select
                deleteQuery += " OR wp_DamageTypes NOT LIKE '%heat%' " 
        elif filterSelections[5] == True and reset ==False: #Magnetic Select
                deleteQuery += " OR wp_DamageTypes NOT LIKE '%magnetic%' " 
        elif filterSelections[6] == True and reset == False: #Radiation Select
            deleteQuery += " OR wp_DamageTypes NOT LIKE '%radiation%' "
        elif filterSelections[7] == True and reset == False: #Slash Select
            deleteQuery += " OR wp_DamageTypes NOT LIKE '%slash%' "
        elif filterSelections[8] == True and reset == False: #Puncture Select
            deleteQuery += " OR wp_DamageTypes NOT LIKE '%puncture%' "
        elif filterSelections[9] == True and reset == False: #Impact Select
            deleteQuery += " OR wp_DamageTypes NOT LIKE '%impact%' "
        elif filterSelections[10] == True and reset == False: #Rifle Select
            deleteQuery += " OR wp_class NOT LIKE '%rifle%' "
        elif filterSelections[11] == True and reset == False: #Shotgun Select
            deleteQuery += " OR wp_class NOT LIKE '%shotgun%' "
        elif filterSelections[12] == True and reset == False: #Sniper Select
            deleteQuery += " OR wp_class NOT LIKE '%sniper%' "

        if reset == False:
            print(deleteQuery)
            print("DELETE FROM filterView WHERE wp_name IN (" + deleteQuery + ")")
            finalQuery = "DELETE FROM filterView WHERE wp_name IN (" + deleteQuery + ");"
            c.execute(finalQuery)  
            conn.commit()


        newfilNames = c.execute('SELECT wp_name from filterView').fetchall()
        newfilClass = c.execute('SELECT wp_class from filterView').fetchall()
        newfilDamageTypes = c.execute('SELECT wp_DamageTypes from filterView').fetchall()
        newfilFireRate = c.execute('SELECT wp_FireRate from filterView').fetchall()
        newfilFireType = c.execute('SELECT wp_FireType from filterView').fetchall()
        newfilNoise = c.execute('SELECT wp_noise from filterView').fetchall()

        window['filNames'].Update(values=newfilNames)
        window['filClass'].Update(values=newfilClass)
        window['filDamageTypes'].Update(values=newfilDamageTypes)
        window['filFireRate'].Update(values=newfilFireRate)
        


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
    elif event == 'editedWarframe':
        pass

    elif event == 'UpdateWeaponStatsPrimary':
        window[f'-COL2-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)
    elif event == 'UpdateWeaponStatsSecondary':
        window[f'-COL3-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)
    elif event == 'UpdateWeaponStatsMelee':
        window[f'-COL4-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)    

    elif event == 'UpdateWarframe':
        window[f'-COL5-'].update(visible=False)
        window[f'-EditWeapon-'].update(visible=True)

    elif event == 'Back':
        window[f'-EditWeapon-'].update(visible=False)
        window[f'-EditWarframe-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)

    elif event == 'f_Name':
        filteredResult.sort()
        window['filteredResult'].Update(filteredResult)

window.close()
query = "UPDATE weaponsS SET wp_name = '"+ values['editedWeaponS'] +"',wp_DamageTypes = '"+ values['DamageTypeS'] +"', wp_fireRate = '"+ values['fireRateS'] +"', wp_fireType = '"+ values['fireTypeS'] +"', wp_noise = '"+ values['noiseS'] +"' WHERE wp_name = '"+values['editedWeaponS']+ "';"
query = "UPDATE weaponsM SET wp_name = '"+ values['editedWeaponM'] +"',wp_DamageTypes = '"+ values['DamageTypeM'] +"', wp_fireRate = '"+ values['fireRateM'] +"', wp_fireType = '"+ values['fireTypeM'] +"', wp_noise = '"+ values['noiseM'] +"' WHERE wp_name = '"+values['editedWeaponM']+ "';" 