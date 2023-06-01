import hashlib


s="aa1122fe0815beef"
e= 65537
n= 0xAF5466C26A6B662AC98C06023501C9DF6036B065BD1F6804B1FC86307718DA4048211FD68A06917DE6F81DC018DCAF84B38AB77A6538BA2FE6664D3FB81E4A0886BBCDAB071AD6823FE20DF1CD67D33FB6CC5DA519F69B11F3D48534074A83F03A5A9545427720A30A27432E94970155A026572E358072023061AF65A2A18E85

def mgf1(seed: bytes, length: int, hash_func=hashlib.sha256) -> bytes:
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

def to_bytes(x):
    temp1: bytearray = bytearray.fromhex(x)
    return temp1


def construct_mb(mb):
    mb_new= mb|0x1<<mb.bit_length()+1
    return mb_new


def oaep(seed,length,length1,mb):
    tmp=to_bytes(seed)    
    dbmask=int((mgf1(tmp, length).hex()),16)
    newmb=construct_mb(mb)
    maskedmb=dbmask^newmb
    tmp1 = maskedmb.to_bytes(119, 'big')
    seedmask=int((mgf1(tmp1, length1).hex()),16)
    seedtmp=int(seed,16)
    maskedseed=seedtmp^seedmask
    oaep=0x00<<(maskedseed.bit_length())+(maskedmb.bit_length())|maskedseed<<maskedmb.bit_length()|maskedmb
    p=pow(oaep,e,n)

    print(f"Datablockmask: {hex(dbmask)}")
    print("=============================================================")
    print(f"Seedmask: {hex(seedmask)}")
    print("=============================================================")
    print(f"Masked Datablock: {hex(maskedmb)}")
    print("=============================================================")
    print(f"Masked seed: {hex(maskedseed)}")
    print("=============================================================")
    print(f"OAEP:{hex(oaep)}")    
    print("=============================================================")
    print(f"P:{hex(p)}")
    print("=============================================================")


input=input("Inout your message, keep it short!\n")
mb1 = input.encode().hex()
mb=int(mb1,16)
print(hex(mb))
oaep(s,119,8,mb)
