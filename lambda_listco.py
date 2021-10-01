# 1. Напишите lambda функцию которая принимает число и возвращает его возведенным в степень двойки
# 2. Напишите lambda функцию которая принимает строку и возвращает её в верхнем регистре.
# 3. Напишите lambda функцию которая принимает строку и возвращает её в нижнем регистре.
# 4. Напишите lambda функцию которая принимает список или tuple и возвращает последний элемент.
# 5. Дан список: [1,2,3,4,5,6,834,123, 99,32, 644 ] с помощью спискового включения - сформируйте новый список только из чётных элементов.

x = lambda i: i ** 2
print(x(5))
print(list(map(lambda i: i.upper(), ["I", "must", "learn", "coding", "in", "python"])))
print(list(map(lambda i: i.lower(), ["I", "STARTED", "LEARNING", "PYTHON"])))
my_list = lambda t=("I", "must", "learn", "coding", "in", "python"): t[-1]
print(my_list())
print(list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5, 6, 834, 123, 99, 32, 644])))





# my_list = lambda my_list_1 = ("I", "STARTED", "LEARNING", "PYTHON"):
# print(my_list())