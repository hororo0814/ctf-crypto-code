flag_enc = bytes.fromhex(
    "73e7a714676a81d9bd03339392733c7af01ccb2cdd9dd3d0dac14f90655b79db"
)

a_enc = bytes.fromhex(
    "e4652bae42f3610cd8c03eaf0c8373e3d6c7dec46574800e3df32176a7d92937"
)

known = b"A" * 32

key = bytes(a ^ b for a, b in zip(a_enc, known))

flag = bytes(a ^ b for a, b in zip(flag_enc, key))

print(flag.decode())
