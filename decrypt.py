c1=0x78766a52455329b486aaa414c3a029834a7e4b6ed87019dce4056f4d8999b137404d9ec4df28da201c9b0bc142deb1d86ff94d83becc
c2=0x670b865216dfd0aacd5f7fa8802e704fa82f3fb9c7dbe3eb5a9ec308a1a2288648b15d5cc8ba2f54b245a972aea977932c9c84cf6422
c3=0x61d5f2a4298bff3d6ebcd78830fb9181d97235623819eb7c60b92dcdf836a6cf731c60187e72f471c05d1c6eab216c3f6032af3c5370
c4=0x3651009d02a0c72b9bc206c57d12277594d9eaad28bb3de5d661670b42f1cfafe688b9674e34d4ad79db898205417086e7e1877b9ef1
c5=0x96e51d4675c6be5b14ec0cf2a9e9a9610a99d632723b3f1fcfc6b36806f5d74045f47622817cc35f6ffe9afe29f0aa236cbe12371651

d = 0xaffe0815
n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBFFFEC000000000000000000000000000000000000000000000000019
n_len = n.bit_length() //8


def decrypt(c,d,n):
    t=pow(c,d,n)
    return t

print("="*108)
t1=decrypt(c1,d,n)
print(t1.to_bytes(n_len,"big").hex())
print("="*108)
t2=decrypt(c2,d,n)
print(t2.to_bytes(n_len,"big").hex())
print("="*108)
t3=decrypt(c3,d,n)
print(t3.to_bytes(n_len,"big").hex())
print("="*108)
t4=decrypt(c4,d,n)
print(t4.to_bytes(n_len,"big").hex())
print("="*108)
t5=decrypt(c5,d,n)
print(t5.to_bytes(n_len,"big").hex())