l = "герань"
c = "фикус"
r = "крокус"
days = int(input("Введите кол-во дней: "))
for d in range(days):
    c, r = r, c
    l, c = c, l
print(l, c, r)
