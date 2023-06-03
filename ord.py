for g in range(1, 12):
    for k in range(1, 12):
        if (g ** k) % 11 == 1:
            print(f"g={g}, k={k}")
            break