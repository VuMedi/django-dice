"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from dice.tests.models import Choice


class DiceTest(TestCase):
    def setUp(self):
        self.number_of_tosses = 1000

    def close(self, number1, number2, percentage=0.1):
        """
        Test whether numbers are within some percentage
        """
        if number1 == number2:
            return True
        return abs(number1-number2) / float(max(number1, number2)) < percentage

    def test_coin(self):
        head = Choice.objects.create(key="coin", weight=1)
        tail = Choice.objects.create(key="coin", weight=1)

        head_count = 0
        tail_count = 0
        for i in range(self.number_of_tosses):
            toss = Choice.objects.pick("coin")
            if toss == head:
                head_count += 1
            elif toss == tail:
                tail_count += 1
            else:
                self.fail()

        self.assertEqual(self.number_of_tosses, head_count + tail_count)
        self.assertTrue(self.close(head_count, tail_count))

    def test_thirds(self):
        one_third = Choice.objects.create(key="third", weight=1)
        two_thirds = Choice.objects.create(key="third", weight=2)

        one_third_count = 0
        two_thirds_count = 0
        for i in range(self.number_of_tosses):
            toss = Choice.objects.pick("third")
            if toss == one_third:
                one_third_count += 1
            elif toss == two_thirds:
                two_thirds_count += 1
            else:
                self.fail()
        self.assertEqual(self.number_of_tosses, one_third_count + two_thirds_count)
        self.assertTrue(self.close(one_third_count * 2, two_thirds_count))

    def test_not_existing_key(self):
        with self.assertRaises(Exception):
            Choice.objects.pick("not_existing_key")


