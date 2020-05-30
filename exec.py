import sys, os 
sys.path.append('./')
import numpy as np
from search import linear＿search, sentinel_linear_search, binary_search
from sort import bubble_sort


A = np.random.randint(20, size=10)
seq_A = np.arange(0,10,1)

sorted_A = bubble_sort(A, 10)
print(sorted_A)

#sentinel_linear_search(A, 20, 10)
#linear_search(A, 20, 100)
#binary_search(seq_A, 10, 2)