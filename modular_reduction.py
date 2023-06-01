print("<-Modulare Reduktion mit maximal 64 Bit großen Werten->")

rel, pol = input("Geben sie ihre erzeugende Relation und ihr Polynom getrennt von einem Leerzeichen in Hex ein:").split()
hex_rel = int(rel, 16)
hex_pol = int(pol, 16)

if len(bin(hex_rel)[2:]) > 64 or len(bin(hex_pol)[2:]) > 64:
    print("Die Eingabe ist größer als 64 Bit")
else:
    print("|Relation Basis 16 : {:>18}".format(hex(hex_rel)))
    print("|Länge in Bit      : {:>18}".format(len(bin(hex_rel)[2:])))
    print("|Polynom  Basis 16 : {:>18}".format(hex(hex_pol)))
    print("|Länge in Bit      : {:>18}".format(len(bin(hex_pol)[2:])))
    print("|===============================================")
    x=0
    while hex_rel.bit_length() >= hex_pol.bit_length():
        x+=1
        hex_rel ^= hex_pol << (hex_rel.bit_length() - hex_pol.bit_length())        
        print(f"|Hexwert nach dem {x}. Reduktionsschritt -> {hex(hex_rel)}")
        print("|===============================================")


