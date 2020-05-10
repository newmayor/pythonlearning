
def merge(left, right, compare): 
    """Assumes left and right are sorted lists and compare defines and ordering on the elements.
    Returns a new sorted (by compare) list containing the same elements as (left + right) would contain. """

    result = [] #initiate the return object
    i,j = 0,0 #starting position?
    while i < len(left) and j < len(right):
        if compare(left[i], right[i]): #compare is a function?
            result.append(left[i])
            result += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i]) #whats happening here? Just building another list as a copy of left?
        i += 1
    while (j < len(right)):
        result.append(right[j]) #looks like this while loop and the one before it (for left) are just appending the whole left and right lists at the end of result after already having sorted the lists in the very first while loop. Why is that?
        j += 1
    return result


def mergeSort(L, compare = lambda x, y: x<y):
    """Assumes L is a list, compare defines and ordering on elements of L.
    Returns a new sorted list with the same elements as L.
    What the heck is lambda? """
    if len(L) < 2:
        return L[:] #list is too short, so it's already sorted
    else:
        middle = len(L)//2 #what's the double / do? Is it rounded division?
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
    #Time complexity: we already know merge() has complexity O(len(L)). mergeSort() is O(n*log(n)). The time complexity of mergeSort is the complexity of merge(), O(len(L)), multipled by the number of levels of recursion. Since mergeSort divides the list L into half each time, that's a logarithmic decrement by half; therefore, a logarithmic complexity O(log(len(L))). Therefore, the time complexity of mergeSort() is O(n*log(n)) in simplified standard form.