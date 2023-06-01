import hashlib

def mgf1(seed: bytes, length: int, hash_func=hashlib.sha1) -> bytes:
    hLen = hash_func().digest_size

    if length > (hLen << 32):
        raise ValueError("mask too long")
    T = b""

    counter = 0
    while len(T) < length:
        C = int.to_bytes(counter, 4, 'big')
        T += hash_func(seed + C).digest()
        counter += 1
    return T[:length]

mb= int("466f6f62617220313233343536373839",16)
b = bytes("aa1122fe0815beef", 'utf-8')
seed= int("aa1122fe0815beef",16)

def construct_mb(mb):
    mb_new= (0x1<<mb.bit_length()+1)|mb
    return mb_new

test1=mgf1(b,8)
hex_value = test1.hex()
print(hex_value)


def constr_enc_msg(seed,length,mb):
    mgf2=mgf1(seed,length)
    mgf1_hex=mgf2.hex()
    print(mgf1_hex)
    new_mb=mgf1_hex^construct_mb(mb)
    mb_byte=bytes(mb)
    mb_hex=mgf1(mb_byte,16)
    mask_seed=mb_hex^seed
    return mask_seed|new_mb

test=constr_enc_msg(b,8,mb)
print(test)

