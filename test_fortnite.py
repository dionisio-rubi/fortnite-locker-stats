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

class FetchTest(unittest.TestCase):
    def setUp(self):
        self.info = Fetch()

    def test_fetchOutfitNames(self):
        self.assertNotEqual(self.info.printOutfitNames(), [])

    def test_fetchPickaxeNames(self):
        self.assertNotEqual(self.info.printPickaxeNames(), [])

    def test_fetchContrailNames(self):
        self.assertNotEqual(self.info.printContrailNames(), [])

    def test_fetchBackblings(self):
        self.assertNotEqual(self.info.printBackblings(), [])

    def test_fetchGliderNames(self):
        self.assertNotEqual(self.info.printGliderNames(), [])

    def test_getFortnite(self):
        self.assertNotEqual(self.info.getFortnite(), [])

class CombinationViewTest(unittest.TestCase):
    def setUp(self):
        self.view = CombinationView()

    def test_comboView(self):
        self.assertNotEqual(self.view.printComboNames(), [])

    def test_comboInformation(self):
        self.assertNotEqual(self.view.printComboInformation(), [])

class LockerTest(unittest.TestCase):
    def setUp(self):
        self.locker = Locker()

    def test_locker(self):
        self.assertNotEqual(self.locker.getLocker(), [])
        self.assertEqual(self.locker.getLockerName(), ['demo2', 'tkinter-test', 'tkinter-demo', 'tkinter-demo2', 'defauilt test', 'tkinter-demo3', 'tkinter-demo4', 'tkinter-demo5', 'demo'])
        self.assertEqual(self.locker.addCombo(Combination()), None)

class LockerViewTest(unittest.TestCase):
    def setUp(self):
        self.view = LockerView(CombinationView())

    def test_lockerView(self):
        self.assertEqual(self.view.displayLocker([]), [])
        self.assertEqual(self.view.displayLockerNames([]), [])

class LockerControllerTest(unittest.TestCase):
    def setUp(self):
        self.locker = Locker()
        self.view = LockerView(CombinationView())
        self.controller = LockerController(self.locker, self.view)

    def test_lockerController(self):
        self.assertNotEqual(self.controller.getLockeritems(), [])
        self.assertEqual(self.controller.getAllLockerNames(), ['demo2', 'tkinter-test', 'tkinter-demo', 'tkinter-demo2', 'defauilt test', 'tkinter-demo3', 'tkinter-demo4', 'tkinter-demo5', 'demo'])
        self.assertNotEqual(self.controller.getLockerCombos(), [])

class CombinationTest(unittest.TestCase):
    def setUp(self):
        self.combo = Combination()

    def test_combination(self):
        self.assertNotEqual(self.combo.getName(), 'default')
        self.assertEqual(self.combo.getOutfit(), [('Recruit', 'Standard issue combatant outfit.', 'Common', 'N/A', 'N/A')])
        self.assertEqual(self.combo.updateSoloWins(1), None)
        self.assertEqual(self.combo.updateDuoWins(1), None)
        self.assertEqual(self.combo.updateTrioWins(1), None)
        self.assertEqual(self.combo.updateSquadWins(1), None)
        self.assertEqual(self.combo.setName('Test'), None)
        self.assertEqual(self.combo.setOutfit('Test'), None)
        self.assertEqual(self.combo.setPickaxe('Test'), None)
        self.assertEqual(self.combo.setGlider('Test'), None)
        self.assertEqual(self.combo.setContrail('Test'), None)
        self.assertEqual(self.combo.setBackbling('Test'), None)

class CombinationControllerTest(unittest.TestCase):
    def setUp(self):
        self.combo = Combination()
        self.view = CombinationView()
        self.controller = CombinationController(self.combo, self.view)

    def test_combinationController(self):
        self.assertNotEqual(self.controller.getCombinationName(), 'default')
        self.assertEqual(self.controller.setComboName('Test'), None)
        self.assertEqual(self.controller.setComboOutfit('Test'), None)
        self.assertEqual(self.controller.setComboPickaxe('Test'), None)
        self.assertEqual(self.controller.setComboGlider('Test'), None)
        self.assertEqual(self.controller.setComboContrail('Test'), None)
        self.assertEqual(self.controller.setComboBackbling('Test'), None)
        self.assertEqual(self.controller.updateSolo(1), None)
        self.assertEqual(self.controller.updateDuo(1), None)
        self.assertEqual(self.controller.updateTrio(1), None)
        self.assertEqual(self.controller.updateSquad(1), None)
        self.assertEqual(self.controller.getOutfitInfo(), [])

class ViewAllTest(unittest.TestCase):
    def setUp(self):
        self.info = Fetch()
        self.viewAll = ViewAll(self.info.printOutfitNames(), self.info.printPickaxeNames(), self.info.printContrailNames(), self.info.printBackblings(), self.info.printGliderNames())

    def test_viewAll(self):
        self.assertEqual(self.viewAll.start(), None)

    def test_seeFrame(self):
        self.assertNotEqual(self.viewAll.seeFrame(), [])

    def test_onSelect(self):
        self.assertEqual(self.viewAll.on_select('demo2', 'CID_349_Athena_Commando_M_Banana', 'BID_STWHeroNoDefaultBackpack', 'DefaultContrail', 'solo_umbrella', 'DefaultPickaxe'), None)

if __name__ == '__main__':
    unittest.main()