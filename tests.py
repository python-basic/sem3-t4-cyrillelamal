import unittest as ut
import math
import random


from factorial import fac


class TestFactorial(ut.TestCase):
    def setUp(self):
        self.end = 100
        self.unexpected_values = ['(lambda: exit())()', float(5), lambda x: x*x]

    def tearDown(self):
        pass

    def test_positive(self):
        for i in range(random.randint(1, self.end)):
            self.assertEqual(math.factorial(i), fac(i))

    def test_zero(self):
        self.assertEqual(1, fac(0))

    def test_negative(self):
        try:
            self.assertRaises(ValueError, fac(-1))
        except ValueError:
            pass

    def test_int_conversion(self):
        for i in range(random.randint(1, self.end)):
            good_value = math.factorial(i)
            i = str(i)
            self.assertEqual(good_value, fac(i))

    def test_unexpeted_types(self):
        for uv in self.unexpected_values:
            try:
                self.assertRaises(ValueError, fac(float()))
            except:
                pass


if __name__ == '__main__':
    ut.main()
