"""
Number System Conversions:
- Develop a Python script to convert numbers between hexadecimal, octal,
and decimal systems.

Unit Conversions:
Write Python functions to:

- Convert from feet to centimeters.
- Convert from centimeters to feet.
"""

# Input a number in decimal format
decimal_num = float(input("Enter a decimal number: "))

# Decimal to Hexadecimal
hexadecimal = hex(int(decimal_num))
print(f'Hexadecimal: {hexadecimal}')

# Decimal to Octal
octal = oct(int(decimal_num))
print(f'Octal: {octal}')

# Hexadecimal to Decimal
hex_input = input("Enter a hexadecimal number: ")
decimal_from_hex = int(hex_input, 16)
print(f'Decimal from Hexadecimal: {decimal_from_hex}')

# Octal to Decimal
octal_input = input("Enter an octal number: ")
decimal_from_octal = int(octal_input, 8)
print(f'Decimal from Octal: {decimal_from_octal}')

# Feet to Centimeters
feet = float(input("Enter length in feet: "))
centimeters = feet * 30.48
print("Centimeters:", centimeters)

# Centimeters to Feet
centimeters_input = float(input("Enter length in centimeters: "))
feet_from_cm = centimeters_input / 30.48
print("Feet:", feet_from_cm)
