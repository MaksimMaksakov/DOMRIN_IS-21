#Дана строка '2020год - 16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая
#средние температуры по месяцам в году. Преобразовать информацию из строки в словарь,
#с использованием функции
#найти среднюю и минимальные температуры, результаты вывести на экран.
adidas = '-16 -10 -6 4 20 32 36 52 32 15 1 -15'
abibos = adidas.split()
bibra = 0
podik = abibos[1]
mesyats = {"январь":f"{abibos[0]}",
           "февраль":f"{abibos[1]}",
           "март":f"{abibos[2]}",
           "апрель":f"{abibos[3]}",
           "май":f"{abibos[4]}",
           "июнь":f"{abibos[5]}",
           "июль":f"{abibos[6]}",
           "август":f"{abibos[7]}",
           "сентябрь":f"{abibos[8]}",
           "октябрь":f"{abibos[9]}",
           "ноябрь":f"{abibos[10]}",
           "декабрь":f"{abibos[11]}", }
for i in range (11):
    bibra += int(abibos[i])
bibra = bibra/12
for s in range (11) :
    if podik > abibos[s]:
        podik = abibos [s]
print(bibra,podik)