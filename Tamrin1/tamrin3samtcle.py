def convert_to_binary_string(num):
    return "{:032b}".format(num)

def main():
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    k = int(input("Enter the number of queries: "))

    binary_a = convert_to_binary_string(a)
    binary_b = convert_to_binary_string(b)

    combined_binary = binary_b + binary_a

    final_ans = ""
    for _ in range(k):
        mehman_x = int(input("Enter a query: "))

        if combined_binary[-mehman_x - 1] == '1':
            final_ans += '1'
        else:
            final_ans += '0'

    for bit in final_ans:
        print('yes' if bit == '1' else 'no')

if __name__ == "__main__":
    main()
