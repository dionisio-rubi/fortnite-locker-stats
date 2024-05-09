from ViewAll import ViewAll
from Fetch import Fetch

if __name__ == '__main__':
#     getFortnite()
    fetch = Fetch()
    outfits = fetch.printOutfitNames()
    pickaxes = fetch.printPickaxeNames()
    contrails = fetch.printContrailNames()
    backblings = fetch.printBackblings()
    gliders = fetch.printGliderNames()
    fortnite = ViewAll(outfits, pickaxes, contrails, backblings, gliders)
    fortnite.start()


