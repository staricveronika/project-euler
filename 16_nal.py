# vsota števk 2 ** 1000
n = 2 ** 1000
vsota = 0
while n > 0:
    stevka = n % 10
    vsota += stevka
    n = n // 10

print(vsota)