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


def quick_sort(A, L, R):
    if L < R:
        p = L
        k = L + 1
        while k <= R:
            if A[k-1] < A[L-1]:
                tmp = A[(p + 1) -1 ]
                A[(p + 1) -1] = A[k-1]
                A[k-1] = tmp
                p+=1
            k+=1
        tmp = A[L-1]
        A[L-1] = A[p-1]
        A[p-1] = tmp

        print("L: " + str(A[L-1:p-1]) + " p: " + str(A[p-1]) + " R: " + str(A[(p+1)-1:R]))

        quick_sort(A, L, p-1)
        quick_sort(A, p+1, R)
    return A


def random_quick_sort(A, L, R):
    if L < R:
        r = np.random.randint(L, R)
        swap = A[L-1]
        A[L-1] = A[r]
        A[r] = swap
        p = L
        k = L + 1
        while k <= R:
            if A[k-1] < A[L-1]:
                tmp = A[(p + 1) -1 ]
                A[(p + 1) -1] = A[k-1]
                A[k-1] = tmp
                p+=1
            k+=1
        tmp = A[L-1]
        A[L-1] = A[p-1]
        A[p-1] = tmp

        print("L: " + str(A[L-1:p-1]) + " p: " + str(A[p-1]) + " R: " + str(A[(p+1)-1:R]))

        random_quick_sort(A, L, p-1)
        random_quick_sort(A, p+1, R)
    return A
