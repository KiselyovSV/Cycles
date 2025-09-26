# print("\nBus_tour start")
# height = 4.37
# # num_bridges = int(input("Введите количество мостов от 1 до 1000 шт.: "))
# bridges = input("Через пробел введите высоты мостов ( до 10 метров вкл.):\n ")
# separated_bridges = bridges.split()
# counter = 0
# mes = "No crash"
# for i in separated_bridges:
#     counter += 1
#     if float(i) > 10:
#         mes = "Недопустимая высота моста!")
#         break
#     elif float(i) <= height:
#         mes = f"Crash {counter}"
#         break
# print(mes)

print("\nBus_tour start")
bus_height = 4.37
num_bridges = int(input("Введите количество мостов от 1 до 1000 шт.: "))
counter = 0
mes = "No crash"
for i in range(num_bridges):
    bridge_heigh = float(input(f"Введите высоту моста № {i} ( до 10 метров вкл.):\n "))
    counter += 1
    if bridge_heigh <= bus_height:
        mes = f"Crash {counter}"
        break
print(mes)