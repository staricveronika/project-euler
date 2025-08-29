# najdaljše collatzovo zaporedje števila pod 1 mio

def naslednji_clen(n):
    while n > 0:
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1
        
def dolzina_zaporedja(n):
    cleni = 1
    while n != 1:
        cleni += 1
        n = naslednji_clen(n)
    return cleni

def najdaljse_zaporedje(m, n):
    max_dolzina = 0
    stevilo = 0
    for k in range(m, n + 1):
        d = dolzina_zaporedja(k)
        if d > max_dolzina:
            max_dolzina = d
            stevilo = k
    return stevilo, max_dolzina


print(najdaljse_zaporedje(1, 1000000))
