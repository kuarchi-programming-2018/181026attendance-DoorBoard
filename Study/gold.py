# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 00:51:06 2018

@author: toi1-
"""

from turtle import *
import numpy as np


# 与えられた黄金長方形から螺旋を描く関数
# spiral_recursion(始点，繰り返し回数）
def spiral_recursion(points, depth):
    rectangle(points)
    new_points = next_points(points)
    
    if depth == 0:
        penup()
        setpos(-200, -200)
        
    else:
        spiral_recursion(new_points, depth - 1)

#任意の始点,単位長から黄金長方形の螺旋を描く関数
#spiral(始点,　単位長,　繰り返し回数)
def spiral(point, length, depth):
    points = [point, [point[0], point[1] - length],
              [point[0] + length * gold()  , point[1] - length],
              [point[0] + length * gold(), point[1]]]
    spiral_recursion(points, depth)


#---------------— 以下は補助的な関数—------------------------


# 黄金比を出す関数
# gold()
def gold():
    return (1 + np.sqrt(5))/2


# 内分を実行する関数
# deviding(点A, 点B, 内分比)
def deviding(p0, p1, r):
    return p0 * (1 - r) + p1 * r


# 長方形を描く関数
# rectangle(四角形の4頂点）
def rectangle(points):
    [[x0, y0], [x1, y1], [x2, y2], [x3, y3]] = points
    penup()
    setpos(x0, y0)
    pendown()
    setpos(x1, y1)
    setpos(x2, y2)
    setpos(x3, y3)
    setpos(x0, y0)


# 2点の内分点を求める関数
# deviding_point(点A, 点B, 内分比）
def deviding_point(p0, p1, ratio):
    [x0, y0] = p0
    [x1, y1] = p1
    xr = deviding(x0, x1, ratio)
    yr = deviding(y0, y1, ratio)
    return [xr, yr]


#　最初の長方形の頂点を求める関数
# start_points(始点, 単位長)
def start_points(start,length):
    return [start, [start[0], start[1] - length],
              [start[0] + length * gold()  , start[1] - length],
              start[0] + length * gold(), start[1]]


# 一つ次の長方形の頂点を求める関数
# next_points(四角形の4頂点内分比）
def next_points(points):
    [p0, p1, p2, p3] = points
    pr0 = deviding_point(p1, p2, 1/(gold()))
    pr1 = p2
    pr2 = p3
    pr3 = deviding_point(p0, p3, 1/(gold()))
    return [pr0, pr1, pr2, pr3]
