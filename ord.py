for g in range(1, 12):
    for k in range(1, 12):
        if (g ** k) % 11 == 1:
            print(f"g={g}, k={k}")
            break

def ord(a,b):
    for g in range(a, b):
        for k in range(a, b):
            if (g ** k) % (b-1) == 1:
                print(f"g={g}, k={k}")
                break

