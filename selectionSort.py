def selSort(L):
    """Assumes that L is a list of elements that can be compared using >.
    Sorts L in ascending order. """

    suffixStart = 0
    while suffixStart != len(L):
        #look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
    #this program consists of two loops that increment thru a length of list. The inside one is O(len(L)) and the outside one is O(len(L)). Therefore, this program has complexity O(len(L^2)). This is known as quadratic time complexity.