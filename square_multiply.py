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
base=2830193791865

exponent=2940009941077
modulus=3822016834723

erg=square_and_multiply(base, exponent,modulus)
print(erg)
