def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def ord(a,b):
    for g in range(a, b):
        for k in range(a, b):
            if (g ** k) % (b-1) == 1:
                print(f"g={g}, k={k}")
                break



def find_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd == 1:
        return x % m
    else:
        raise ValueError("Inverse existiert nicht")

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


def square_and_multiply(base, exponent, modulus=None):
    result = 1
    if modulus is not None:
        base %= modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus if modulus else result * base

        base = (base * base) % modulus if modulus else base * base
        exponent //= 2

    return result

def mode(temp):

    if temp == "gcd":
        print("Input your two numbers")
        a=int(input())
        b=int(input())
        res=extended_gcd(a,b)
        print(res)

    if temp == "fac":
        print("Input the numbers you want to factorize")
        n=int(input())
        factors=prime_factorization(n)
        print(f"Die Primfaktoren sind {factors}")

    if temp == "findinverse":
        print("Input your Element in Field:")
        a=int(input())
        print("Input your Field:")
        b=int(input())
        res=find_inverse(a,b)
        print(f"The inverse of {a} in field {b} is {res}")

    if temp == "sqm":
        print("Input Base:")
        b=int(input())
        print("Input Exponent")
        e=int(input())
        print("Input modulus")
        m=int(input())
        erg=square_and_multiply(b,e,m)
        print(f"The result is {erg}")

    if temp == "ord":
        print("Input your field range:")
        a=int(input())
        b=int(input())
        ord(a,b)
        

print("Geben sie den Betriebsmodus ein: gcd, fac, sqm, findinverse, ord")
temp=input()
mode(temp)

