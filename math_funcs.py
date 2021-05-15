# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 23:03:20 2021

@author: Aafaaq
"""
import numpy as np
import math


def euler_taylor(x, n):
    '''
    args: x, n (number of taylor series)
    returns: value of euler number at x after n approximations 
    using taylor
    '''
    taylor_series = [((x**i)/math.factorial(i)) for i in range(n+1)]
    exp_value = np.sum(taylor_series)
    rest = abs(exp_value - math.exp(x))
    return {'taylorSeries': taylor_series, 
            'remainder': rest,
            'Valueat_x': exp_value}


def harmonic_series_sum(n):
    '''
    returns the sum of first n members of a harmonic series
    '''
    ns_arr = np.arange(1, n)
    harmonic = 1/ns_arr
    return np.sum(harmonic)


def birthday_probability(people):
    '''
    probality of all people people born on a different day,
    given the number of people
    args: number of people
    returns: probablity (in %) of all people having a birthday 
    on different days.
    '''
    birthdays = np.full(people, 365)
    step_1 = np.arange(365, 365-people, -1)/birthdays
    probabs = step_1.cumprod()
    return probabs[people - 1] * 100
    
def expected_value(num_rolls):
    rolls_array = np.random.randint(1, 7, num_rolls)
    return {'mean': np.mean(rolls_array), 
            'median': np.median(rolls_array)}



def f1_x(x):
    return 3 * np.sqrt(x+2)

def f2_x(x):
    return (x/5)-(52/5)

