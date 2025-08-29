# pitagorejska trojica z vsoto 1000
# a ** 2 + b ** 2 = c ** 2
# a + b + c = 1000

for a in range(1, 1000):
    for b in range(a + 1, 1000 - a): # b večji od a
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c)
            print(a * b * c)
