"""
Created on Fri Dec  2 00:32:44 2022

@author: tricialyjun
"""
import numpy as np

with open('plannedcourse', 'r') as f:
    course = f.read().strip().split("\n")

course = [x.split(" ") for x in course]
course = np.asarray(course)

# Part 1
forward = course[course[:,0] == "forward",1].astype(int)
down    = course[course[:,0] == "down", 1].astype(int)
up      = course[course[:,0] == "up", 1].astype(int)
print(sum(forward) * (sum(down)-sum(up)))

# Part 2
aim = 0
horizontal = 0
depth = 0
for ii in range(len(course)):
    if course[ii,0] == "forward":
        horizontal += course[ii,1].astype(int)
        depth += aim*course[ii,1].astype(int)
    elif course[ii,0] == "up":
        aim -= course[ii,1].astype(int)
    elif course[ii,0] == "down":
        aim += course[ii,1].astype(int)
        
print(horizontal * depth)