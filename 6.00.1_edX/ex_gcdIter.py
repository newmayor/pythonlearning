def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    a1 = a
    b1 = b

    if a < b:
        while a != 1:
            if b % a == 0 and a1 % a == 0:
                gcd = a
                return gcd
            else:
                a -= 1
    else:
        while b != 1:
            if a % b == 0 and b1 % b == 0:
                gcd = b
                return gcd
            else:
                b -= 1
