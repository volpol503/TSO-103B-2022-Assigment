#4. Монетки
#Условие: В денежной системе есть монеты ценности: 10, 5, 2 и 1 рубль
#C клавиатуры вводится целое число X - сумма денег, которую вам нужно
#набрать

# Выведите на экран, какое количество монет каждой ценности нужно взять,
# чтобы набрать в сумме X и количество монет было наименьшим возможным

#Формат входных данных: На вход программе дается одно целое число X
#(1≤X≤10000)

#Формат выходных данных: Количество монет каждой ценности (сначала
#ценности 10, потом 5, 2 и 1) через пробел в одной строке

n = int(input())

decade = n // 10
n %= 10

fift = n // 5
n %= 5

duble = n // 2
n %= 2

singleone = n
print('  десятичные монеты: ',decade,'\n пятизначные монеты: ',fift,'\n двухзначные монеты: ',duble,'\n однозначные монеты: ',singleone)

