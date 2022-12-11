# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

import random
num = int(input("Укажите длину списка: "))
my_list = [random.randint(1000, 9999) for _ in range(num)]
print(f'1 этап: {my_list}')
for_del = input("Введите цифру: ")
for i in range(num):
    my_list[i] = int(str(my_list[i]).replace(for_del, ''))
print(f'2 этап: {my_list}')
def sum_digit_for_dig(num):
    dig_sum = 0
    while num > 0:
        dig_sum += num % 10
        num = num // 10
    if dig_sum > 9:
        dig_sum = dig_sum % 10 + dig_sum // 10
    return dig_sum
my_list = list(map(lambda x: sum_digit_for_dig(x), my_list))
print(f'3 этап: {my_list}')
my_list = list(set(my_list))
print(f'4 этап: {my_list}')
# Старое решение
# - создает список из рандомных четырех значных чисел
# my_list = []
# num = int(input("Укажите длину списка: "))
# for i in range(num):
#     my_list.append(random.randint(1000, 9999))
# print(f'1 этап: {my_list}')
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# for_del = input("Введите цифру: ")
# for i in range(num):
#     my_list[i] = int(str(my_list[i]).replace(for_del, ''))
# print(f'2 этап: {my_list}')
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# def sum_digit_for_dig(num):
#     dig_sum = 0
#     while num > 0:
#         dig_sum += num % 10
#         num = num // 10
#     if dig_sum > 9:
#         dig_sum = dig_sum % 10 + dig_sum // 10 #тут конечно хорошо бы рекурсию, но я что-то с ней не справилась
#     return dig_sum
# for i in range(num):
#     my_list[i] = sum_digit_for_dig(my_list[i])
# print(f'3 этап: {my_list}')
# - из финального списка убирает все дублирующиеся элементы
# un_list = []
# for i in range(len(my_list)):
#     if my_list[i] not in un_list:
#         un_list.append(my_list[i])
#
# print(f'4 этап: {un_list}')
