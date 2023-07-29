# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def create_array(n, mn, mx):
    import random
    array = [random.randint(mn, mx) for _ in range(n)]
    return array


element_1 = int(input('Введите количество чисел первого множества: '))
element_2 = int(input('Введите количество чисел второго множества: '))
listing_1 = create_array(element_1, 0, 15)
listing_2 = create_array(element_2, 0, 15)
print(listing_1)
print(listing_2)

set_1 = set(listing_1)
set_2 = set(listing_2)

result = set_1 & set_2
print('Числа которые встречаются в обоих множествах: - ', sorted(result), '\n')