#Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
#информацию из строки в словарь, найти среднее арифметическое оценок,
#результаты вывести на экран.
student = {}
inf = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'
inf = inf.split()
student['Фамилия'] = inf[0]
student['Имя'] = inf[1]
student['Группа'] = inf[2]
student['Оценки'] = []
for i in inf[3:]:
 student['Оценки'].append(int(i))
sr_ar = sum(student['Оценки'])/2
print(student)
print(sr_ar)

