from PyQt5 import QtWidgets
from plotFunction import validate
import unittest

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.app = QtWidgets.QApplication([])

    def test_validate_happy(self):
        self.assertTrue(validate("x+1","3","0"))

    def test_validate_empty_min_field(self):
        self.assertFalse(validate("x+1","3",""))

    def test_validate_wrong_max_input(self):
        self.assertFalse(validate("x+1","aa","0"))

    def test_validate_min_greater_than_max(self):
        self.assertFalse(validate("-x","0","3"))

if __name__ == "__main__":
    unittest.main()