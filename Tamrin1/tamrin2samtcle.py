def add_with_bitwise_operations(x, y):
    while y != 0:
        tmp = x & y
        x = x ^ y
        y = tmp << 1
    return x

def main():
    n = int(input("Enter the first integer: "))
    m = int(input("Enter the second integer: "))
    
    result = add_with_bitwise_operations(n, m)

    k = int(input("Enter the target integer: "))

    print(result)
    print('YES' if result == k else 'NO')

if __name__ == "__main__":
    main()
