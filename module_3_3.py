def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)

#1.Функция с параметрами по умолчанию:
print_params()
print_params('Первая')
print_params(7, 8, 9)
print_params(b = 25)
print_params(c = [1, 2, 3])
print()

#2.Распаковка параметров:
values_list = [3, False, 'string']
values_dict = {'a':True, 'b': 456, 'c': "Inspector"}
print_params(*values_list)
print_params(**values_dict)
print()

#3.Распаковка + отдельные параметры:
values_list_2 = [9876, 'Training']
print_params(*values_list_2, 42)

