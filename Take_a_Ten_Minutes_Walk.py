
def is_valid_walk(walk):
    dict = {'n': 0, 's': 0, 'w': 0, 'e': 0}
    if len(walk) != 10:
        return False
    for i in walk:
            if i == 'n':
                dict['n'] +=1
            elif i == 's':
                dict['s'] +=1
            elif i == 'w':
                dict['w'] +=1
            elif i == 'e':
                dict['e'] +=1
    if dict['n'] - dict['s'] == 0 and dict ['w'] - dict['e'] == 0:
        return True
    return False

print(is_valid_walk(['n', 's', 'e', 'w', 'n', 'n', 'e', 'w', 'n', 's'])) # should return False
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # should return True.
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # should return False.
print(is_valid_walk(['w']))# should return False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # shoul return False.


def is_valid_walk(walk):

    if len(walk) !=10:
            return False
    if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
        return True
    return False

print(is_valid_walk(['n', 's', 'e', 'w', 'n', 'n', 'e', 'w', 'n', 's'])) # should return False
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # should return True.
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # should return False.
print(is_valid_walk(['w']))# should return False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # shoul return False.