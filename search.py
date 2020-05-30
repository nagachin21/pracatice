import numpy as np

def linear_search(A, n, v):
    k = 0
    print(A)
    while k <= n-1:
        if A[k] == v:
            print("発見: " + str(v))
            return
        k+=1
    print("見つからない")

    return

def sentinel_linear_search(A, n, v):
    sentinel_A = np.append(A, v)
    k = 0
    print(sentinel_A)
    while not sentinel_A[k] == v:
        k += 1
    
    if k + 1 <= n:
        print("発見:" + str(v) + " k = " + str(k))
    else:
        print("見つからない")

    return

def binary_search(A,n,v):
    print(A)
    a = 1
    b = n
    while a <= b:
        print(str(a) + " : " + str(b))
        k = int(np.floor( (a+b)/2 ))
        print(k, A[k-1])
        if A[k-1] == v:
            print("発見: " + str(v))
            return
        elif A[k-1] < v:
            a = k + 1
        else :
            b = k - 1
    
    print("見つからない")
    return



