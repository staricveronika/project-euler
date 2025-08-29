# poišči vsoto vseh števil, ki so enaka vsoti fakultet svojih števk

def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n - 1)
    
curious = []

def seznam_stevk(n):
    stevke = []
    while n > 0:
        stevka = n % 10
        stevke.append(stevka)
        n = n // 10
    return stevke

def vsota_fakultet_stevk(n):
    stevkice_od_n = seznam_stevk(n)
    vsota_fakultet = 0
    while stevkice_od_n:
        vsota_fakultet += fakulteta(int(stevkice_od_n[0]))
        stevkice_od_n = stevkice_od_n[1:]
    return vsota_fakultet

kandidati = []
for i in range(10, 2540161):
    if i == vsota_fakultet_stevk(i):
        kandidati.append(i)

print(sum(kandidati))
        

