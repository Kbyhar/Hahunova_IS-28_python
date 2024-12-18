#Дано число A (>1). Вывести наибольшее из целых чисел K, для которых сумма 1 +
#1/2 + ... + 1/K будет меньше A, и саму эту сумму.

try:
    A = float(input("Введите число A (> 1): "))
    # Ввод числа A
    if A <= 1:
       raise ValueError("Число должно быть больше и не равно 1")
    # Ошибка если условие не выполняется
    K = 0
    #Инициализация переменной K
    b = 0
    #Инициализация переменной b
    while b < A:
        K = 1 + (1/2)
        b += 1 / K
        #Вычисления
    print(f"Наибольшее K: {K}")
    print(f"Сумма: {b}")
#вывод наибольшего К и суммы
except ValueError as c :
    print(f"Ошибка ввода:{c}")
    #Ошибка ввода

