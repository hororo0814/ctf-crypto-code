import hashlib

text = "インターネット"

hash_value = hashlib.sha256(text.encode("utf-8")).hexdigest()

print(hash_value)
