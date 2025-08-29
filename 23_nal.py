# perfect number - vsota pravih deliteljev je enaka številu
# deficient - vsota pravih deliteljev je manjša od števila
# abundant - vsota pravih deliteljev je večja od števila
# najti moramo vsoto vseh števil pod 28123, ki ne morejo biti zapisani kot vsota dveh abundant števil

def vsota_pravih_deliteljev(n):
    vsota = 1
    for x in range(2, n):
        if n % x == 0:
            vsota += x
    return vsota

# poiščemo abundant števila do 28123
seznam = []
for x in range(1, 28124):
    if vsota_pravih_deliteljev(x) > x:
        seznam.append(x)

# poiščemo vse vsote dveh abundant števil do 28123
sestevki = set()
for i in seznam:
    for j in seznam:
        if i + j <= 28123:
            sestevki.add(i + j)

# vsa števila, ki niso abundant
niso_abundant = []
for x in range(1, 28124):
    if x not in sestevki:
        niso_abundant.append(x)

print(sum(niso_abundant))
