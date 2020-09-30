"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 6: Fruitful Functions in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""
def first(word):
    """
        Take a string and return the first character

        word: string
        return: first character from word
    """
    return word[0]

def last(word):
    """
        Take a string and return the last character

        word: string
        return: last character from word
    """
    return word[-1]

def middle(word):
    """
        Take a string and return all but the first and last characters

        word: string
        return: all but the first and last characters
    """
    return word[1:-1]

def is_palindrome(word):
    """
        Determine if a string is a palindrome
        Note: uppercase and lowercase letters are not identical and will not match

        word: string
        return: True if the word is a palindrome, false otherwise
    """
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome("bob"))
print(is_palindrome("Bob"))
print(is_palindrome("Frank"))
print(is_palindrome("barnanrab"))
print(is_palindrome("redivider"))
print(is_palindrome("supply"))