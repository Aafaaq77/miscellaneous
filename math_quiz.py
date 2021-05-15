# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:44:13 2021

@author: Aafaaq
"""
import random


def addition_quiz(lower_range=0, upper_range=500):
    '''
    A small quiz game of 10 addition questions
    args: int lower_range for questions, default = 0 
          int upper_range for questions, default = 500 
    returns: None
    '''
    results_list = []
    
    for quiz in range(1, 11):
        rand_num_a = random.randint(0, 500)
        rand_num_b = random.randint(0, 500)
        guess = input(f"Aufgabe{quiz}: {rand_num_a} + {rand_num_b} = ")
        if int(guess) == rand_num_a + rand_num_b:
            print("prima")
        else:
            print('leider falsch')
        
        results_list.append(int(guess) == rand_num_a + rand_num_b)
        
    richtig = results_list.count(True)
    print(f"{richtig} von 10 Aufgaben ({(richtig/10)*100} %) richtig.")

