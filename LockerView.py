class LockerView:
    """View for the Locker class"""

    def __init__(self, comboview):
        self.comboView = comboview

    def displayLocker(self, locker):
        """Displays the locker"""
        print("Locker:")
        for combo in locker.getLocker():
            self.comboView.displayCombo(combo)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")