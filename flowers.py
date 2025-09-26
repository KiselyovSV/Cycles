# l = "герань"
# c = "фикус"
# r = "крокус"
# days = int(input("Введите кол-во дней: "))
# for d in range(days):
#     c, r = r, c
#     l, c = c, l
# print(l, c, r)

l = "герань"
c = "фикус"
r = "крокус"
days = int(input("Введите кол-во дней: "))
if days % 3 == 0:
    print(l, c, r)
elif (days + 2) % 3 == 0:
    print(r, l, c)
else:
    print(c, r, l)
