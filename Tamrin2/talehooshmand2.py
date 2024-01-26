def calculate_and_convert(lines):
    total_sum = 0
    valid_bases = set(range(2, 10))

    for line in lines:
        n, b = map(int, line.split())

        if 1 <= n <= 1000 and 2 <= b <= 9:
            divisors_sum = sum(i for i in range(1, n + 1) if n % i == 0)
            converted_number = int(str(divisors_sum), 10)  # Convert to base 10
            total_sum += converted_number
        else:
            return "Invalid base!"

        valid_bases.discard(b)

    if valid_bases:
        return "Invalid base!"

    return total_sum

def main():
    input_lines = ["5 3", "6 4", "-1 -1"]
    result = calculate_and_convert(input_lines)
    print(result)

if __name__ == "__main__":
    main()
