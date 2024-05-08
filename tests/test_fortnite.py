import unittest
from Combination import Combination


class CombinationTest(unittest.TestCase):
    def test_comboName(self):
        combo = Combination()
        combo.setName('Test')
        self.assertEqual(combo.getName(), 'Test')

    def test_comboOutfit(self):
        combo = Combination()
        combo.setOutfit('CID_Creative_Mannequin_M_Default')
        self.assertEqual(combo.getOutfit(), 'CID_Creative_Mannequin_M_Default')

    def test_comboPickaxe(self):
        combo = Combination()
        combo.setPickaxe()
        self.assertEqual(combo.getPickaxe(), 'DefaultPickaxe')




if __name__ == '__main__':
    unittest.main()
