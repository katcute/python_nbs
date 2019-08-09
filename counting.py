m = 5
A = [0, 0, 4, 2, 4, 5]
def counts(A, m):
    '''
    A is a list of numbers
    m is the largest unique number in the list
    '''
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count
counts(A, m)
