from Combination import Combination
from CombinationView import CombinationView

class CombinationController:
    """The controller for the combination class"""

    def __init__(self, combination: Combination, view: CombinationView):
        self.comboModel = combination
        self.comboview = view

    def setCombination(self, combination: Combination):
        self.comboModel = combination

    def getCombinationName(self):
        """Returns the name of the combination, calls upon combination class"""
        return self.comboModel.getName()

    def setComboName(self, name):
        """Set the name of the combo, calls upon combination class"""
        self.comboModel.setName(name)

    def setComboOutfit(self, outfit='CID_Creative_Mannequin_M_Default'):
        """Set the outfit of the combo, calls upon combination class"""
        self.comboModel.setOutfit(outfit)
    def setComboPickaxe(self, pickaxe='DefaultPickaxe'):
        """Set the pickaxe of the combo, calls upon combination class"""
        self.comboModel.setPickaxe(pickaxe)

    def setComboGlider(self, glider='DefaultGlider'):
        """Set the glider of the combo, calls upon combination class"""
        self.comboModel.setGlider(glider)

    def setComboContrail(self, contrail='DefaultContrail'):
        """Set the contrail of the combo, calls upon combination class"""
        self.comboModel.setContrail(contrail)

    def setComboBackbling(self, backbling='BID_STWHeroNoDefaultBackpack'):
        """Set the backbling of the combo, calls upon combination class"""
        self.comboModel.setBackbling(backbling)

    def updateSolo(self, newWins):
        """Update the solo wins count of the combo"""
        self.comboModel.updateSoloWins(newWins)

    def updateDuo(self, newWins):
        """Update the duo wins count of the combo"""
        self.comboModel.updateDuoWins(newWins)

    def updateTrio(self, newWins):
        """Update the trio wins count of the combo"""
        self.comboModel.updateTrioWins(newWins)

    def updateSquad(self, newWins):
        """Update the squad wins count of the combo"""
        self.comboModel.updateSquadWins(newWins)

    def getOutfitInfo(self):
        """returns all the info about the outfit in the form of a list"""
        return self.comboModel.getOutfit()

    def getGliderInfo(self):
        """returns all the info about the glider in the form of a list"""
        return self.comboModel.getGlider()

    def getContrailInfo(self):
        """returns all the info about the contrail in the form of a list"""
        return self.comboModel.getContrail()

    def getBackblingInfo(self):
        """returns all the info about the backbling in the form of a list"""
        return self.comboModel.getBackbling()

    def getPickaxeInfo(self):
        """returns all the info about the pickaxe in the form of a list"""
        return self.comboModel.getPickaxe()

    def getSolo(self):
        """Get the solo wins count"""
        return self.comboModel.getSoloWins()

    def getDuo(self):
        """Get the duo wins count"""
        return self.comboModel.getDuoWins()

    def getTrio(self):
        """Get the trio wins count"""
        return self.comboModel.getTrioWins()

    def getSquad(self):
        """Get the squad wins count"""
        return self.comboModel.getSquadWins()

    def getOutfit_ID(self):
        """returns outfit id"""
        return self.comboModel.getOutfitID()

    def getPickaxe_ID(self):
        """returns pickaxe id"""
        return self.comboModel.getPickaxeID()

    def getGlider_ID(self):
        """returns glider id"""
        return self.comboModel.getGliderID()

    def getContrail_ID(self):
        """returns contrail id"""
        return self.comboModel.getContrailID()

    def getBackbling_ID(self):
        """returns backbling id"""
        return self.comboModel.getBackblingID()

    def updateView(self):
        """update view to print everything"""
        self.comboview.printCombination(self.comboModel)