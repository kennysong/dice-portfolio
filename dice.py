from itertools import product

def get_player_rolls(n):
    '''Gets all possible rolls, sorted by score, for n rolls of the dice'''
    rolls = dict()

    for roll in product([1, 2, 3, 4, 5, 6], repeat = n):
        score = max(roll)
        if rolls.get(score):
            rolls[score].append(roll)
        else:
            rolls[score] = [roll]

    return rolls

def get_occurences(score, limit=9):
    '''Lists occurrences of a score for each set of n dice rolls up to limit'''  
    for i in range(1, limit):
        rolls = get_player_rolls(i)
        print 'score %i in %i rolls: %i'%(score, i, len(rolls[score]))
        
def get_all():
    '''Lists all occurrences 1-6 for pattern spotting (quite inefficient)'''
    for i in range(1, 7):
        get_occurences(i)

#rolls = get_player_rolls(int(raw_input('How many dice rolls?  ')))
