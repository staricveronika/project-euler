# vsota števk v 100!

def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n - 1)

stevilo = fakulteta(100)
vsota = 0
while stevilo > 0:
    stevka = stevilo % 10
    vsota += stevka
    stevilo = stevilo // 10

print(vsota)