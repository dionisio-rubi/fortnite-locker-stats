from Locker import Locker
class LockerController:
    """Locker Controller Class"""

    def __init__(self):
        self.lockerModel = Locker()

    def getLocker(self):
        """Returns the locker"""
        return self.lockerModel.getLocker()

    def addCombo(self, combo):
        """Adds a combo to the locker class"""
        self.lockerModel.addCombo(combo)