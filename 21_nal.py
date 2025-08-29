# a in b sta prijateljski števili, če vsota_deliteljev(a) = b in vsota_deliteljev(b) = a, in a != b
# delitelji so delitelji brez števila samega
# iščemo vsoto vseh prijateljskih števil pod 10000

def vsota_pravih_deliteljev(n):
    vsota = 1 # 1 je vedno delitelj
    for i in range(2, n):
        if n % i == 0:
            vsota += i
    return vsota

# poiščemo prijateljska števila do 10000
amicable = []
for a in range(2, 10000):
    b = vsota_pravih_deliteljev(a)
    if vsota_pravih_deliteljev(b) == a and a < b:
        amicable.append(a)
        amicable.append(b)

print(sum(amicable))