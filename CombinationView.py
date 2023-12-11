from Combination import Combination
# from CombinationController import CombinationController
# import tkinter as tk

class CombinationView:
    """The view for the Combination class"""

    def __init__(self):
        self.combo = Combination()

    def printCombination(self, combo: Combination):
        """Prints the entire Combination with all the information"""
        self.combo = combo

        res = []
        res.append(self.printComboNames())
        res.append(self.printComboInformation())

        return res

    def printComboNames(self):
        """Prints the names of the combinations"""
        print("Combination: ", self.combo.getName())
        return [str("Combination: " + self.combo.getName())]

    def printComboInformation(self):
        """prints the information about the combination"""
        result = []

        outfit_info = self.combo.getOutfit()
        glider_info = self.combo.getGlider()
        pickaxe_info = self.combo.getPickaxe()
        backbling_info = self.combo.getBackbling()
        contrail_info = self.combo.getContrail()

        print("   ~ Outfit Name: ", outfit_info[0][0])
        print("       ~ Description: ", outfit_info[0][1])
        print("       ~ Rarity: ", outfit_info[0][2])
        print("       ~ Set: ", outfit_info[0][3])
        print("       ~ Set Description: ", outfit_info[0][4])
        result.append(str("Outfit Name: " + outfit_info[0][0] + "\n       ~ Description: " + outfit_info[0][1] + "\n       ~ Rarity: " + outfit_info[0][2] + "\n       ~ Set: " + outfit_info[0][3] + "\n       ~ Set Description: " + outfit_info[0][4]))

        print("   ~ Glider Name: ", glider_info[0][0])
        print("       ~ Description: ", glider_info[0][1])
        print("       ~ Rarity: ", glider_info[0][2])
        print("       ~ Set: ", glider_info[0][3])
        print("       ~ Set Description: ", glider_info[0][4])
        result.append("Glider Name: " + glider_info[0][0] + "\n       ~ Description: " + glider_info[0][1] + "\n       ~ Rarity: " + glider_info[0][2] + "\n       ~ Set: " + glider_info[0][3] + "\n       ~ Set Description: " + glider_info[0][4])

        print("   ~ Pickaxe Name: ", pickaxe_info[0][0])
        print("       ~ Description: ", pickaxe_info[0][1])
        print("       ~ Rarity: ", pickaxe_info[0][2])
        print("       ~ Set: ", pickaxe_info[0][3])
        print("       ~ Set Description: ", pickaxe_info[0][4])
        result.append("Pickaxe Name: " + pickaxe_info[0][0] + "\n       ~ Description: " + pickaxe_info[0][1] + "\n       ~ Rarity: " + pickaxe_info[0][2] + "\n       ~ Set: " + pickaxe_info[0][3] + "\n       ~ Set Description: " + pickaxe_info[0][4])

        print("   ~ Back Bling Name: ", backbling_info[0][0])
        print("       ~ Description: ", backbling_info[0][1])
        print("       ~ Rarity: ", backbling_info[0][2])
        print("       ~ Set: ", backbling_info[0][3])
        print("       ~ Set Description: ", backbling_info[0][4])
        print("   ~ Contrail Name: ", contrail_info[0][0])
        print("       ~ Description: ", contrail_info[0][1])
        print("       ~ Rarity: ", contrail_info[0][2])
        print("       ~ Set: ", contrail_info[0][3])
        print("       ~ Set Description: ", contrail_info[0][4])
        result.append("Back Bling Name: " + backbling_info[0][0] + "\n       ~ Description: " + backbling_info[0][1] + "\n       ~ Rarity: " + backbling_info[0][2] + "\n       ~ Set: " + backbling_info[0][3] + "\n       ~ Set Description: " + backbling_info[0][4])

        print("   ~~~~~~~ Wins ~~~~~~~")
        print("      ~ Solo Wins: ", self.combo.getSoloWins())
        print("      ~ Duo Wins: ", self.combo.getDuoWins())
        print("      ~ Trio Wins: ", self.combo.getTrioWins())
        print("      ~ Squad Wins: ", self.combo.getSquadWins())
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        result.append("\n   ~~~~~~~ Wins ~~~~~~~" + "\n      ~ Solo Wins: " + str(self.combo.getSoloWins()) + "\n      ~ Duo Wins: " + str(self.combo.getDuoWins()) + "\n      ~ Trio Wins: " + str(self.combo.getTrioWins()) + "\n      ~ Squad Wins: " + str(self.combo.getSquadWins()) + "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        return result