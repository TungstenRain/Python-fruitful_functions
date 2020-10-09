"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 6: Fruitful Functions in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""

def gcd(a, b):
    # if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def user_prompt():
    """
        Prompt the user for input to check the is_power function.
    """
    print("We're going to find the greatest common divisor for two numbers.\n")
    a = int(input("Enter an integer for a: "))
    b = int(input("Enter an integer for b: "))
    print(gcd(a, b))

user_prompt()