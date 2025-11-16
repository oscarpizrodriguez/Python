from slicing_tools import *

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

result = get_row(array,0)
print(result)
result = get_column(array,0)
print(result)
result = get_subarray(array,0,2,0,4)
print(result)
result = greater_than(array,5)
print(result)