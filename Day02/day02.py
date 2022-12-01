"""
Created on Fri Dec  2 00:32:44 2022

@author: tricialyjun
"""

# Part 1
with open('plannedcourse', 'r') as f:
    course = f.read().strip("\n").split("\n", " ")
    

forward = [int(ii[-1]) for ii in course if ii.startswith('f')]
up      = [int(ii[-1]) for ii in course if ii.startswith('u')]
down    = [int(ii[-1]) for ii in course if ii.startswith('d')]

print(sum(forward) * (sum(down)-sum(up)))

# Part 2
aim = 0
horizontal = 0
depth = 0
for ii in range(len(course)):
    if course[ii][:-2] == "forward":
        horizontal += int(course[ii][-1])
        depth += aim*int(course[ii][-1])
    elif course[ii][:-2] == "up":
        aim -= int(course[ii][-1])
    elif course[ii][:-2] == "down":
        aim += int(course[ii][-1])
        
print(horizontal * depth)