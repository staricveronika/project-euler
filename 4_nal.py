# <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
# <p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

def je_palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    
najvecji = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        produkt = i * j # preverimo vse produkte trimestnih števil
        if je_palindrom(produkt) and produkt > najvecji:
            najvecji = produkt

print(najvecji)