def create_secret_message(v1):
    v2 = v1.split()
    v3 = sorted(v2, key=lambda x: int(x[1:]))
    secret_message = ''.join([char[0] for char in v3])
    return secret_message

def main():
    v1 = input("Enter space-separated strings: ")
    result = create_secret_message(v1)
    print(result)

if __name__ == "__main__":
    main()
