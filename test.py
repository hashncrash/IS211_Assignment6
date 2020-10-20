#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Assignment - Tests
	Dave Soto
"""

import conversions
import unittest


class KnownValues(unittest.TestCase):
    """Testing the conversion function in conversions.py"""
    knownvals = ((180.00, 300.00, 543.15),
                 (200.00, 375.00, 473.15),
                 (98.00, 248.00, 299.25),
                 (0.00, 32.00, 273.15),
                 (-273.15, -459.67, 0.00))

    def testCelsiustoKelvin(self):
        """Tests the above functionTests that the convertCelsiusToKelvin
	to see if conversion works.
        """
        for val in self.knownvals:
            c = val[0]
            k = val[2]
            expect = conversions.convertCelsiusToKelvin(c)
            self.assertEqual(expect, k, msg=('{} degrees K '
                                             'is not equal to {}'
                                             ' degrees K.').format(c, k))

    def testCelsiustoFahrenheit(self):
        """test convertCelsiusToFahrenheit function returns the
        correct value.
        """
        for val in self.knownvals:
            c = val[0]
            f = val[1]
            expect = conversions.convertCelsiusToFahrenheit(c)
            self.assertEqual(expect, f, msg=('{} degrees F '
                                             'is not equal to {}'
                                             ' degrees F.').format(c, f))

    def testFahrenheitToCelsius(self):
        """Tests that the convertFahrenheitToCelsius function.
        """
        for val in self.knownvals:
            f = val[1]
            c = val[0]
            expect = conversions.convertFahrenheitToCelsius(f)
            self.assertEqual(expect, c, msg=('{} degrees C '
                                             'is not equal to {}'
                                             ' degrees C.').format(f, c))

    def testFahrenheitToKelvin(self):
        """Tests the convertFahrenheitToKelvin function returns the
        correct value.
        """
        for val in self.knownvals:
            f = val[1]
            k = val[2]
            expect = conversions.convertFahrenheitToKelvin(f)
            self.assertEqual(expect, k, msg=('{} degrees K '
                                             'is not equal to {}'
                                             ' degrees K.').format(f, k))

    def testKelvinToCelsius(self):
        """Tests the convertKelvinToCelsius function returns the
        correct vaule.
        """
        for val in self.knownvals:
            k = val[2]
            c = val[0]
            expect = conversions.convertKelvinToCelsius(k)
            self.assertEqual(expect, c, msg=('{} degrees C '
                                             'is not equal to {}'
                                             ' degrees C.').format(k, c))

    def testKelvinToFahrenheit(self):
        """Tests that the convertKelvinToFahrenheit function
        """
        for val in self.knownvals:
            k = val[2]
            f = val[1]
            expect = conversions.convertKelvinToFahrenheit(k)
            self.assertEqual(expect, f, msg=('{} degrees F '
                                             ' is not equal to {}'
                                             ' degrees F.').format(k, f))


if __name__ == '__main__':
    unittest.main()
