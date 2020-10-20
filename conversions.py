Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Assignment - Conversions
	Dave Soto"""

import decimal


def convertCelsiusToKelvin(degrees):
    """Performs arithmetic to convert given temperature in degrees celsius to
    degrees Kelvin.
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) + decimal.Decimal('273.15'))
    return float(convert)


def convertCelsiusToFahrenheit(degrees):
    """Performs arithmetic to convert given temperature in degrees Celsius to
    degrees Fahrenheit.
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) / decimal.Decimal('5') * 9) + 32
    return float(convert)


def convertFahrenheitToCelsius(degrees):
    """Performs arithmetic to convert given temperature in degrees Fahrenheit to
    degrees Celsius.
    """
    degrees = str(degrees)
    convert = ((decimal.Decimal(degrees) - 32) * 5) / decimal.Decimal('9')
    return float(convert)


def convertFahrenheitToKelvin(degrees):
    """Perfroms arithmetic to convert given temperature in degrees Fahrenheit to
    degrees Kelvin.
    """
    
    degrees = str(degrees)
    convert = (((decimal.Decimal(degrees) + decimal.Decimal('459.67')) * 5) /
               decimal.Decimal('9'))
    return float(convert)


def convertKelvinToCelsius(degrees):
    """Performs arithmetic to convert given temperature in degrees Kelvin to
    degrees Celsius.
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) - decimal.Decimal('273.15'))
    return float(convert)


def convertKelvinToFahrenheit(degrees):
    """Performs artimethic to convert given temperature in degrees Kelvin to
    degrees Fahrenheit.
    """
    degrees = str(degrees)
    convert = (((decimal.Decimal(degrees) * 9) / decimal.Decimal('5'))
               - decimal.Decimal('459.67'))
    return float(convert)

