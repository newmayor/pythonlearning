
def search(L, e):
    """Assumes L is a list and e is the element looking to be matched in L. L is sorted in ascending order. Returns True if e is in L and False otherwise."""

    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low +high)//2 #find the center element of the remaining list
        if L[mid] == e:
            return True
        elif L[mid] > e: 
            if low == mid: #nothing left to search. end of the list L.
                return False
            else:
                return bSearch(L, e, low, mid - 1) # search on left side of the list
        else:
            return bSearch(L, e, mid + 1, high) #search on right side of the list
        
        if len(L) == 0: #terminate the program if length of the list is 0. This ensures theres at least 1 element to do a search against
            return False
        else: return bSearch(L, e, 0, len(L) - 1) # now start the search