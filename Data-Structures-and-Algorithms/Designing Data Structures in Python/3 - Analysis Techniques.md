# Asymptotic Analysis for Performance
- Characterize **time complexity** of method
    - Time for a method to complete
    - Calculate time as function `t(n)`` relating the number of steps given aggregate size, ``n``
- Characterize **space complexity** of method
    - Amount of computer storage required
    - Determine required space ``s(n)`` in similar fashion

# Data Structure Cost Model
- From data structure implementation, determine total number of steps based on ``n``
    - Sequential, deterministic computing platform
- Assume a **constant cost** to every operation
    - Enables using ``t(n)`` to estimate execution time

# Performance Computation
Add 2^n random digits for n = 1 to 8
    
    import random
    import timeit

    for trial in [2**_ for _ in range(1,9)]:
        numbers = [random.randint(1,9) for _ in range(trial)]
        m = timeit.timeit(stmt='sum = 0\nfor d in numbers:\n\tsum = sum + d',
                          setup='import random\nnumbers = ' + str(numbers))
        print ('{0:d} {1:f}'.format(trial, m))

# Asymptotic Space Complexity
- How much extra storage is required
    - A secondary concern that cannot be ignored
- Sample problem
    - Determine if **list** contains duplicate entries
    - Two approaches

Example 1: 
Uses **set** for extra storage
Amortized constant time for **set**
Performance O(n) time with O(n) space

    def uniqueCheckFast(aList):
    """
    Return True if aList contains any duplicates. It
    completes in O(n) time with O(n) space required.
    Individual elements must be hashable.
    """
    check = set()
    for v in alist:
        if v in check:
            return True
        check.add(v)
    return False
    
Example 2:
Nested for loop is key to O(n^2) or quadtratic performance!
    
    def uniqueCheckFast(aList):
    """
    Return True if aList contains any duplicates. It
    completes in O(n^2) time with no space required.
    """
    for i in range (len(aList)-1):
        for j in range(i-1, len(aList)):
            if aList[i] == aList[j]:
                return True
            return False
                
                