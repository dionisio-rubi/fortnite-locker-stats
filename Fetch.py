import psycopg as pg
import requests


class Fetch:
    """Fetch Class that fetches data from the database"""

    def __init__(self):
        self.host_name = 'localhost'
        self.name = 'fortnite'
        self.username = 'postgres'
        self.password = 'password'

    def getFortnite(self):
        # will be used for set table
        all_sets = []

        # create postgres connection
        try:
            conn = pg.connect(host=self.host_name, dbname=self.name, user=self.username, password=self.password)
            cur = conn.cursor()

            # delete all tables if they exist

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
            conn = pg.connect(host=self.host_name, dbname=self.name, user=self.username, password=self.password)
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

    def printOutfitNames(self):
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

    def printGliderNames(self):
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

    def printContrailNames(self):
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

    def printPickaxeNames(self):
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

    def printBackblings(self):
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
