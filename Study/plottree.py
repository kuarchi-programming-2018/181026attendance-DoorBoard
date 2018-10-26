# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:19:54 2018

@author: toi1-
"""
from turtle import *
from tree import *

#パラメータを代入します.ここではサンプルに以下の値を設定しています

lim = 30 #枝の長さの下限(len以下.20～50くらい)
len = 200 #幹の長さ(200～300くらい)
dev_r = 0.6 #右分岐までの分割比(0以上1以下.)
dev_l = 0.7 #左分岐までの分割比(0以上1以下.dev_rと離れすぎないと綺麗)
ratio_r = 0.8 #右分岐後の短縮比(0以上1以下.0.7くらい)
ratio_l = 0.75 #左分岐後の短縮比(0以上1以下.ratio_rと離れすぎないと綺麗)
angle_r = 25 #右分岐時の角度(0以上90以下が綺麗)
angle_l = 33 #左分岐時の角度(0以上90以下が綺麗.angle_rとの公約数が少ない方がランダムっぽい)



#-------------------以下描画-------------------

penup()
setpos(0,-300)
pendown()
left(90)
speed(0)
tree_recursion(lim, len, dev_r, dev_l, ratio_r, ratio_l,
               angle_r, angle_l)
hideturtle()
done()
