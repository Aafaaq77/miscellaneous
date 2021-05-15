# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:16:42 2021

@author: Aafaaq
"""

from abc import ABC, abstractmethod

class Calc(ABC):
    def __init__(self, x=4, y=6):
        self._x = x
        self._y = y
        
        
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    
    
    def show_x_y(self):
        print(self._x, self._y)
    
    @abstractmethod
    def add_x_y(self):
        pass
    
    
class Real_calc(Calc):
    def __init__(self, z):
        super().__init__()
        self._z = z
        
    
    @property
    def z(self):
        return self._z
        
    def add_x_y(self):
        return self._x + self._y
        
    def show_z(self):
        print(self._z)
        
my_nums = Real_calc(3)        
