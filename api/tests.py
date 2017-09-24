from django.test import TestCase

from .models import Rabbit

class RabbitTests(TestCase):
    def test_calculate_age_of_rabbit(self):
        r = Rabbit(birth_date='2016-03-01')
        self.assertEquals(1, r.age())
