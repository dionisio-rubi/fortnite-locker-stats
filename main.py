import psycopg as pg
import requests
import tkinter as tk
bg_color = "#5fceea"

# from MyGUI import MyGUI
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

# def getFortnite():
#     # will be used for set table
#     all_sets = []
#
#     # create postgres connection
#     try:
#         conn = pg.connect(host=host_name, dbname=name, user=username, password=password)
#         cur = conn.cursor()
#
#         #delete all tables if they exist
#         cur.execute('DROP TABLE IF EXISTS locker;')
#         cur.execute('DROP TABLE IF EXISTS backbling;')
#         cur.execute('DROP TABLE IF EXISTS glider;')
#         cur.execute('DROP TABLE IF EXISTS pickaxe;')
#         cur.execute('DROP TABLE IF EXISTS outfit;')
#         cur.execute('DROP TABLE IF EXISTS contrail;')
#         cur.execute('DROP TABLE IF EXISTS fortnitesets;')
#         conn.commit()
#
#         create_table = 'CREATE TABLE IF NOT EXISTS fortniteSets (set_id VARCHAR(255) PRIMARY KEY, series_name VARCHAR(255), description VARCHAR(255));'
#         cur.execute(create_table)
#         conn.commit()
#
#         create_table = 'CREATE TABLE IF NOT EXISTS glider (glider_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
#         cur.execute(create_table)
#         conn.commit()
#
#         create_table = 'CREATE TABLE IF NOT EXISTS pickaxe (pickaxe_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
#         cur.execute(create_table)
#         conn.commit()
#
#         create_table = 'CREATE TABLE IF NOT EXISTS outfit (outfit_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
#         cur.execute(create_table)
#         conn.commit()
#
#         create_table = 'CREATE TABLE IF NOT EXISTS contrail (contrail_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
#         cur.execute(create_table)
#         conn.commit()
#
#         create_table = 'CREATE TABLE IF NOT EXISTS backbling (backbling_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), rarity VARCHAR(255), set_id VARCHAR(255), FOREIGN KEY (set_id) REFERENCES fortniteSets(set_id));'
#         cur.execute(create_table)
#         conn.commit()
#
#         create_table = 'CREATE TABLE IF NOT EXISTS locker (id SERIAL PRIMARY KEY, combo_name VARCHAR(255), solo_wins INT, duo_wins INT, trio_wins INT, squad_wins INT, outfit_id VARCHAR(255), backbling_id VARCHAR(255), pickaxe_id VARCHAR(255), glider_id VARCHAR(255), contrail_id VARCHAR(255), FOREIGN KEY (outfit_id) REFERENCES outfit(outfit_id), FOREIGN KEY (backbling_id) REFERENCES backbling(backbling_id), FOREIGN KEY (pickaxe_id) REFERENCES pickaxe(pickaxe_id), FOREIGN KEY (glider_id) REFERENCES glider(glider_id), FOREIGN KEY (contrail_id) REFERENCES contrail(contrail_id));'
#         cur.execute(create_table)
#         conn.commit()
#     except Exception as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#         if cur is not None:
#             cur.close()
#
#     try:
#         conn = pg.connect(host=host_name, dbname=name, user=username, password=password)
#         cur = conn.cursor()
#
#         # get contrails
#         contrails = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=contrail')
#         json = contrails.json()
#         for i in range(len(json['data'])):
#             ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
#             # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
#             if ser not in all_sets:
#                 all_sets.append(ser)
#                 if ser == 'N/A':
#                     sn = 'N/A'
#                     descr = 'N/A'
#                 else:
#                     sn = json['data'][i]['set']['value']
#                     descr = json['data'][i]['set']['text']
#
#                 insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
#                 insert_value = (ser, sn, descr)
#                 cur.execute(insert_script, insert_value)
#                 conn.commit()
#
#             idd = json['data'][i]['id']
#             n = json['data'][i]['name']
#             desc = json['data'][i]['description']
#             rar = json['data'][i]['rarity']['displayValue']
#
#             insert_script = 'INSERT INTO contrail (contrail_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
#             insert_value = (idd, n, desc, rar, ser)
#             cur.execute(insert_script, insert_value)
#             conn.commit()
#
#
#
#         # get gliders into datatable
#         gliders = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=glider')
#         json = gliders.json()
#         for i in range(len(json['data'])):
#             ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
#             # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
#             if ser not in all_sets:
#                 all_sets.append(ser)
#                 if ser == 'N/A':
#                     sn = 'N/A'
#                     descr = 'N/A'
#                 else:
#                     sn = json['data'][i]['set']['value']
#                     descr = json['data'][i]['set']['text']
#
#                 insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
#                 insert_value = (ser, sn, descr)
#                 cur.execute(insert_script, insert_value)
#                 conn.commit()
#
#             idd = json['data'][i]['id']
#             n = json['data'][i]['name']
#             desc = json['data'][i]['description']
#             rar = json['data'][i]['rarity']['displayValue']
#
#             insert_script = 'INSERT INTO glider (glider_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
#             insert_value = (idd, n, desc, rar, ser)
#             cur.execute(insert_script, insert_value)
#             conn.commit()
#
#         # get pickaxes
#         pickaxes = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=pickaxe')
#         json = pickaxes.json()
#         for i in range(len(json['data'])):
#             ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
#             # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
#             if ser not in all_sets:
#                 all_sets.append(ser)
#                 if ser == 'N/A':
#                     sn = 'N/A'
#                     descr = 'N/A'
#                 else:
#                     sn = json['data'][i]['set']['value']
#                     descr = json['data'][i]['set']['text']
#
#                 insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
#                 insert_value = (ser, sn, descr)
#                 cur.execute(insert_script, insert_value)
#                 conn.commit()
#
#             idd = json['data'][i]['id']
#             n = json['data'][i]['name']
#             desc = json['data'][i]['description']
#             rar = json['data'][i]['rarity']['displayValue']
#
#             insert_script = 'INSERT INTO pickaxe (pickaxe_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
#             insert_value = (idd, n, desc, rar, ser)
#             cur.execute(insert_script, insert_value)
#             conn.commit()
#
#         # get skins
#         pickaxes = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=outfit')
#         json = pickaxes.json()
#         for i in range(len(json['data'])):
#             ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
#             # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
#             if ser not in all_sets:
#                 all_sets.append(ser)
#                 if ser == 'N/A':
#                     sn = 'N/A'
#                     descr = 'N/A'
#                 else:
#                     sn = json['data'][i]['set']['value']
#                     descr = json['data'][i]['set']['text']
#
#                 insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
#                 insert_value = (ser, sn, descr)
#                 cur.execute(insert_script, insert_value)
#                 conn.commit()
#
#             idd = json['data'][i]['id']
#             n = json['data'][i]['name']
#             desc = json['data'][i]['description']
#             rar = json['data'][i]['rarity']['displayValue']
#
#             insert_script = 'INSERT INTO outfit (outfit_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
#             insert_value = (idd, n, desc, rar, ser)
#             cur.execute(insert_script, insert_value)
#             conn.commit()
#
#         # get backblings
#         backblings = requests.get('https://fortnite-api.com/v2/cosmetics/br/search/all?type=backpack')
#         json = backblings.json()
#         for i in range(len(json['data'])):
#             ser = json['data'][i]['set']['backendValue'] if json['data'][i]['set'] is not None else 'N/A'
#             # to add sets not already in the set table, helps so I don't have to use a bunch of joins later on
#             if ser not in all_sets:
#                 all_sets.append(ser)
#                 if ser == 'N/A':
#                     sn = 'N/A'
#                     descr = 'N/A'
#                 else:
#                     sn = json['data'][i]['set']['value']
#                     descr = json['data'][i]['set']['text']
#
#                 insert_script = 'INSERT INTO fortniteSets (set_id, series_name, description) VALUES (%s, %s, %s)'
#                 insert_value = (ser, sn, descr)
#                 cur.execute(insert_script, insert_value)
#                 conn.commit()
#
#             idd = json['data'][i]['id']
#             n = json['data'][i]['name']
#             desc = json['data'][i]['description']
#             rar = json['data'][i]['rarity']['displayValue']
#
#             insert_script = 'INSERT INTO backbling (backbling_id, name, description, rarity, set_id) VALUES (%s, %s, %s, %s, %s)'
#             insert_value = (idd, n, desc, rar, ser)
#             cur.execute(insert_script, insert_value)
#             conn.commit()
#
#     except Exception as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#         if cur is not None:
#             cur.close()

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def welcomeFrame():
    clear_widgets(loggingFrame)
    clear_widgets(lockerFrame)
    clear_widgets(updatingFrame)
    mainFrame.tkraise()
    # bg_color = "#5fceea"
    mainFrame.pack_propagate(False)
    # mainFrame widgets
    welcome = tk.Label(mainFrame, text='Welcome to your Fortnite Locker!', fg="black", font=('TKMenuFont', 24), bg=bg_color).pack(pady=60)
    logbtn = tk.Button(mainFrame, text='Log a New Combo', font=('TKHeadingFont', 18), bg='#1B90DD', fg='white', cursor="hand2", activebackground="black", activeforeground="white", command=lambda: logFrame()).pack(pady=20)
    seebtn = tk.Button(mainFrame, text='See Locker', font=('TKHeadingFont', 18), bg='#1B90DD', fg='white', cursor="hand2", activebackground="black", activeforeground="white", command=lambda: seeFrame()).pack(pady=20)
    updatebtn = tk.Button(mainFrame, text='Update Existing Combo', font=('TKHeadingFont', 18), bg='#1B90DD', fg='white', cursor="hand2", activebackground="black", activeforeground="white", command=lambda: updateFrame()).pack(pady=20)


def logFrame():
    clear_widgets(mainFrame)
    loggingFrame.tkraise()

    welcome1 = tk.Label(loggingFrame, text='Ready to Start a New Log', font=('TKMenuFont', 24), bg=bg_color).pack(pady=40)
    welcome2 = tk.Label(loggingFrame, text='Start by entering the name for your new locker combo', font=('TKMenuFont', 14), bg=bg_color).pack(pady=20)

    gobackbtn = tk.Button(loggingFrame, text='Go Back ', font=('TKHeadingFont', 16), bg='#1B90DD', fg='white', cursor="hand2", activebackground="black", activeforeground="white", command=lambda: welcomeFrame()).pack(pady=20)

def seeFrame():
    clear_widgets(mainFrame)
    lockerFrame.tkraise()

    welcome = tk.Label(lockerFrame, text='See Your Locker', font=('TKMenuFont', 24), bg=bg_color).pack(pady=60)

    lockerItems = lockerC.getLockeritems()
    print("here2")
    for i in lockerItems:
        print(lockerItems)
        for j in i:
            for k in j:
                print("here")
                tk.Label(lockerFrame, text=k, bg="blue", fg="white", font=("TKMenuFont", 12)).pack(fill="both")

    gobackbtn = tk.Button(lockerFrame, text='Go Back ', font=('TKHeadingFont', 16), bg='#1B90DD', fg='white', cursor="hand2", activebackground="black", activeforeground="white", command=lambda: welcomeFrame()).pack(pady=20)

def updateFrame():
    clear_widgets(mainFrame)
    updatingFrame.tkraise()

    welcome = tk.Label(updatingFrame, text='', font=('TKMenuFont', 24), bg=bg_color).pack(pady=60)


    gobackbtn = tk.Button(updatingFrame, text='Go Back ', font=('TKHeadingFont', 16), bg='#1B90DD', fg='white', cursor="hand2", activebackground="black", activeforeground="white", command=lambda: welcomeFrame()).pack(pady=20)


# MyGUI()

# getFortnite()

# combo1 = Combination()
comboV = CombinationView()
comboC = CombinationController(Combination(), comboV)
# locker = Locker()
# lockerV = LockerView(comboV)
lockerC = LockerController(Locker(), LockerView(comboV))

root = tk.Tk()
root.title('Fortnite Locker Stats')
root.eval("tk::PlaceWindow . center")

mainFrame = tk.Frame(root, width=800, height=800, bg=bg_color)
loggingFrame = tk.Frame(root, bg=bg_color)
lockerFrame = tk.Frame(root, bg=bg_color)
updatingFrame = tk.Frame(root, bg=bg_color)

for frame in [mainFrame, loggingFrame, lockerFrame, updatingFrame]:
    frame.grid(row=0, column=0, sticky="nesw")

welcomeFrame()

root.mainloop()

#
# comboC.setComboName("test")
# comboC.setComboOutfit()
# comboC.setComboGlider()
# comboC.setComboPickaxe()
# comboC.setComboContrail()
# comboC.setComboBackbling()
#
# lockerC.addNewCombo(combo1)
# lockerC.getLockeritems()
# comboC.updateSolo(2)
# lockerC.getLockeritems()

# if __name__ == '__main__':
#     getFortnite()


