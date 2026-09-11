ciphertext = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}"

key = "CYLAB"

plaintext = ""
key_index = 0

for char in ciphertext:
    if "A" <= char <= "Z":
        c = ord(char) - ord("A")
        k = ord(key[key_index % len(key)]) - ord("A")
        p = (c - k) % 26
        plaintext += chr(p + ord("A"))
        key_index += 1
    elif "a" <= char <= "z":
        c = ord(char) - ord("a")
        k = ord(key[key_index % len(key)]) - ord("A")
        p = (c - k) % 26
        plaintext += chr(p + ord("a"))
        key_index += 1
    else:
        plaintext += char

print(plaintext)
