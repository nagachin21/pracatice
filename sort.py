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

def insertion_sort(A, n):
    for i in range(1, n):
        tmp = A[i]
        j = i
        while tmp < A[j-1] and j > 0:
            A[j] = A[j-1]
            j-=1
        A[j] = tmp
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


def randomized_quick_sort(A, L, R):
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

        randomized_quick_sort(A, L, p-1)
        randomized_quick_sort(A, p+1, R)
    return A


def merge_sort(A, cnt):
    #print("Merge Sort : " + str(cnt) + " 回目 >> ")

    if len(A) > 1:
        mid = len(A) // 2
        cnt += 1
        #print( "L: " + str(A[:mid]) + " R: " + str(A[mid:]) )
        L = merge_sort(A[:mid], cnt)
        R = merge_sort(A[mid:], cnt)

        A = np.empty(0)
        i = j = 0
        #print( "ソート開始 >> L: " + str(L) + " R: " + str(R) )
        while len(L) > i and len(R) > j:
            if L[i] < R[j]:
                A = np.append(A, L[i])
                #print("LをAに追加" + str(A))
                i += 1
            else:
                A = np.append(A, R[j])
                #print("RをAに追加" + str(A))
                j += 1

        if len(L) > i:
            #print("残りのLをAに追加")
            A = np.append(A, L[i:])
        elif len(R) > j:
            #print("残りのRをAに追加")
            A = np.append(A, R[j:])
    else:
        #print(A)
        pass

    #print("<< Merge Sort : " + str(cnt) + " 回目")
    #print("終了 : " + str(A))
    return A
