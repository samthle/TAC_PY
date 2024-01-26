def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def calculate_gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

def calculate_lcm(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

def process_teleportation(command, numbers):
    try:
        if command == "sum":
            return sum(numbers)
        elif command == "average":
            return round(sum(numbers) / len(numbers), 2)
        elif command == "lcm":
            return calculate_lcm(numbers)
        elif command == "gcd":
            return calculate_gcd(numbers)
        elif command == "min":
            return min(numbers)
        elif command == "max":
            return max(numbers)
        else:
            raise ValueError("Invalid command")
    except ValueError as e:
        return str(e)

def main():
    teleport_command = input().strip()
    numbers = []

    while True:
        num_input = input().strip()
        if num_input == "end":
            break
        numbers.append(int(num_input))

    output_result = process_teleportation(teleport_command, numbers)
    print(output_result)

if __name__ == "__main__":
    main()
