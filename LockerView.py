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

    def displayLockerNames(self, locker):
        """Displays only the name of the combination"""
        res = []
        for combo in range(len(locker)):
            print('[' + str(combo) + ']', self.comboView.printComboNames()[combo])
            res.append('[' + str(combo) + ']' + self.comboView.printComboNames()[combo])
        return res