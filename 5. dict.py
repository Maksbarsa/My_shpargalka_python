"=============================================== Создание словаря ==================================================="""

# Создание словаря:
a1 = {"name" : "Jon"}
# print(a1):  {'name' : 'Jon'}


# Создание словаря из списка кортежей:
b1 = [('name', 'Jon'), ('age' , '23')]
a2 = dict(b1)
# print(a2):  {'name': 'Jon', 'age': '23'}


# Создание словаря с использованием именованных аргументов (только для строковых ключей):
a3 = dict(name = 'Jon', age = '32')
# print(a3):  {'name': 'Jon', 'age': '32'}


# Создание словаря с одинаковыми значениями:
b2 = ['name', 'Jon', 'age' , '23']
a4 = dict.fromkeys(b2, "value")
# print(a4):  {'name': 'value', 'Jon': 'value', 'age': 'value', '23': 'value'}


# Создание словаря из списка с нумерацией:
b3 = ['name', 'Jon', 'age' , '23']
a5 = dict([i for i in enumerate(b3)])
# print(a5):  {0: 'name', 1: 'Jon', 2: 'age', 3: '23'}


"========================================== Доступ к элементам словар ================================================="

# Получение значения по ключу, (если введенного ключа нет, возникнет ошибка!)
dict_1 = {"name" : "Jon", "age" : 32, "city" : "New-York"}
name = dict_1["name"]
# print(name):  Jon

# Безопасный способ получения значения, (если введенного ключа нет, ошибки не будет!)
phone = dict_1.get("phone")
# print(phone):  None


# Проверка наличия ключа: True / False
dict_2 = {"name" : "Jon", "age" : 32, "city" : "New-York"}
# print("name" in dict_2):  True


# Доступ к значениям во вложенном словаре:
dict_3 = {"person1" : {"name" : "Jon", "age" : 33}, "person2" : {"name" :  "Jon", "age" : 33}}
a6 = dict_3["person1"]["age"]
# print(a6):  33


# Получение значения по ключу, (если такого ключа нет, возникнет ошибка!)
dict_4 = {"name" : "Jon", "age" : 20, "city" : "New-York"}
age_1 = dict_4["age"]
# print(age_1):  20

# Безопасный способ получения ключа, (если введенного ключа нет, ошибки не будет!)
lastname = dict_4.get("lastname")
# print(lastname):  None


# Проверка наличия ключа:
dict_5 = {"name" : "Jon", "age" : 20, "city" : "Moskow"}
# print("name" in dict_5):  True


"=================================== Добавление и изменение элементов словаря ========================================="

# Добавление нового ключа + значение:
dict_6 = {"name": "Jon", "age" : 20}
dict_6["city"] = "Krasnodar"
# print(dict_6):  {'name': 'Jon', 'age': 20, 'city': 'Krasnodar'}


# Изменение значения по ключу:
dict_7 = {"name" : "Jon", "age" : 20, "city" : "Moskow"}
dict_7["age"] = 7
# print(dict_7):  {'name': 'Jon', 'age': 7, 'city': 'Moskow'}


# Массовое добавление ключа + значения:
dict_8 = {'name': 'Jon', 'age': 8, 'city': 'Krasnodar'}
dict_8.update({'city': 'Sochi', 'job': "santehnik"})
# print(dict_8):  {'name': 'Jon', 'age': 8, 'city': 'Sochi', 'job': 'santehnik'}


"======================================== Удаление элементов в словаре ================================================"

# Удаление элемента по ключу:
dict_9 = {"name" : "Jon", "age" : 20, "city" : "Moskow"}
del dict_9["age"]
# print(dict_9):  {'name': 'Jon', 'city': 'Moskow'}

# Удаление и возврат элемента по ключу (если нет такого ключа, произойдет ошибка!)
dict_10 = {"name" : "Jon", "age" : 20, "city" : "New-York"}
age_2 = dict_10.pop("age")
# print(dict_10):  {'name': 'Jon', 'city': 'New-York'}
# print(age_2):  20


# Безопасное удаление и возврат элемента по ключу (если нет такого ключа, ошибки не будет!)
dict_11 = {"name" : "Jon", "age" : 20, "city" : "New-York"}
age_3 = dict_11.pop("job", "Такого ключа здесь нет!")
# print(dict_11):  {'name': 'Jon', 'age': 20, 'city': 'New-York'}
# print(age_3):  Такого ключа здесь нет!


"==================================Получение ключей, значений и пар ключ-значение======================================"

person1 = {"name": "John", "age": 30, "city": "New York"}
# Получение всех ключей:
print(person1.keys())
# dict_keys(['name', 'age', 'city'])


person2 = {"name": "John", "age": 30, "city": "New York"}
# Получение всех значений:
print(person2.values())
# dict_values(['John', 30, 'New York'])


person3 = {"name": "John", "age": 30, "city": "New York"}
# Получение всех пар ключ-значение:
print(person3.items())
# dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])


person4 = {"name": "John", "age": 30, "city": "Krasnodar"}
# Преобразование представлений в списки:
keys_list = list(person4)
print(keys_list)
# ['name', 'age', 'city']