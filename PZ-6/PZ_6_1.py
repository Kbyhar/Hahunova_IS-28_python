#Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
#арифметическое всех элементов списка, кроме элементов с номерами от K до L
#включительно.

def chipi(spes, K, L):
    if not (0 <= K < L < len(spes)):
        #Проверяем коректность диапозона
        raise ValueError("Индексы K и L должны удовлетворять условию: 1 < K ≤ L ≤ N.")
    del_el = spes[:K] + spes[L+1:]
    #Формируем список удаляя К и L

    # Проверяем, что в списке остались элементы
    if not del_el:
        raise ValueError("После исключения диапазона K-L в списке не осталось элементов.")
    #проверяем остались ли в списке элементы
    sr_ar = sum(del_el) / len(del_el)
    #Вычислем среденее арифметическое
    return sr_ar

spes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#создаем список
K, L = 7, 8
#диапозон удаляемых индексов
try:
    resultat = chipi(spes, K, L)
    print(f"Список:{spes}")
    print(f"Среднее арифметическое списка: {resultat}")
except ValueError :
    print(f"Ошибка!")

