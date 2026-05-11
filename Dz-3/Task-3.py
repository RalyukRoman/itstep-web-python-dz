def calculate(list_to_work, function_to_call):
    result = []
    for element in list_to_work:
        result.append(function_to_call(element))
    return result

arr = [1, 2, 3, 4, 5]
print('\nArray:', arr)

print('\nChoice of function to call: 1 - square, 2 - cube')
choice = int(input('Enter your choice: '))

if choice == 1:
    def square(x):
        return x ** 2
    print("\nResult:", calculate(arr, square))
elif choice == 2:
    def cube(x):
        return x ** 3
    print("\nResult:", calculate(arr, cube))