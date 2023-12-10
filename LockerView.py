from CombinationView import CombinationView
# from LockerController import LockerController
class LockerView:
    """View for the Locker class"""

    def __init__(self, comboView: CombinationView):
        self.comboView = comboView

    def displayLocker(self, locker):
        """Displays the locker"""
        print("Locker:")
        for combo in locker:
            self.comboView.printCombination(combo)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")