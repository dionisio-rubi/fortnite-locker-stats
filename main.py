import psycopg as pg
import requests

from Combination import Combination
from CombinationView import CombinationView
from CombinationController import CombinationController

from Locker import Locker
from LockerView import LockerView
from LockerController import LockerController

host_name = 'localhost'
name = 'fortnite'
username = 'postgres'
password = 'password'

def getFortnite():
    # will be used for set table
    all_sets = []

    # create postgres connection
    try:
        conn = pg.connect(host=host_name, dbname=name, user=username, password=password)
        cur = conn.cursor()

        # delete all tables if they exist only because Fortnite tends to add new cosmetics and recalling the API allows for new cosmetics to be accounted for
        cur.execute('DROP TABLE IF EXISTS locker;')
        cur.execute('DROP TABLE IF EXISTS backbling;')
        cur.execute('DROP TABLE IF EXISTS glider;')
        cur.execute('DROP TABLE IF EXISTS pickaxe;')
        cur.execute('DROP TABLE IF EXISTS outfit;')
        cur.execute('DROP TABLE IF EXISTS contrail;')
        cur.execute('DROP TABLE IF EXISTS fortnitesets;')
        conn.commit()

        create_table = 'CREATE TABLE IF NOT EXISTS fortniteSets (set_id VARCHAR(255) PRIMARY KEY, series_name VARCHAR(255), description VARCHAR(255));'
        cur.execute(create_table)
        conn.commit()

        create_table = 'CREATE TABLE IF NOT EXISTS glider (glider_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
        cur.execute(create_table)
        conn.commit()

        create_table = 'CREATE TABLE IF NOT EXISTS pickaxe (pickaxe_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
        cur.execute(create_table)
        conn.commit()

        create_table = 'CREATE TABLE IF NOT EXISTS outfit (outfit_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
        cur.execute(create_table)
        conn.commit()

        create_table = 'CREATE TABLE IF NOT EXISTS contrail (contrail_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
        cur.execute(create_table)
        conn.commit()

        create_table = 'CREATE TABLE IF NOT EXISTS backbling (backbling_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
        cur.execute(create_table)
        conn.commit()

        create_table = 'CREATE TABLE IF NOT EXISTS locker (id SERIAL PRIMARY KEY, combo_name VARCHAR(255), solo_wins INT, duo_wins INT, trio_wins INT, squad_wins INT, outfit_id VARCHAR(255), backbling_id VARCHAR(255), pickaxe_id VARCHAR(255), glider_id VARCHAR(255), contrail_id VARCHAR(255), FOREIGN KEY (outfit_id) REFERENCES outfit(outfit_id), FOREIGN KEY (backbling_id) REFERENCES backbling(backbling_id), FOREIGN KEY (pickaxe_id) REFERENCES pickaxe(pickaxe_id), FOREIGN KEY (glider_id) REFERENCES glider(glider_id), FOREIGN KEY (contrail_id) REFERENCES contrail(contrail_id));'
        cur.execute(create_table)
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()

    try:
        conn = pg.connect(host=host_name, dbname=name, user=username, password=password)
        cur = conn.cursor()

        # get contrails
        contrails = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=contrail')
        json = contrails.json()
        for i in range(len(json['data'])):
            ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
            # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
            if ser not in all_sets:
                all_sets.append(ser)
                if ser == 'N/A':
                    sn = 'N/A'
                    descr = 'N/A'
                else:
                    sn = json['data'][i]['set']['value']
                    descr = json['data'][i]['set']['text']

                insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
                insert_value = (ser, sn, descr)
                cur.execute(insert_script, insert_value)
                conn.commit()

            idd = json['data'][i]['id']
            n = json['data'][i]['name']
            desc = json['data'][i]['description']
            rar = json['data'][i]['rarity']['displayValue']

            insert_script = 'INSERT INTO contrail (contrail_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
            insert_value = (idd, n, desc, rar, ser)
            cur.execute(insert_script, insert_value)
            conn.commit()



        # get gliders into datatable
        gliders = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=glider')
        json = gliders.json()
        for i in range(len(json['data'])):
            ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
            # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
            if ser not in all_sets:
                all_sets.append(ser)
                if ser == 'N/A':
                    sn = 'N/A'
                    descr = 'N/A'
                else:
                    sn = json['data'][i]['set']['value']
                    descr = json['data'][i]['set']['text']

                insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
                insert_value = (ser, sn, descr)
                cur.execute(insert_script, insert_value)
                conn.commit()

            idd = json['data'][i]['id']
            n = json['data'][i]['name']
            desc = json['data'][i]['description']
            rar = json['data'][i]['rarity']['displayValue']

            insert_script = 'INSERT INTO glider (glider_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
            insert_value = (idd, n, desc, rar, ser)
            cur.execute(insert_script, insert_value)
            conn.commit()

        # get pickaxes
        pickaxes = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=pickaxe')
        json = pickaxes.json()
        for i in range(len(json['data'])):
            ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
            # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
            if ser not in all_sets:
                all_sets.append(ser)
                if ser == 'N/A':
                    sn = 'N/A'
                    descr = 'N/A'
                else:
                    sn = json['data'][i]['set']['value']
                    descr = json['data'][i]['set']['text']

                insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
                insert_value = (ser, sn, descr)
                cur.execute(insert_script, insert_value)
                conn.commit()

            idd = json['data'][i]['id']
            n = json['data'][i]['name']
            desc = json['data'][i]['description']
            rar = json['data'][i]['rarity']['displayValue']

            insert_script = 'INSERT INTO pickaxe (pickaxe_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
            insert_value = (idd, n, desc, rar, ser)
            cur.execute(insert_script, insert_value)
            conn.commit()

        # get skins
        pickaxes = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=outfit')
        json = pickaxes.json()
        for i in range(len(json['data'])):
            ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
            # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
            if ser not in all_sets:
                all_sets.append(ser)
                if ser == 'N/A':
                    sn = 'N/A'
                    descr = 'N/A'
                else:
                    sn = json['data'][i]['set']['value']
                    descr = json['data'][i]['set']['text']

                insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
                insert_value = (ser, sn, descr)
                cur.execute(insert_script, insert_value)
                conn.commit()

            idd = json['data'][i]['id']
            n = json['data'][i]['name']
            desc = json['data'][i]['description']
            rar = json['data'][i]['rarity']['displayValue']

            insert_script = 'INSERT INTO outfit (outfit_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
            insert_value = (idd, n, desc, rar, ser)
            cur.execute(insert_script, insert_value)
            conn.commit()

        # get backblings
        backblings = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=backpack')
        json = backblings.json()
        for i in range(len(json['data'])):
            ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
            # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
            if ser not in all_sets:
                all_sets.append(ser)
                if ser == 'N/A':
                    sn = 'N/A'
                    descr = 'N/A'
                else:
                    sn = json['data'][i]['set']['value']
                    descr = json['data'][i]['set']['text']

                insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
                insert_value = (ser, sn, descr)
                cur.execute(insert_script, insert_value)
                conn.commit()

            idd = json['data'][i]['id']
            n = json['data'][i]['name']
            desc = json['data'][i]['description']
            rar = json['data'][i]['rarity']['displayValue']

            insert_script = 'INSERT INTO backbling (backbling_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
            insert_value = (idd, n, desc, rar, ser)
            cur.execute(insert_script, insert_value)
            conn.commit()

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()

def menu():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nChoose what you would like to do...")
    print("1. Add a New Combo to your locker")
    print("2. See locker")
    print("3. Update number of wins of a Combo already in your locker")
    print("4. Exit")
    selection = input("\nSelection: ")
    return int(selection)

def updateMenu():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nChoose what you would like to do...")
    print("1. Update Solo Wins")
    print("2. Update Duo Wins")
    print("3. Update Trio Wins")
    print("4. Update Squad Wins")
    print("5. Back")
    selection = input("\nSelection: ")
    return int(selection)

def printOutfitNames():
    outfits = []
    try:
        conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
        cur = conn.cursor()

        script = 'SELECT name FROM outfit;'
        cur.execute(script)
        conn.commit()
        outfits = cur.fetchall()

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()
    return outfits

def printGliderNames():
    gliders = []
    try:
        conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
        cur = conn.cursor()

        script = 'SELECT name FROM glider;'
        cur.execute(script)
        conn.commit()
        gliders = cur.fetchall()

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()
    return gliders

def printContrailNames():
    contrails = []
    try:
        conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
        cur = conn.cursor()

        script = 'SELECT name FROM contrail;'
        cur.execute(script)
        conn.commit()
        contrails = cur.fetchall()

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()
    return contrails

def printPickaxeNames():
    pickaxes = []
    try:
        conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
        cur = conn.cursor()

        script = 'SELECT name FROM pickaxe;'
        cur.execute(script)
        conn.commit()
        pickaxes = cur.fetchall()

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()

    return pickaxes

def printBackblings():
    backblings = []
    try:
        conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
        cur = conn.cursor()

        script = 'SELECT name FROM backbling;'
        cur.execute(script)
        conn.commit()
        backblings = cur.fetchall()

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()
    return backblings

def validateChoice(choice, item):
    choiceID = ('wrong')
    try:
        conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
        cur = conn.cursor()

        script = ''
        if item == 'outfit':
            script = 'SELECT outfit_id FROM outfit WHERE name = %s;'
        elif item == 'glider':
            script = 'SELECT glider_id FROM glider WHERE name = %s;'
        elif item == 'backbling':
            script = 'SELECT backbling_id FROM backbling WHERE name = %s;'
        elif item == 'pickaxe':
            script = 'SELECT pickaxe_id FROM pickaxe WHERE name = %s;'
        elif item == 'contrail':
            script = 'SELECT contrail_id FROM contrail WHERE name = %s;'

        in_script = (choice,)
        cur.execute(script, in_script)
        conn.commit()
        choiceID = cur.fetchall()

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()

    print(choiceID[0][0])
    return choiceID[0][0]

def fortniteProject():
    print('Welcome to Fortnite Locker')
    comboV = CombinationView()
    comboC = CombinationController(Combination(), comboV)
    lockerC = LockerController(Locker(), LockerView(comboV))


    while True:
        selection = menu()

        if selection == 1: #  log in a new combo
            newCombo = Combination()
            comboC.setCombination(newCombo)
            name = input("Enter combination name: ")
            comboC.setComboName(name)
            comboC.setComboOutfit()
            comboC.setComboGlider()
            comboC.setComboPickaxe()
            comboC.setComboContrail()
            comboC.setComboBackbling()

            # outfits
            outfitNames = printOutfitNames()
            outfitlen = len(outfitNames)

            for i in range(outfitlen):
                print('{}: {}'.format(i, outfitNames[i][0]))

            outfitChoice = int(input("Enter outfit choice number or -1 for none: "))
            choice = validateChoice(outfitNames[outfitChoice][0], 'outfit') if outfitChoice != -1 else None
            if choice is not None:
                comboC.setComboOutfit(choice)
            elif choice == 'wrong':
                print('invalid')
                break

            # gliders
            gliderNames = printGliderNames()
            gliderlen = len(gliderNames)

            for i in range(gliderlen):
                print('{}: {}'.format(i, gliderNames[i][0]))

            gliderChoice = int(input("Enter glider choice number or -1 for none: "))
            choice = validateChoice(gliderNames[gliderChoice][0], 'glider') if gliderChoice != -1 else None
            if choice is not None:
                comboC.setComboGlider(choice)
            elif choice == 'wrong':
                print('invalid')
                break

            # pickaxes
            pickaxeNames = printPickaxeNames()
            pickaxelen = len(pickaxeNames)

            for i in range(pickaxelen):
                print('{}: {}'.format(i, pickaxeNames[i][0]))

            pickaxeChoice = int(input("Enter pickaxe choice number or -1 for none: "))
            choice = validateChoice(pickaxeNames[pickaxeChoice][0], 'pickaxe') if pickaxeChoice != -1 else None
            if choice is not None:
                comboC.setComboPickaxe(choice)
            elif choice == 'wrong':
                print('invalid')
                break

            # contrails
            contrailNames = printContrailNames()
            contraillen = len(contrailNames)

            for i in range(contraillen):
                print('{}: {}'.format(i, contrailNames[i][0]))

            contrailChoice = int(input("Enter Contrail choice number or -1 for none: "))
            choice = validateChoice(contrailNames[contrailChoice][0], 'contrail') if contrailChoice != -1 else None
            if choice is not None:
                comboC.setComboContrail(choice)
            elif choice == 'wrong':
                print('invalid')
                break

            # backblings
            backblingNames = printBackblings()
            backblinglen = len(backblingNames)

            for i in range(backblinglen):
                print('{}: {}'.format(i, backblingNames[i][0]))

            backblingChoice = int(input("Enter Back Bling choice number or -1 for none: "))
            choice = validateChoice(backblingNames[backblingChoice][0], 'backbling') if backblingChoice != -1 else None
            if choice is not None:
                comboC.setComboBackbling(choice)
            elif choice == 'wrong':
                print('invalid')
                break

            lockerC.addNewCombo(newCombo)

            print("Successfully added!\nSelect [3] in menu to log in number of wins!")

        elif selection == 2: # show locker
            lockerC.getLockeritems()
        elif selection == 3: # update existing combo
            while True:
                menuSelection = updateMenu()
                if menuSelection == 1:
                    num = int(input("\nEnter number to be added: "))
                    locker = lockerC.getAllLockerNames()
                    lockerlen = len(locker)
                    for i in range(lockerlen):
                        print('{}: {}'.format(i, locker[i]))
                    num2 = int(input("\nChoose which Combination to update: "))
                    chosen = locker[num2] if num2 < len(locker) else None
                    if chosen is None:
                        print("No such Combination")
                        break

                    # get the specific combo
                    lockerCombo = lockerC.getLockerCombos()
                    comboC.setCombination(lockerCombo[num2])
                    comboC.updateSolo(num)

                    print("Successfully updated")
                    break
                elif menuSelection == 2:
                    num = int(input("\nEnter number to be added: "))
                    locker = lockerC.getAllLockerNames()
                    lockerlen = len(locker)
                    for i in range(lockerlen):
                        print('{}: {}'.format(i, locker[i]))
                    num2 = int(input("\nChoose which Combination to update: "))
                    chosen = locker[num2] if num2 < len(locker) else None
                    if chosen is None:
                        print("No such Combination")
                        break

                    # get the specific combo
                    lockerCombo = lockerC.getLockerCombos()
                    comboC.setCombination(lockerCombo[num2])
                    comboC.updateDuo(num)

                    print("Successfully updated")
                    break
                elif menuSelection == 3:
                    num = int(input("\nEnter number to be added: "))
                    locker = lockerC.getAllLockerNames()
                    lockerlen = len(locker)
                    for i in range(lockerlen):
                        print('{}: {}'.format(i, locker[i]))
                    num2 = int(input("\nChoose which Combination to update: "))
                    chosen = locker[num2] if num2 < len(locker) else None
                    if chosen is None:
                        print("No such Combination")
                        break

                    # get the specific combo
                    lockerCombo = lockerC.getLockerCombos()
                    comboC.setCombination(lockerCombo[num2])
                    comboC.updateTrio(num)

                    print("Successfully updated")
                    break
                elif menuSelection == 4:
                    num = int(input("\nEnter number to be added: "))
                    locker = lockerC.getAllLockerNames()
                    lockerlen = len(locker)
                    for i in range(lockerlen):
                        print('{}: {}'.format(i, locker[i]))
                    num2 = int(input("\nChoose which Combination to update: "))
                    chosen = locker[num2] if num2 < len(locker) else None
                    if chosen is None:
                        print("No such Combination")
                        break

                    # get the specific combo
                    lockerCombo = lockerC.getLockerCombos()
                    comboC.setCombination(lockerCombo[num2])
                    comboC.updateSquad(num)

                    print("Successfully updated")
                    break
                elif menuSelection == 5:
                    break
                else:
                    print("Invalid")

        elif selection == 4: # exit
            exit()
        else:
            print("Invalid")

if __name__ == '__main__':
    # getFortnite()
    fortniteProject()


