from ViewAll import ViewAll
from Fetch import Fetch

if __name__ == '__main__':
#     getFortnite()
    fortnite = ViewAll(Fetch.printOutfitNames(), Fetch.printPickaxeNames(), Fetch.printContrailNames(), Fetch.printBackblings(), Fetch.printGliderNames())
    fortnite.start()


