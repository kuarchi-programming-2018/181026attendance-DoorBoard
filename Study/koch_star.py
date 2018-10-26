# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:36:04 2018

@author: toi1-
"""

import turtle as tl

def draw(length, depth):
    if depth == 0:
        tl.forward(length)
    
    else:
        draw(length/3, depth - 1)
        
        tl.left(60)
        
        draw(length/3, depth - 1)
        
        tl.right(120)
        
        draw(length/3, depth - 1)
        
        tl.left(60)
        
        draw(length/3, depth - 1)

def draw_star(length, depth):
    for i in range(3):
        draw(length, depth)
        tl.right(120)
        
    
    
    

#tl.tracer(0,0) # no animation
tl.up()
tl.setpos(-250,150)
tl.down()
tl.speed(0)  # 0:fastest, 1:slow to 10:fast
draw_star(500, 2)
tl.done()
