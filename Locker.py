class Locker:
    """Represents a user's Fortnite Locker"""
    def __init__(self):
        self.locker = []

    def getLocker(self):
        """Returns the locker"""
        return self.locker

    def addCombo(self, combo):
        """Adds a combo to the locker"""
        self.locker.append(combo)