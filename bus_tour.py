print("\nBus_tour start")
height = 4.37
# num_bridges = int(input("Введите количество мостов от 1 до 1000 шт.: "))
bridges = input("Через пробел введите высоты мостов ( до 10 метров вкл.):\n ")
separated_bridges = bridges.split()
counter = 0
mes = "No crash"
for i in separated_bridges:
    counter += 1
    if float(i) > 10:
        print("Недопустимая высота моста!")
        mes = ""
        break
    elif float(i) <= height:
        print(f"Crash {counter}")
        mes = ""
        break
print(mes)
