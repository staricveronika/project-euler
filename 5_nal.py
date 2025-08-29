# najmanjše pozitivno število, ki je deljivo z vsemi števili od 1 do 20
import math

def najmanjsi_skupni_veckratnik(a, b):
    """Vrne lcm dveh števil po formuli."""
    return a * b // math.gcd(a, b)

def najmanjsi_range(n):
    """Poišče najmanjše število, ki je deljivo z vsemi števili od 1 do n."""
    rezultat = 1
    for x in range(1, n + 1):
        rezultat = najmanjsi_skupni_veckratnik(rezultat, x) 
        # najmanjše število, ki je deljivo z vsemi do tega trenutka
    return rezultat

print(najmanjsi_range(20))