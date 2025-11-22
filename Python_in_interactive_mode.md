```console
Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

# Prints a string
>>>print("Python")

# Prints a string with a leading tab
>>>print("\tPython")

# Prints a string interspersed with new line escape sequences
>>>print("Languages:\nPython\nC\nJavaScript")

# Prints a string interspersed with new line and tab escape sequences
>>>print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Assigns string with trailing space to a variable
>>>favorite_language = 'python '

# Prints out variable's value
>>>favorite_language

# Invokes rstrip() method on variable to strip away trailing whitespace
>>>favorite_language.rstrip()

# Prints out variable's value 
>>>favorite_language

# Strips away trailing whitespace from variable and saves resulting string to the same variable's new value
>>>favorite_language = favorite_language.rstrip()

# Prints out variable's value
>>>favorite_language

# Assigns string with leading and trailing whitespace to variable
>>>favorite_language = ' python '

# Prints string with trailing whitespace stripped away
>>>favorite_language.rstrip()

# Prints string with leading whitespace stripped away
>>>favorite_language.lstrip()

# Prints string with both leading and trailing whitespace stripped away
>>>favorite_language.strip()

# Addition
>>>2 + 3
5

# Subtraction
>>>3 - 2
1

# Multiplication
>>>2 * 3
6

# Division (result is expressed as a float)
>>>3 / 2
1.5

# Exponents ( 3^2 = 9 )
>>>3 ** 2
9

# Exponents ( 3^3 = 27 )
>>>3 ** 3
27

# Exponents ( 10^6 = 1000000 )
>>>10 ** 6
1000000

# Order of Operations example (PEMDAS) Multiplication before Addition
>>>2 + 3*4
14

# Order of Operations example that incorporates parentheses for specifying the order of operations
>>>(2 + 3) * 4
20

# Math with Floats
>>>0.1 + 0.1
0.2

>>>0.2 + 0.2
0.4

>>>2 * 0.1
0.2

>>>2 * 0.2
0.4

>>>0.2 + 0.1
0.30000000000000004

>>>3 * 0.1
0.30000000000000004

>>>4/2
2.0

>>>1 + 2.0
3.0

>>>2 * 3.0
6.0

>>>3.0 ** 2
9.0

>>>universe_age = 14_000_000_000

>>>print(universe_age)
14000000000

# Multiple assignment example
>>>x, y, z = 0, 0, 0

>>>print(5 + 3)
8

>>>print(11 - 3)
8

>>>print(2 * 4)
8

>>>print(16 / 2)
8.0

# Reveals your favorite number using an f-string
>>>favorite_number = 21
>>>print(f"My favorite number is: {favorite_number}" )
My favorite number is: 21

# Finding the length of a list
>>>cars = ['bmw', 'audi', 'toyota', 'subaru']
>>>len(cars)
4
```
