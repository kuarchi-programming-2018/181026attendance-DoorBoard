# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:37:25 2018

@author: toi1-
"""
from turtle import *

#左右に枝を伸ばす木を描く再帰関数
#tree_recursion(枝の長さの下限, 幹の長さ, 右分岐までの分割比, 左分岐までの分割比,
                #右分岐後の短縮比, 左分岐後の短縮比, 右分岐時の角度,　左分岐時の角度)
def tree_recursion(lim, len, dev_r, dev_l, ratio_r, ratio_l,
                   angle_r, angle_l):
    
    if len <= lim:
        forward(len)
        backward(len)
    
    else:
        forward(len)
        backward(len)
        
        forward(len * dev_r)
        
        right(angle_r)
        tree_recursion(lim, len * ratio_r, dev_r, dev_l, ratio_r, ratio_l,
                       angle_r, angle_l)
        left(angle_r)
        
        backward(len * dev_r)
        
        forward(len * dev_l)
        
        left(angle_l)
        tree_recursion(lim, len * ratio_l, dev_r, dev_l, ratio_r, ratio_l,
                       angle_r, angle_l)
        right(angle_l)
        
        backward(len * dev_l)
        