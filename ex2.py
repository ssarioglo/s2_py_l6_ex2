print("Введите натуральное число, x <= 2e9 (считает 2млрд очень долго)")
x = int(input())
cdel = 0 # количество делителей
print()
#for i in range (1, int(math.sqrt(x) + 1)):
for i in range (1, x):
    if x % i == 0:
        print(i)
        cdel += 1

print("Количество натуральных делителей:", cdel)