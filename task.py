# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

'''
number = int(input('Enter number of values: '))
numbers = range(number)
numbers_list = list(numbers)
for i in numbers_list:
    numbers_list[i]=(-3)**i
print(numbers_list)
'''

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''
def Generate_Values (numb):
    generate_list = {}                    # НЕ ПОНИМАЮ ПОЧЕМУ [] НЕ РАБОТАЕТ, А С {} РАБОТАЕТ!!!!(поле 2 лекции кажись понял)
    for i in range(1, numb+1):
        generate_list[i]=3*i+1
    return generate_list

number = int(input('Enter number of values: '))
total_numbers = Generate_Values(number)
print(total_numbers)
'''

# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

'''
def Count_element(row1, row2):                     # не смог до конца понять как это решилось посмотрел решения Сергея 
    count = 0                                      # сделал так же, и почему в 30 строке не можем просто поставить row1
    for i in range(0, len(row1)):
        if row1[i:i+len(row2)]==row2:
            count+=1
    return count


origin_list = "qwe, asd, zxc, qwe, ertqwe,    qwe, qwe, qwte"
Search_string_list = 'qwe'
if len(origin_list) > len(Search_string_list):
    print(Count_element(origin_list, Search_string_list))
else:
    print(Count_element(Search_string_list, origin_list))
'''

# Подсчитать сумму цифр в вещественном числе.

'''
def Sum_digits_of_number(numb):                    # Аллилуя решил сам!!!!!
    sum = 0
    numb_list = str(numb)
    New_numb_list = numb_list.replace('.', '')
    # print(New_numb_list)
    # print(type(New_numb_list))
    new_numb = int(New_numb_list)
    # print(new_numb)
    # print(type(new_numb))
    while new_numb != 0:
        sum += new_numb % 10
        new_numb //= 10
    return sum


print('Enter real number: ')
number = float(input())
total_sum = Sum_digits_of_number(number)
print(total_sum)
'''

# Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

'''
def factorial(numb):            # НЕ ПОЛУЧИЛОСЬ СДЕДАТЬ ТАК "пусть N = 4, тогда [ 1, 2, 6, 24 ]"
    product = 1
    number_list = list(range(1, numb+1))
    # print(number_list)
    for i in range(0, numb):
        # print(i)
        product*= number_list[i]
    return product


number = int(input())
# print(type(number))
total = print('factorial = ',factorial(number))
#print(total)
'''
