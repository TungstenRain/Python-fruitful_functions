"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 6: Fruitful Functions in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""
def is_power(a, b):
    """
        Determine if a number, a, is a power of b
        if a is divisible by b and a/b

        a: integer
        b: integer
        return: True if a is a power of b, False otherwise
    """
    if a % b == 0:
        if a == b:
            return True
        else:
            return is_power(a/b, b)
    return False

def user_prompt():
    """
        Prompt the user for input to check the is_power function.
    """
    print("We're going to check the is_power function.\n")
    a = int(input("Enter an integer for a: "))
    b = int(input("Enter an integer for b: "))
    if is_power(a, b):
        print("Integer a: " + str(a) + " is a power of b: " + str(b) + ".")
    else:
        print("Integer a: " + str(a) + " is not a power of b: " + str(b) + ".")

user_prompt()