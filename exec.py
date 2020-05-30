import sys, os 
sys.path.append('./')
import numpy as np
from search import linear＿search, sentinel_linear_search, binary_search
from sort import bubble_sort, quick_sort, random_quick_sort


A = np.random.randint(20, size=10)
seq_A = np.arange(0,10,1)

#sorted_A = bubble_sort(A, 10)
#print(sorted_A)

#sentinel_linear_search(A, 20, 10)
#linear_search(A, 20, 100)
#binary_search(seq_A, 10, 2)

print(A)
print("Sorted by quick sort")
sorted_A = quick_sort(A, 1, 10)
print(sorted_A)
print("--------------------------------------")
print("Sorted by random quick sort")
random_sorted_A = random_quick_sort(A, 1, 10)
print(random_sorted_A)
