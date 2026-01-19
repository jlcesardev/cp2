import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):

    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

    def test_convert_string_float_with_trailing_dot(self):
        self.assertEqual(4.0, util.convert_to_number("4."))

    def test_convert_string_float_without_leading_zero(self):
        self.assertEqual(0.5, util.convert_to_number(".5"))

    def test_convert_string_with_spaces(self):
        self.assertEqual(4, util.convert_to_number(" 4 "))

    def test_convert_string_float_with_spaces(self):
        self.assertEqual(4.5, util.convert_to_number(" 4.5 "))
    
    def test_convert_to_number_unreachable_exception_branch(self):
        # Forzamos un tipo que rompa la conversión interna
        self.assertRaises(TypeError, util.convert_to_number, [])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

