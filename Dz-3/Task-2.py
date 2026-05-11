def sum_arrays_elements(arr1, arr2):
    max_length = max(len(arr1), len(arr2))
    for i in range(max_length):
        val1 = arr1[i] if i < len(arr1) else 0
        val2 = arr2[i] if i < len(arr2) else 0
        yield val1 + val2

arr1 = [1, 2, 3, 5, 2, 6, 2, -5, 0]
arr2 = [4, 5, 3, 1, 5, 4, 1]

print()
print('Array #1:', arr1)
print('Array #2:', arr2)

print()
result = list(sum_arrays_elements(arr1, arr2))
print('Result:  ', result)