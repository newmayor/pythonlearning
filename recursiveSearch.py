
def search(L, e):
    """Assumes L is a list and e is the element looking to be matched in L. L is sorted in ascending order. Returns True if e is in L and False otherwise."""

    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low +high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search. end of the list L.
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
        
        if len(L) == 0:
            return False
        else: return bSearch(L, e, 0, len(L) - 1)