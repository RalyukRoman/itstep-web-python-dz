def fibonacci_generator(start, end):
    a, b = 0, 1
    while a <= end:
        if a >= start:
            yield a
        a, b = b, a + b

print("\nFibonacci numbers between 3 and 500:")
for number in fibonacci_generator(3, 500):
    print(number, end=' ')

print("\n\nFibonacci numbers between 86 and 523:")
for number in fibonacci_generator(86, 523):
    print(number, end=' ')

print("\n\nFibonacci numbers between -5 and 24:")
for number in fibonacci_generator(-5, 24):
    print(number, end=' ')

print()