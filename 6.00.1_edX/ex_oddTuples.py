def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here

    outTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            outTup = outTup + (aTup[i],)
    return outTup


