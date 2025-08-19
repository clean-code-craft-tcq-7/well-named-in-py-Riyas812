import unittest
from color_map import get_color_pair_number, get_color_from_pair_number
from report import get_color_code_manual_lines

class TestColorMapping(unittest.TestCase):
    def test_pair_number_and_colors(self):
        # Test known mappings
        self.assertEqual(get_color_pair_number('White', 'Blue'), 1)
        self.assertEqual(get_color_pair_number('Red', 'Slate'), 10)
        self.assertEqual(get_color_pair_number('Violet', 'Slate'), 25)
        
        self.assertEqual(get_color_from_pair_number(1), ('White', 'Blue'))
        self.assertEqual(get_color_from_pair_number(10), ('Red', 'Slate'))
        self.assertEqual(get_color_from_pair_number(25), ('Violet', 'Slate'))
        
        # Test invalid inputs raise exceptions
        with self.assertRaises(ValueError):
            get_color_pair_number('Pink', 'Blue')
        with self.assertRaises(ValueError):
            get_color_from_pair_number(26)

class TestReport(unittest.TestCase):
    def test_report_format(self):
        lines = get_color_code_manual_lines()
        self.assertTrue(lines[0].startswith("Pair Number"))
        self.assertTrue(lines[2].startswith("1"))
        self.assertIn("White", lines[2])
        self.assertIn("Blue", lines[2])
        
        # Check last line for pair 25
        self.assertTrue(lines[-1].startswith("25"))
        self.assertIn("Violet", lines[-1])
        self.assertIn("Slate", lines[-1])

if __name__ == '__main__':
    unittest.main()
