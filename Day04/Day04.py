"""
Created on Sun Dec  4 00:00:26 2022

@author: tricialyjun
"""
with open("bingo", "r") as f:
    bingo = f.read().strip().split("\n\n")

outcome = bingo.pop(0).split(",")
cards = [x.replace("\n", " ").strip().replace("  ", " ").split(" ") for x in bingo]

def check_winner(card):
    check = [card[i*5:(i+1)*5].count(0) for i in range(5)] + [card[i::5].count(0) for i in range(5)]
    if check.count(5) == 1:
        win_value = sum([int(x) for x in card])
    else:
        win_value = 0
    return win_value

win_order = []
win_score = []
for jj in range(len(cards)):
    for ii in range(len(outcome)):
        if outcome[ii] in cards[jj]:
            cards[jj][cards[jj].index(outcome[ii])] = 0
            score = check_winner(cards[jj]) * int(outcome[ii])
            if score != 0:
                win_score.append(score)
                win_order.append(ii)
                break

# Part 1
print(win_score[win_order.index(min(win_order))])

# Part 2
print(win_score[win_order.index(max(win_order))])