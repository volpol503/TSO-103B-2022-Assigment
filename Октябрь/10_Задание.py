#10. Положительное или отрицательное?

#Условие: Дано вещественное число x. Проверьте, является ли оно
#положительным или отрицательным.

#Формат входных данных: С клавиатуры вводится одно вещественное
#число x с точностью до трех знаков после десятичной точки. Гарантируется,
#что |x|≤1000; x≠0.

#Формат выходных данных: Требуется вывести «POSITIVE», если число
#является положительным, и «NEGATIVE», если отрицательным

x = float(input())
if x < 0:
    print('NEGATIVE')
else:
    print('POSITIVE')
