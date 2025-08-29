a, b = 1, 1
indeks = 2

while len(str(b)) < 1000:
    a, b = b, a + b
    indeks += 1

print(indeks)
