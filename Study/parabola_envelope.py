# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 01:00:20 2018

@author: toi1-
"""
from turtle import *

#放物線の包絡線を描く関数
#parabola_recursion(始点, 単位長, 分割数)
def parabola_recursion(start, length, number):
    for i in range(number + 1):
        penup()
        setpos(start[0] + length * i/number, start[1])
        pendown()
        setpos(start[0], start[1] + length * (1 - i/number))


speed(10)
parabola_recursion([-300,-300], 600, 30)