def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    out = base
    if exp == 0:
        out = 1
    else:
        while exp > 1:
            out *= base
            exp -= 1
    return out


def recurPower(base, exp):

    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)

