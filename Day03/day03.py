"""
Created on Fri Dec  2 01:17:36 2022

@author: tricialyjun
"""

# Part 1
with open("powerconsumption", "r") as f:
    power_consumption = f.read().strip("\n").split("\n")

transpose_count = ['1' if (ii.count('1') > 500) else '0' for ii in list(zip(*power_consumption))]

gamma = int("".join(transpose_count), 2)
epsilon = 2**len(transpose_count)-1 - gamma
print(gamma*epsilon)

# Part 2
### Oxygen
searchstr = transpose_count[0]
searchlist = power_consumption
n = len(searchlist)
while n > 1:
    m = len(searchstr)
    searchlist = [x for x in searchlist if x.startswith(searchstr)]
    n = len(searchlist)
    if n == 1:
        break
    elif list(zip(*searchlist))[m].count('1') >= n/2:
        searchstr += '1'
    else:
        searchstr += '0'

oxygen = int(searchlist[0], 2)

### carbon_dioxide
searchstr = str(abs(int(transpose_count[0])-1))
searchlist = power_consumption
n = len(searchlist)
while n > 1:
    m = len(searchstr)
    searchlist = [x for x in searchlist if x.startswith(searchstr)]
    n = len(searchlist)
    if n == 1:
        break
    elif list(zip(*searchlist))[m].count('0') <= n/2:
        searchstr += '0'
    else:
        searchstr += '1'
        
carbon_dioxide = int(searchlist[0], 2)

print(oxygen * carbon_dioxide)