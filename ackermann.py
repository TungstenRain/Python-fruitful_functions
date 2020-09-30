"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 6: Fruitful Functions in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""
def ack(m, n):
    """
        Evaluate the Ackermann function
                 | n+1                  if m = 0
        A(m,n) = { A(m - 1, 1)          if m > 0, and n = 0
                 | A(m-1, A(m, n - 1))  if m > 0, and n > 0
    
        m: integer
        n: integer
    """
    if m == 0:
        return n + 1
    elif (m > 0) and (n == 0):
        return ack(m - 1, 1)
    elif (m > 0) and (n > 0):
        return ack(m - 1, ack(m, n - 1))
    else:
        return 0

ackermann = ack(3,4)
print("Evaluating the Ackermann function for m= 3 and n= 4, A(m, n) = " + str(ackermann))