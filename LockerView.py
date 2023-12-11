from CombinationView import CombinationView
# from LockerController import LockerController

class LockerView:
    """View for the Locker class"""

    def __init__(self, comboView: CombinationView):
        self.comboView = comboView

    def displayLocker(self, locker):
        """Displays the locker"""
        print("Locker:")
        res = []
        for combo in locker:
            res.append(self.comboView.printCombination(combo))
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(res)
        return res
