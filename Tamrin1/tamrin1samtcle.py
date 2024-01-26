def num_to_bin_string(num):
    return "{:064b}".format(num)

def count_set_bits(binary_string):
    return sum(1 for bit in binary_string if bit == '1')

def main():
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))

    xor_result = a ^ b
    binary_difference = num_to_bin_string(xor_result)
    set_bits_count = count_set_bits(binary_difference)

    print("The number of differing bits is:", set_bits_count)

if __name__ == "__main__":
    main()
