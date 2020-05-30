import numpy as np

def bubble_sort(A, n):
    m = n
    while m > 1:
        k = 1
        while k < m:
            if A[k-1] > A[(k+1) - 1]:
                tmp = A[(k+1) - 1]
                A[(k+1) - 1] = A[k-1]
                A[k-1] = tmp
            k+=1
            print(A)
        m-=1
    return A