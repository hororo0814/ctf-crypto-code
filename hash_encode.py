import hashlib

document = b"""The Large Hadron Collider (LHC) is the world's largest and highest-energy particle collider and the largest machine in the world. It was built by the European Organization for Nuclear Research (CERN) between 1998 and 2008 in collaboration with over 10,000 scientists and hundreds of universities and laboratories, as well as more than 100 countries."""
print(hashlib.md5(document).hexdigest())
