import psycopg as pg
from Combination import Combination

class Locker:
    """Represents a user's Fortnite Locker"""
    def __init__(self):
        self.locker = []

        self.temp = []
        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()
            script = 'SELECT * FROM locker'
            cur.execute(script)
            conn.commit()
            self.temp = cur.fetchall()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

        for (_, n, solo, duo, trio, squads, o, b, p, g, c) in self.temp:
            combo = Combination(n, o, p, g, c, b, solo, duo, trio, squads)
            self.locker.append(combo)

    def getLocker(self):
        """Returns the locker"""
        return self.locker

    def getLockerName(self):
        """returns a list of locker names"""
        lockerNames = []
        for l in self.locker:
            lockerNames.append(l.getName())

        return lockerNames

    def addCombo(self, combo: Combination):
        """Adds a combo to the locker"""
        self.locker.append(combo)
        try:
            conn = pg.connect(host='localhost', dbname='fortnite', user='postgres', password='password')
            cur = conn.cursor()

            script = 'INSERT INTO locker (combo_name, solo_wins, duo_wins, trio_wins, squad_wins, outfit_id, backbling_id, pickaxe_id, glider_id, contrail_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            insert_statement = (combo.getName(), combo.getSoloWins(), combo.getDuoWins(), combo.getTrioWins(), combo.getSquadWins(), combo.getOutfitID(), combo.getBackblingID(), combo.getPickaxeID(), combo.getGliderID(), combo.getContrailID())
            cur.execute(script, insert_statement)
            conn.commit()

        except Exception as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()