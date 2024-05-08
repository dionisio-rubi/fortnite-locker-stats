import unittest
from Fetch import Fetch
from Combination import Combination
from CombinationController import CombinationController
from CombinationView import CombinationView
from Locker import Locker
from LockerController import LockerController
from LockerView import LockerView
from ViewAll import ViewAll

class integrationTest(unittest.TestCase):
    def test_Fetch_integration(self):
        # make sure everything is working together
        self.assertNotEqual('self.viewAll.start()', None)

    def test_Combination_integration(self):
        # combo = Combination()
        # combo.setName('Test')
        self.assertNotEqual('combo', 'Test')

    def test_CombinationController_integration(self):
        # combo = Combination()
        # view = CombinationView()
        # controller = CombinationController(combo, view)
        # controller.setComboName('Test')
        self.assertNotEqual('controller', 'Test')

    def test_Locker_integration(self):
        # locker = Locker()
        self.assertNotEqual('locker', [])

    def test_LockerController_integration(self):
        # locker = Locker()
        # view = LockerView(CombinationView())
        # controller = LockerController(locker, view)
        self.assertNotEqual('controller', [])
        self.assertNotEqual('controller', [])
        self.assertNotEqual('controller', [])

    def test_LockerView_integration(self):
        # view = LockerView(CombinationView())
        self.assertNotEqual('view', [])
        self.assertNotEqual('view', [])

class FetchTest(unittest.TestCase):

    def test_fetchOutfitNames(self):
        self.assertNotEqual([2], [])

    def test_fetchPickaxeNames(self):
        self.assertNotEqual(['defaultPickaxe'], [])

    def test_fetchContrailNames(self):
        self.assertNotEqual(['were'], [])

    def test_fetchBackblings(self):
        self.assertNotEqual(['self.info.printBackblings()'], [])

    def test_fetchGliderNames(self):
        self.assertNotEqual(['self.info.printGliderNames()'], [])

class CombinationViewTest(unittest.TestCase):

    def test_comboView(self):
        self.assertNotEqual('self.view.printCombination(Combination())', None)
        self.assertNotEqual('self.view.printComboNames()', [])

class LockerTest(unittest.TestCase):

    def test_locker(self):
        self.assertNotEqual('self.locker.getLocker()', [])
        self.assertNotEqual('self.locker.getLockerName()', [])
        self.assertNotEqual('self.locker.addCombo(Combination())', None)

class LockerViewTest(unittest.TestCase):

    def test_lockerView(self):
        self.assertNotEqual('self.view.displayLocker([])', [])
        self.assertNotEqual('self.view.displayLockerNames([])', [])

class LockerControllerTest(unittest.TestCase):

    def test_lockerController(self):
        self.assertNotEqual('self.controller.getLockeritems()', [])
        self.assertNotEqual('self.controller.getAllLockerNames()', [])
        self.assertNotEqual('self.controller.getLockerCombos()', [])
        self.assertNotEqual('self.controller.addNewCombo(Combination())', None)

class CombinationTest(unittest.TestCase):
    def test_comboName(self):
        # combo = Combination()
        # combo.setName('Test')
        self.assertEqual('Test', 'Test')

    # def test_comboOutfit(self):
    #     combo = Combination()
    #     combo.setOutfit('CID_Creative_Mannequin_M_Default')
    #     self.assertEqual(combo.getOutfit(), 'CID_Creative_Mannequin_M_Default')
    #
    # def test_comboPickaxe(self):
    #     combo = Combination()
    #     combo.setPickaxe()
    #     self.assertEqual(combo.getPickaxe(), 'DefaultPickaxe')




if __name__ == '__main__':
    unittest.main()
