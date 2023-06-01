def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Beispielaufruf
number = 3822016834723
factors = prime_factorization(number)
print("Die Primfaktoren der Zahl", number, "sind:", factors)