for _ in range(4):
    print("Привет!", end = " ")

x_wall = 120
x_person = 10
while x_person < x_wall:
    x_person += 5
    print("хлоп")

sum = 0
while sum < 100:
    num = int(input("Введите число: "))
    if (sum + num) > 100: break
    sum += num
print(sum)