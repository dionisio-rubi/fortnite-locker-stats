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
    def setUp(self):
        self.info = Fetch()
        self.viewAll = ViewAll(self.info.printOutfitNames(), self.info.printPickaxeNames(), self.info.printContrailNames(), self.info.printBackblings(), self.info.printGliderNames())

    def test_Fetch_integration(self):
        # make sure everything is working together
        self.assertEqual(self.viewAll.start(), None)

    def test_Combination_integration(self):
        combo = Combination()
        combo.setName('Test')
        self.assertEqual(combo.getName(), 'Test')

    def test_CombinationController_integration(self):
        combo = Combination()
        view = CombinationView()
        controller = CombinationController(combo, view)
        controller.setComboName('Test')
        self.assertEqual(controller.getCombinationName(), 'Test')

    def test_Locker_integration(self):
        locker = Locker()
        self.assertNotEqual(locker.getLocker(), [])

    def test_LockerController_integration(self):
        locker = Locker()
        view = LockerView(CombinationView())
        controller = LockerController(locker, view)
        self.assertNotEqual(controller.getLockeritems(), [])
        self.assertNotEqual(controller.getAllLockerNames(), [])
        self.assertNotEqual(controller.getLockerCombos(), [])

    def test_LockerView_integration(self):
        view = LockerView(CombinationView())
        self.assertEqual(view.displayLocker([]), [])
        self.assertEqual(view.displayLockerNames([]), [])

    def test_ViewAll_integration(self):
        self.assertEqual(self.viewAll.start(), None)




if __name__ == '__main__':
    unittest.main()
