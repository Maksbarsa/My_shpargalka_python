"""=================================== Сравнение с обычными функциями ==============================================="""
# Обычная функция
def square(x):
    return x * x
# print(square(5)):  25

# Эквивалентная лямбда-функция
square_lambda = lambda x: x * x
# print(square_lambda(5)):  25


# Функция с несколькими аргументами
def power(num1, num2):
    return num1 ** num2
# print(power(2, 3)):  8

# Эквивалентная лямбда-функция с несколькими аргументами
power_lambda = lambda num1, num2: num1 ** num2
# print(power_lambda(2, 3)):  8


"======= Наиболее распространенные случаи использования лямбда-функции с функциями высшего порядка, такими как: ======="

"map() - Функция применяет указанную функцию к каждому элементу итерируемого объекта:"
# Удвоение всех чисел в списке
lst = [1, 2, 3, 4, 5]

# С обычной функцией:
def double(x):
    return x * 2

doubled = list(map(double, lst))
# print(doubled):  [2, 4, 6, 8, 10]


# С лямбда-функцией (гораздо компактнее!):
doubled_lambda = list(map(lambda x: x * 2, lst))
# print(doubled_lambda):  [2, 4, 6, 8, 10]


# Преобразование температуры из Цельсия в Фаренгейт
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
# print(fahrenheit): [32.0, 50.0, 68.0, 86.0, 104.0]


"filter() - Функция создает итератор из элементов, для которых функция возвращает True:"
# Фильтрация четных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_lambda = list(filter(lambda x: x % 2 == 0, numbers))  # функция filter используется как оператор if (если), без иначе!
# print(even_lambda): [2, 4, 6, 8, 10]


# Фильтрация слов длиннее 3 букв
words = ["hi", "hello", "hey", "howdy", "hi there"]
long_words = list(filter(lambda word: len(word) > 3, words))  # функция filter используется как оператор if (если), без иначе!
# print(long_words): ['hello', 'howdy', 'hi there']


"reduce() - (из модуля functools) последовательно применяет функцию к элементам, накапливая результат:"
from functools import reduce

# Сумма всех чисел в списке
numbers = [1, 2, 3, 4, 5]
total_lambda = reduce(lambda x, y: x + y, numbers)
# print(total_lambda):  15


# Объединение строк
words = ["Hello", "world", "of", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
# print(sentence):  Hello world of Python


"==== Передача лямбда-функций в другие функции. Лямбда-функции часто используются как аргументы в других функциях: ===="

# Использование с разными лямбда-функциями:
def apply_operation(x, y, operation):
    """Применяет операцию к двум числам и возвращает результат"""
    return operation(x, y)

# print(apply_operation(5, 3, lambda x, y: x + y))  # Сложение
# 8
# print(apply_operation(5, 3, lambda x, y: x * y))  # Умножение
# 15


# Форматирование данных:
def format_data(data, formatter):
    """Форматирует данные с помощью указанной функции"""
    return [formatter(item) for item in data]

names = ["alice", "bob", "charlie"]
# print(format_data(names, lambda x: x.title()))  # Начало с заглавной
# ['Alice', 'Bob', 'Charlie']

