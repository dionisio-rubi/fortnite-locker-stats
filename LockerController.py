from Locker import Locker
from Combination import Combination
from LockerView import LockerView
class LockerController:
    """Locker Controller Class"""

    def __init__(self, locker: Locker, lockerView: LockerView):
        self.lockerModel = locker
        self.lockerView = lockerView

    def getLockeritems(self):
        """Returns the locker"""
        print(self.lockerModel.getLocker())
        print(self.lockerView.displayLocker(self.lockerModel.getLocker()))
        return self.lockerView.displayLocker(self.lockerModel.getLocker())

    def addNewCombo(self, combo: Combination):
        """Adds a combo to the locker class"""
        self.lockerModel.addCombo(combo)