class intDict(object):
    """A dictionary with integer keys. """
    def __init__(self, numBuckets):
        """create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
    
    def addEntry(self, key, dictVal):
        """Assumes key is an int. Add an entry."""
        hashBucket = self.buckets[key%self.numBuckets] #I dont fully understand this line. convert key to hashed equivalent and then look up that key in self.numBuckets?
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key: #if that key is found in any of the spots within hashBucket, store the tuple (key, dictVal) at index i location
                hashBucket[i] = (key, dictVal)
                return
        hashBucket.append((key, dictVal)) #if it wasn't found, store the tuple (key, dictVal) at the end of the bucket.

    def getValue(self, key):
        """Assumes key is an int.
        Returns value associated with key."""
        hackBucket = self.buckets[key%self.numBuckets]
        for e in hashBucket: #for every key, dictValue pair,
            if e[0] == key: #if there's a match,
                return e[1] #return value associated with key
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
            return result[:-1] + '}' #result[:-1] omits the last comma


import random
D = intDict(17)
for i in range(20):
    #choose a random int in the range 0 to 10^5 - 1
    key = random.choice(range(10**5))
    D.addEntry(key,i)
print('The value of the intDict is:')
print(D)
print('\n', 'The buckets are:')
for hashBucket in D.buckets: 
    print('  ', hashBucket)

    