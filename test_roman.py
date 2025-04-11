import unittest
from roman import roman_to_int

class TestRomanConverter(unittest.TestCase):
    def test_single_letters(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
    
    def test_repeated_letters(self):
        self.assertEqual(roman_to_int("II"), 2)
        self.assertEqual(roman_to_int("XX"), 20)
    
    def test_subtractive_notation(self):
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
    
    def test_mixed_notation(self):
        self.assertEqual(roman_to_int("XIV"), 14)  # 10 + (5-1)
        self.assertEqual(roman_to_int("MCMXC"), 1990)  # 1000 + (1000-100) + (100-10)
    
    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            roman_to_int("Z")
        with self.assertRaises(ValueError):
            roman_to_int("XIZ")
    
    def test_empty_input(self):
        self.assertEqual(roman_to_int(""), 0)

if __name__ == "__main__":
    unittest.main()