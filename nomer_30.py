# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def progres():
    # a, d, n = map(int, input("3 значения ").split())
    a = int(input("Введите начальное число "))
    d = int(input("Введите конечное число "))
    n = int(input("Введите колличество элементов "))
    sum=0
    lst=[]
    for i in range(1,n+1):
        sum = a+(i-1)*d
        lst.append(sum)
    print(*lst)

progres()