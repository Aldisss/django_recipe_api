from django.test import TestCase

from .calc import add

""""test command
docker-compose run app sh -c "python manage.py test"
"""

class CalcTest(TestCase):
    def test_add_numbers(self):
        """adding 2 numbers"""
        self.assertEqual(add(3, 8), 11)
