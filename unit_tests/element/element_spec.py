import unittest

from src.element import validator
from src.element.element import Element
from src.element.element_exception import ElementException


class WhenCreatingElement(unittest.TestCase):

    def test_is_immutable(self):
        immutable_element = Element(3)
        self.assertEqual(True, immutable_element.is_immutable)
        self.assertEqual(3, immutable_element.value)
        self.assertEqual([3], immutable_element.possible_values)

    def test_is_mutable(self):
        mutable_element = Element(0)
        self.assertEqual(False,  mutable_element.is_immutable)
        self.assertEqual(validator.cleared, mutable_element.value)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], mutable_element.possible_values)

    def test_raises_ElementException_when_out_of_bounds(self):
        with self.assertRaises(ElementException):
            Element(-1)
        with self.assertRaises(ElementException):
            Element(10)
        with self.assertRaises(ElementException):
            Element(None)


class WhenTryNextPossibleValue(unittest.TestCase):

    def test_is_mutable(self):
        mutable_element = Element(0)
        value = mutable_element.next_possible_value()
        mutable_element.set_value(value)
        self.assertEqual(1, mutable_element.value)
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9], mutable_element.possible_values)
        self.assertEqual(False, mutable_element.is_immutable)

    def test_is_immutable(self):
        immutable_element = Element(3)
        with self.assertRaises(ElementException):
            immutable_element.next_possible_value()

    def test_no_more_possible_values(self):
        mutable_element = Element(0)
        mutable_element.possible_values = []
        with self.assertRaises(ElementException):
            mutable_element.next_possible_value()


class WhenClearValue(unittest.TestCase):

    def test_is_mutable(self):
        mutable_element = Element(0)
        mutable_element.set_value(3)
        mutable_element.possible_values = []
        mutable_element.clear_value()
        self.assertEqual(validator.cleared, mutable_element.value)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], mutable_element.possible_values)
        self.assertEqual(False, mutable_element.is_immutable)

    def test_is_immutable(self):
        immutable_element = Element(3)
        with self.assertRaises(ElementException):
            immutable_element.clear_value()

    def test_no_more_possible_values(self):
        mutable_element = Element(0)
        mutable_element.next_possible_value()
        with self.assertRaises(ElementException):
            mutable_element.clear_value()


class WhenSettingValue(unittest.TestCase):

    def test_is_mutable(self):
        mutable_element = Element(0)
        mutable_element.set_value(3)
        self.assertEqual(mutable_element.possible_values, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(mutable_element.value, 3)
        self.assertEqual(mutable_element.is_immutable, False)

    def test_is_immutable(self):
        immutable_element = Element(3)
        with self.assertRaises(ElementException):
            immutable_element.set_value(3)

if __name__ == '__main__':
    loader = unittest.TestLoader()
