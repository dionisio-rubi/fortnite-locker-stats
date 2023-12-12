from Combination import Combination
from CombinationView import CombinationView
from CombinationController import CombinationController

import psycopg as pg

from Locker import Locker
from LockerView import LockerView
from LockerController import LockerController
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import scrolledtext
class ViewAll:
    def __init__(self, outfits, pickaxes, contrails, backblings, gliders):
        self.comboV = CombinationView()
        self.comboC = CombinationController(Combination(), self.comboV)
        self.lockerC = LockerController(Locker(), LockerView(self.comboV))

        self.outfits = [i[0] for i in outfits]
        self.pickaxes = [i[0] for i in pickaxes]
        self.contrails = [i[0] for i in contrails]
        self.backblings = [i[0] for i in backblings]
        self.gliders = [i[0] for i in gliders]

        self.bg_color = "#5fceea"
        self.root = tk.Tk()
        self.root.title('Fortnite Locker Stats')
        self.root.eval("tk::PlaceWindow . center")

        self.mainFrame = tk.Frame(self.root, width=800, height=800, bg=self.bg_color)
        self.loggingFrame = tk.Frame(self.root, bg=self.bg_color)
        self.lockerFrame = tk.Frame(self.root, bg=self.bg_color)
        self.updatingFrame = tk.Frame(self.root, bg=self.bg_color)

        for frame in [self.mainFrame, self.loggingFrame, self.lockerFrame, self.updatingFrame]:
            frame.grid(row=0, column=0, sticky="nesw")


    def welcomeFrame(self):
        self.clear_widgets(self.loggingFrame)
        self.clear_widgets(self.lockerFrame)
        self.clear_widgets(self.updatingFrame)
        self.mainFrame.tkraise()
        self.mainFrame.pack_propagate(False)
        # mainFrame widgets
        welcome = tk.Label(self.mainFrame, text='Welcome to your Fortnite Locker!', fg="black", font=('TKMenuFont', 24), bg=self.bg_color).pack(pady=60)
        logbtn = tk.Button(self.mainFrame, width=20, text='Log a New Combo', font=('TKHeadingFont', 18), bg='#1B90DD', fg='white', cursor="hand2", activebackground="black", activeforeground="white",
                           command=lambda: self.logFrame()).pack(pady=20)
        seebtn = tk.Button(self.mainFrame, width=20, text='See Locker', font=('TKHeadingFont', 18), bg='#1B90DD', fg='white',
                           cursor="hand2", activebackground="black", activeforeground="white",
                           command=lambda: self.seeFrame()).pack(pady=20)
        updatebtn = tk.Button(self.mainFrame, width=20, text='Update Existing Combo', font=('TKHeadingFont', 18), bg='#1B90DD',
                              fg='white', cursor="hand2", activebackground="black", activeforeground="white",
                              command=lambda: self.updateFrame()).pack(pady=20)

    def clear_widgets(self, frame):
        """Clears all widgets of a frame"""
        for widget in frame.winfo_children():
            widget.destroy()

    def logFrame(self):
        """The logging page"""
        self.clear_widgets(self.mainFrame)
        self.loggingFrame.tkraise()

        welcome = tk.Label(self.loggingFrame, text='Log in new Combo Information', font=('TKMenuFont', 24),
                           bg=self.bg_color).pack(pady=60)
        welcome2 = tk.Label(self.loggingFrame, text='Enter what you would like to name your combo', font=('TKMenuFont', 18),
                            bg=self.bg_color).pack(pady=10)

        entry = tk.Entry(self.loggingFrame)
        entry.pack(pady=10)

        welcome2 = tk.Label(self.loggingFrame, text='Select Outfit', font=('TKMenuFont', 18),
                            bg=self.bg_color).pack(pady=10)

        outfit = tk.StringVar()
        dropdown = tk.OptionMenu(self.loggingFrame, outfit, *self.outfits).pack(pady=10)
        outfit.set(self.outfits[0])
        # selectedLockerName.trace('w', lambda *args: self.on_select(selectedLockerName.get()))

        welcome2 = tk.Label(self.loggingFrame, text='Select Backbling', font=('TKMenuFont', 18),
                            bg=self.bg_color).pack(pady=10)

        backbling = tk.StringVar()
        dropdown = tk.OptionMenu(self.loggingFrame, backbling, *self.backblings).pack(pady=10)
        backbling.set(self.backblings[0])

        welcome2 = tk.Label(self.loggingFrame, text='Select Contrail', font=('TKMenuFont', 18),
                            bg=self.bg_color).pack(pady=10)

        contrail = tk.StringVar()
        dropdown = tk.OptionMenu(self.loggingFrame, contrail, *self.contrails).pack(pady=10)
        contrail.set(self.contrails[0])

        welcome2 = tk.Label(self.loggingFrame, text='Select Glider', font=('TKMenuFont', 18),
                            bg=self.bg_color).pack(pady=10)

        glider = tk.StringVar()
        dropdown = tk.OptionMenu(self.loggingFrame, glider, *self.gliders).pack(pady=10)
        glider.set(self.gliders[0])

        welcome2 = tk.Label(self.loggingFrame, text='Select Pickaxe', font=('TKMenuFont', 18),
                            bg=self.bg_color).pack(pady=10)

        pickaxe = tk.StringVar()
        dropdown = tk.OptionMenu(self.loggingFrame, pickaxe, *self.pickaxes).pack(pady=10)
        pickaxe.set(self.pickaxes[0])

        welcome2 = tk.Label(self.loggingFrame, text='Select Update Existing Combo in menu to log in number of wins!',
                            font=('TKMenuFont', 14),
                            bg=self.bg_color).pack(pady=10)

        enter_button = tk.Button(self.loggingFrame, text='Enter', font=('TKHeadingFont', 16), bg='#1B90DD', fg='white',
                                 cursor="hand2", activebackground="black", activeforeground="white",
                                 width=10,
                                 command=lambda: self.on_select(entry.get(), self.get_id('outfit', outfit.get()), self.get_id('backbling', backbling.get()),self.get_id('contrail', contrail.get()), self.get_id('glider', glider.get()), self.get_id('pickaxe', pickaxe.get()))).pack(pady=10)

        gobackbtn = tk.Button(self.loggingFrame, text='Go Back ', font=('TKHeadingFont', 16), bg='darkblue',
                              fg='white',
                              cursor="hand2", activebackground="black", activeforeground="white",
                              width=10, command=lambda: self.welcomeFrame()).pack(pady=20)
    def updateFrame(self):
        """The page where users can update a combo"""
        self.clear_widgets(self.mainFrame)
        self.updatingFrame.tkraise()

        welcome = tk.Label(self.updatingFrame, text='Time to Update Locker Info', font=('TKMenuFont', 24), bg=self.bg_color).pack(pady=60)
        welcome2 = tk.Label(self.updatingFrame, text='Choose the combination name you', font=('TKMenuFont', 18), bg=self.bg_color).pack()
        welcome2 = tk.Label(self.updatingFrame, text='would like to update from the dropdown', font=('TKMenuFont', 18), bg=self.bg_color).pack(pady=20)

        lockerItems = self.lockerC.getAllLockerNames()

        selectedLockerName = tk.StringVar()
        dropdown = tk.OptionMenu(self.updatingFrame, selectedLockerName, *lockerItems).pack(pady=20)
        selectedLockerName.set(lockerItems[0])
        # selectedLockerName.trace('w', lambda *args: self.on_select(selectedLockerName.get()))

        welcome2 = tk.Label(self.updatingFrame, text='Enter number of wins:', font=('TKMenuFont', 18), bg=self.bg_color).pack(pady=20)
        entry = tk.Entry(self.updatingFrame)
        entry.pack(pady=10)

        welcome2 = tk.Label(self.updatingFrame, text='Choose win type', font=('TKMenuFont', 18), bg=self.bg_color).pack(pady=20)

        solo_button = tk.Button(self.updatingFrame, text='Solo', font=('TKHeadingFont', 16), bg='#1B90DD', fg='white',
                              cursor="hand2", activebackground="black", activeforeground="white",
                              width=10, command=lambda: self.updateIt('solo', selectedLockerName.get(), entry.get())).pack(pady=10)

        duo_button = tk.Button(self.updatingFrame, text='Duo', font=('TKHeadingFont', 16), bg='#1B90DD', fg='white',
                                cursor="hand2", activebackground="black", activeforeground="white",
                                width=10, command=lambda: self.updateIt('duo', selectedLockerName.get(), entry.get())).pack(pady=10)

        trio_button = tk.Button(self.updatingFrame, text='Trio', font=('TKHeadingFont', 16), bg='#1B90DD', fg='white',
                                cursor="hand2", activebackground="black", activeforeground="white",
                                width=10, command=lambda: self.updateIt('trio', selectedLockerName.get(), entry.get())).pack(pady=10)

        squad_button = tk.Button(self.updatingFrame, text='Squad', font=('TKHeadingFont', 16), bg='#1B90DD', fg='white',
                                cursor="hand2", activebackground="black", activeforeground="white",
                                width=10, command=lambda: self.updateIt('squad', selectedLockerName.get(), entry.get())).pack(pady=10)

        gobackbtn = tk.Button(self.updatingFrame, text='Go Back ', font=('TKHeadingFont', 16), bg='darkblue', fg='white',
                              cursor="hand2", activebackground="black", activeforeground="white",
                              width=10, command=lambda: self.welcomeFrame()).pack(pady=20)

    def updateIt(self, kind, combo, wins):
        """update locker"""
        try:
            wins = int(wins)
        except ValueError:
            messagebox.showerror('Error', 'Invalid')
            self.welcomeFrame()

        lockerNames = self.lockerC.getLockerCombos()
        specificCombo = Combination()
        for lockerName in lockerNames:
            if lockerName.getName() == combo:
                specificCombo = lockerName
                break


        self.comboC.setCombination(specificCombo)
        if kind == 'squad':
            self.comboC.updateSquad(wins)
        elif kind == 'trio':
            self.comboC.updateTrio(wins)
        elif kind == 'duo':
            self.comboC.updateDuo(wins)
        elif kind == 'solo':
            self.comboC.updateSolo(wins)
        self.welcomeFrame()

    def on_select(self, name, outfit, backbling, contrail, glider, pickaxe):
        newCombo = Combination(name, outfit, pickaxe, glider, contrail, backbling, )
        self.lockerC.addNewCombo(newCombo)

        self.lockerC.getLockerCombos()
        self.welcomeFrame()

    def get_id(self, item, choice):
        choiceID = ''
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

        return choiceID[0][0]

    def seeFrame(self):
        self.clear_widgets(self.mainFrame)
        self.lockerFrame.tkraise()

        welcome = tk.Label(self.lockerFrame, text='See Your Locker', font=('TKMenuFont', 24), bg=self.bg_color).pack(pady=20)

        lockerItems = self.lockerC.getLockeritems()

        # Create a Text widget as a container for the labels
        text_widget = scrolledtext.ScrolledText(self.lockerFrame, wrap="word", font=("TKMenuFont", 10), bg="#0A0080", fg="white", width=50, height=10)
        text_widget.pack(pady=20, padx=20, fill="both", expand=True)

        # Add labels to the Text widget
        for i in lockerItems:
            for j in i:
                for k in j:
                    text_widget.insert(tk.END, f"{k}\n")

        gobackbtn = tk.Button(self.lockerFrame, text='Go Back ', font=('TKHeadingFont', 16), bg='darkblue',
                              fg='white',
                              cursor="hand2", activebackground="black", activeforeground="white",
                              width=10, command=lambda: self.welcomeFrame())
        gobackbtn.pack(pady=20)

    def start(self):
        """Starts the loop"""

        self.welcomeFrame()
        self.root.mainloop()