""" Строковые типы данных ==========================================================================================="""

text1 = "my text good".title()  # Делает заглавными первые буквы каждого слова в строке; Пример: My Text Good

text2 = "my text good".capitalize()  # Делает заглавную букву только у первого слова в строке; Пример: My text good

text3 = "my text good".count("o")  # Считает сколько раз встречается буква "o" в строке; Пример: 2

text4 = "my text good"
text4_1 = text4.startswith("my")  # Проверяет начинается ли строка со слова "my" (True - да, False - нет) Пример: True
text4_2 = text4.endswith("text")  # Проверяет заканчивается ли строка словом "text" (True - да, False - нет) Пример: False

text5 = "my text good"
text5_1 = "te" in text5  # Проверяет наличия подстроки "te" в строке (True - да, False - нет) Пример: True

text6 = "my text good"
text6_1 = text6.replace("good", "bad")  # Заменяет подстроку. Пример: my text bad


""" Разделение и объединение строк =================================================================================="""

text7 = "my-text good"
text7_1 = text7.split()  # Разделяет строку по пробелу и создает список. Пример: ['my-text', 'good']
text7_2 = text7.split("-")  # Разделяет строку по конкретному символу "-" и создает список. Пример: ['my', 'text good']

text8 = "   my text very good   1"
text8_1 = text8.strip()  # Удаляет пробельные символы слева/справа. Пример. до: "   my text very good   1"
#                                                                        после: "my text very good   1"

text8_2 = text8.strip(" 1")  # Удаляет  символы слева/справа. Пример. до: "   my text very good   1"
#                                                                 после: "my text very good"

text8_3 = text8.lstrip(" 1")  # Удаляет символы слева. Пример. до: "   my text very good   1"
#                                                           после: "my text very good   1"

text8_4 = text8.rstrip(" 1")  # Удаляет символы справа. Пример. до: "   my text very good   1"
#                                                            после: "   my text very good"

""" Объединение списка в строку ====================================================================================="""

lst = ["my", "text", "very", "good"]
lst1 = " | ".join(lst)  # Объединяет список в строку по любому разделителю " | ". Пример: my | text | very | good





