"""
Created on Thu Dec  1 23:44:42 2022

@author: tricialyjun
"""
# Part 1
with open('depth', 'r') as f:
    depth = f.read().strip("\n").split("\n")

depth = [int(x) for x in depth]
increase = [b-a for (a, b) in zip(depth[:-1], depth[1:]) if (b-a) > 0]
print(len(increase))

#Part 2
depth_n3 = [a+b+c for (a,b,c) in zip(depth[:-2], depth[1:-1], depth[2:])]
increase_n3 = [b-a for (a, b) in zip(depth_n3[:-1], depth_n3[1:]) if (b-a) > 0]
print(len(increase_n3))