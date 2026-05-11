
cortege_1 = (5, 2, 18, 3, 7, 10, 22, 20, 25, 17)
cortege_2 = (1, 2, 19, 3, 6, 10, 21, 17, 22)
cortege_3 = (4, 2, 11, 3, 8, 10, 17, 22, 27, 32)

print()
print('Кортеж 1: ', cortege_1)
print('Кортеж 2: ', cortege_2)
print('Кортеж 3: ', cortege_3, '\n')

# Завдання 1

common_elements = set(cortege_1) & set(cortege_2) & set(cortege_3)

print('Завдання 1: є у всіх кортежах')
print(common_elements, '\n')


# Завдання 2

unique_elements_1 = set(cortege_1) - set(cortege_2) - set(cortege_3)
unique_elements_2 = set(cortege_2) - set(cortege_1) - set(cortege_3)
unique_elements_3 = set(cortege_3) - set(cortege_1) - set(cortege_2)

print('Завдання 2: унікальні для кожного списку')
print('Кортеж 1: ', unique_elements_1)
print('Кортеж 2: ', unique_elements_2)
print('Кортеж 3: ', unique_elements_3, '\n')


# Завдання 3

same_elements = []
min_length = min(len(cortege_1), len(cortege_2), len(cortege_3))

for i in range(min_length):
    if (cortege_1[i] == cortege_2[i] == cortege_3[i]):
        same_elements.append(cortege_1[i])

print('Завдання 3: є в кожному з кортежів і на тій самій позиції')
print(same_elements)