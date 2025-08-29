# kvadrat vsote - vsota kvadratov števil od 1 do 100

def vsota_kvadratov(n):
    vsota = 0
    for x in range(1, n + 1):
        vsota += x ** 2
    return vsota

def kvadrat_vsote(n):
    vsota = 0
    for x in range(1, n + 1):
        vsota += x
    return vsota ** 2

print(kvadrat_vsote(100) - vsota_kvadratov(100))