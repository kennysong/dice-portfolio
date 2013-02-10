from itertools import product

rolls = dict()
times = int(raw_input('How many dice rolls?  '))

for roll in product([1, 2, 3, 4, 5, 6], repeat = times):
    score = max(roll)
    if rolls.get(score):
        rolls[score].append(roll)
    else:
        rolls[score] = [roll]
