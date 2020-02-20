def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    l = len(aStr)
    if l%2 !=0 : 
        mid = int(l/2) 
    elif len(aStr) == 0:
        return False
    else:
        mid = int(l/2)

    if char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        aStr = aStr[:mid]
        return isIn(char, aStr)
    elif char > aStr[mid]:
        aStr = aStr[mid:]
        return isIn(char, aStr)
    elif len(aStr) == 1 and char != aStr:
        return False
    else:
        return False