#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:25:29 2022

@author: tricialyjun
"""
with open("vectors", "r") as f:
    vectors = f.read().strip().replace("-", "").replace(">","").replace(","," ").replace("  "," ").split("\n")
vectors = [[int(y) for y in x.split(" ")] for x in vectors]
x_max   = max([max(x[0], x[2]) for x in vectors])
y_max   = max([max(x[1], x[3]) for x in vectors])

testmap = [[0]*(x_max+1) for _ in range(y_max+1)]

# Part 1
hv_vect = [x for x in vectors if int(x[0]) == int(x[2]) or int(x[1]) == int(x[3])]
for kk in range(len(hv_vect)):
    x1, x2 = sorted([hv_vect[kk][0], hv_vect[kk][2]])
    y1, y2 = sorted([hv_vect[kk][1], hv_vect[kk][3]])
    for jj in range(y1, y2+1):
        for ii in range(x1, x2+1):
            testmap[jj][ii] += 1
    
print(sum([sum([int(x > 1) for x in y]) for y in testmap]))

# Part 2
d_vect = [x for x in vectors if x not in hv_vect] 
for kk in range(len(d_vect)):
    x1, x2 = sorted([d_vect[kk][0], d_vect[kk][2]])
    m = (d_vect[kk][2]-d_vect[kk][0])/(d_vect[kk][3]-d_vect[kk][1])
    if m > 0:
        y1 = min([d_vect[kk][1], d_vect[kk][3]]) 
        for dd in range(abs(x2 - x1 + 1)):
            testmap[y1 + dd][x1 + dd] += 1
    else:
        y1 = max([d_vect[kk][1], d_vect[kk][3]]) 
        for dd in range(abs(x2 - x1 + 1)):
            testmap[y1 - dd][x1 + dd] += 1

print(sum([sum([int(x > 1) for x in y]) for y in testmap]))