import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc1
        self.assertFalse(loc1 == loc2)
        self.assertFalse(loc1 == "test")
        self.assertTrue(loc1 == Location("SLO", 35.3, -120.7))
        self.assertTrue(loc1 == loc3)

    def test_eq_call(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc1
        self.assertFalse(loc1.__eq__(loc2))
        self.assertFalse(loc1.__eq__("test"))
        self.assertTrue(loc1.__eq__(Location("SLO", 35.3, -120.7)))
        self.assertTrue(loc1.__eq__(loc3))



if __name__ == "__main__":
        unittest.main()
