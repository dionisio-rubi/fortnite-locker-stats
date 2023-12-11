import psycopg as pg

class Combination:
    """Combination Class that has information about one specific combo"""
    def __init__(self, name='', outfit='CID_Creative_Mannequin_M_Default', pickaxe='', glider='', contrail='', backbling='', solo_wins=0, duo_wins=0, trio_wins=0, squad_wins=0):
        # self.default_outfit = 'CID_Creative_Mannequin_M_Default'
        # self.default_pickaxe = 'DefaultPickaxe'
        # self.default_glider = 'DefaultGlider'
        # self.default_contrail = 'DefaultContrail'
        # self.default_backbling = 'BID_STWHeroNoDefaultBackpack'

        self.name = name
        self.outfit = outfit
        self.pickaxe = pickaxe
        self.glider = glider
        self.contrail = contrail
        self.backbling = backbling
        self.solo_wins = solo_wins
        self.duo_wins = duo_wins
        self.trio_wins = trio_wins
        self.squad_wins = squad_wins

    def setName(self, name):
        """Set the name of the combo"""
        self.name = name

    def setOutfit(self, outfit_id='CID_Creative_Mannequin_M_Default'):
        """Set the outfit of the combo"""
        self.outfit = outfit_id

    def setPickaxe(self, pickaxe_id='DefaultPickaxe'):
        """Set the pickaxe of the combo"""
        self.pickaxe = pickaxe_id

    def setGlider(self, glider_id='DefaultGlider'):
        """Set the glider of the combo"""
        self.glider = glider_id

    def setContrail(self, contrail_id='DefaultContrail'):
        """Set the contrail of the combo"""
        self.contrail = contrail_id

    def setBackbling(self, backbling_id='BID_STWHeroNoDefaultBackpack'):
        """Set the backbling of the combo"""
        self.backbling = backbling_id

    def updateSoloWins(self, newWins):
        """Update the solo wins count of the combo by wins + newWins"""
        self.solo_wins += newWins

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'UPDATE locker SET solo_wins = %s WHERE combo_name = %s;'
            insert_statement = (self.solo_wins, self.name)
            cur.execute(script, insert_statement)
            conn.commit()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

    def updateDuoWins(self, newWins):
        """Update the duo wins count of the combo by wins + newWins"""
        self.duo_wins += newWins

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'UPDATE locker SET duo_wins = %s WHERE combo_name = %s;'
            insert_statement = (self.duo_wins, self.name)
            cur.execute(script, insert_statement)
            conn.commit()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

    def updateTrioWins(self, newWins):
        """Update the trio wins count of the combo by wins + newWins"""
        self.trio_wins += newWins

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'UPDATE locker SET trio_wins = %s WHERE combo_name = %s;'
            insert_statement = (self.trio_wins, self.name)
            cur.execute(script, insert_statement)
            conn.commit()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

    def updateSquadWins(self, newWins):
        """Update the squad wins count of the combo by wins + newWins"""
        self.squad_wins += newWins

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'UPDATE locker SET squad_wins = %s WHERE combo_name = %s;'
            insert_statement = (self.squad_wins, self.name)
            cur.execute(script, insert_statement)
            conn.commit()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

    def getOutfit(self):
        """returns all the info about the outfit in the form of a list"""
        information = []

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()
            script = 'SELECT outfit.name, outfit.description, outfit.rarity, fortniteSets.series_name, fortniteSets.description FROM outfit JOIN fortniteSets ON outfit.set_id = fortniteSets.set_id WHERE outfit.outfit_id = %s'
            insert_statement = self.outfit
            cur.execute(script, (insert_statement,))
            conn.commit()
            information = cur.fetchall()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

        return information

    def getGlider(self):
        """returns all the info about the glider in the form of a list"""
        information = []

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'SELECT o.name, o.description, o.rarity, fs.series_name, fs.description FROM glider AS o JOIN fortniteSets AS fs ON o.set_id = fs.set_id WHERE o.glider_id = %s;'
            insert_statement = (self.glider,)
            cur.execute(script, insert_statement)
            conn.commit()
            information = cur.fetchall()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

        return information

    def getContrail(self):
        """returns all the info about the contrail in the form of a list"""
        information = []

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'SELECT o.name, o.description, o.rarity, fs.series_name, fs.description FROM contrail AS o JOIN fortniteSets AS fs ON o.set_id = fs.set_id WHERE o.contrail_id = %s;'
            insert_statement = (self.contrail,)
            cur.execute(script, insert_statement)
            conn.commit()
            information = cur.fetchall()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

        return information

    def getBackbling(self):
        """returns all the info about the backbling in the form of a list"""
        information = []

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'SELECT o.name, o.description, o.rarity, fs.series_name, fs.description FROM backbling AS o JOIN fortniteSets AS fs ON o.set_id = fs.set_id WHERE o.backbling_id = %s;'
            insert_statement = (self.backbling,)
            cur.execute(script, insert_statement)
            conn.commit()
            information = cur.fetchall()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

        return information

    def getPickaxe(self):
        """returns all the info about the pickaxe in the form of a list"""
        information = []

        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'SELECT o.name, o.description, o.rarity, fs.series_name, fs.description FROM pickaxe AS o JOIN fortniteSets AS fs ON o.set_id = fs.set_id WHERE o.pickaxe_id = %s;'
            insert_statement = (self.pickaxe,)
            cur.execute(script, insert_statement)
            conn.commit()
            information = cur.fetchall()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

        return information

    def getName(self):
        """returns the name of the combo"""
        return self.name

    def getSoloWins(self):
        """Get the solo wins count"""
        return self.solo_wins

    def getDuoWins(self):
        """Get the duo wins count"""
        return self.duo_wins

    def getTrioWins(self):
        """Get the trio wins count"""
        return self.trio_wins

    def getSquadWins(self):
        """Get the squad wins count"""
        return self.squad_wins

    def getOutfitID(self):
        """get the outfit ID of the combo"""
        return self.outfit

    def getPickaxeID(self):
        """get the pickaxe ID of the combo"""
        return self.pickaxe

    def getGliderID(self):
        """get the glider id of the combo"""
        return self.glider

    def getContrailID(self):
        """get the contrail ID of the combo"""
        return self.contrail

    def getBackblingID(self):
        """get the backbling ID of the combo"""
        return self.backbling
