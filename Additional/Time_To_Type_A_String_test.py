import unittest
from Time_To_Type_A_String import main

class MainTest(unittest.TestCase):
    def test_get_time(self):
        self.assertEqual(main('cba'),4)

    def test_get_time2(self):
        self.assertEqual(main('cbad'),7)

if __name__ == "__main__":
    unittest.main()