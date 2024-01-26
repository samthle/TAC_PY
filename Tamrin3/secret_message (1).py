v1 = input()

v2 = v1.split()

v3 = sorted(v2, key=lambda x: int(x[1:]))

secret_message = ''.join([char[0] for char in v3])

print(secret_message)
