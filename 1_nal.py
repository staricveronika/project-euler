# <p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
# <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
def sum_of_multiples_3_5(n): # n = zgornja meja
    sez = [] # seznam, v katerem bodo delitelji 3 in 5 - seznam ustvarimo izven zanke
    for x in range(1, n): # za vsa števila do n
        if (x % 3 == 0) or (x % 5 == 0): # če je število, manjše od n deljivo s 3 ali s 5
            sez.append(x) # ga dodamo v seznam

    return sum(sez)

print(sum_of_multiples_3_5(1000))
