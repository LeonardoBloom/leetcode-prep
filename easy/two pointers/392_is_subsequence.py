def isSubsequence(s, t):

    # ORIGINAL
    # sp = 0
    # tp = 0

    # if len(s) == 0:
    #     return True
    # elif len(t) == 0:
    #     return False

    # while tp != len(t):
    #     if s[sp] == t[tp]:
    #         sp += 1

    #     tp += 1
    #     if sp == len(s):
    #         return True
    # return False

    # OPTIMIZED
    sp = 0
    tp = 0

    
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1

    return sp == len(s)   