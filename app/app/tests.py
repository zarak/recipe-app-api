from django.test import TestCase

from app.calc import add
from app.calc import subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_substract_numbers(self):
        """Test that two numbers are subtracted"""
        self.assertEqual(subtract(5, 11), 6)
