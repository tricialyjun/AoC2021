#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:56:33 2022

@author: tricialyjun
"""
import numpy as np

depth = np.loadtxt('depth', dtype = int)

# Part 1
difference = depth[1:] - depth[:-1]
print(sum(difference > 0))

# Part 2
difference_3 = depth[3:] - depth[:-3]
print(sum(difference_3 > 0))