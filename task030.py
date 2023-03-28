# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести
# с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.




def arm_progr(a1, d, n: int):

    arithmetic_progression = []
    an = 0

    for i in range(n):
        an = a1 + i * d
        arithmetic_progression.append(an)
    return arithmetic_progression

input_a1 = int(input("Введите число a1(первый элемент):  "))
input_d = int(input("Введите число d(разность):  "))
input_n = int(input("Введите число n(кол-во элементов):  "))

print(arm_progr(input_a1, input_d, input_n))
