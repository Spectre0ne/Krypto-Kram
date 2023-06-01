def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def find_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd == 1:
        return x % m
    else:
        raise ValueError("Inverse existiert nicht")

# Beispielaufruf
element = 1070

körper = 1151
inverse = find_inverse(element, körper)
print("Das Inverse von", element, "im Körper", körper, "ist:", inverse)
