# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:51:29 2020

@author: user
"""

def add(x,y):
    """
    
    Retuns x + y.

    Parameters
    ----------
    x : TYPE int
        DESCRIPTION.
    y : TYPE int
        DESCRIPTION.

    Returns int sum of x and y
    -------

    """

    return x+y    

def expon(x):
    """
    returns sqare...

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return x**2

def dplay(msg):
    print(msg)

def threeparam (a,b,c,d=5,e=7):
    print(a+b+c)
    print(d)
    print(e)
    print(a+b+c+d+e)
    
def funca(x):
    return x // 2

def funcb(x):
    return x*4

inta = int(input('Please enter a number:'))
ansint = funcb(funca(inta))
print (ansint)
