def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcd(a, b):
    return a * b // gcd(a, b)
    
def gcd1(numbers):
   for i in range(len(numbers)-1):
    numbers[i+1] = gcd(numbers[i], numbers[i+1])
   return numbers[-1]
   
def lcd1(numbers):
    for i in range(len(numbers) - 1):
        numbers[i + 1] = numbers[i] * numbers[i + 1] // gcd(numbers[i], numbers[i + 1])
    return numbers[-1]
    
def process_teleportation(command, numbers):
    try:
        if command == "sum":
            return sum(numbers)
        elif command == "average":
            return round(sum(numbers) / len(numbers), 2)
        elif command == "lcd":
            return lcd1(numbers)
        elif command == "gcd":
            return gcd1(numbers)
        elif command == "min":
            return min(numbers)
        elif command == "max":
            return max(numbers)
        else:
            raise ValueError("Invalid command")
    except ValueError as e:
        return str(e)

teleport_command = input().strip()
numbers = []

while True:
    num_input = input().strip()
    if num_input == "end":
        break
    numbers.append(int(num_input))

output_result = process_teleportation(teleport_command, numbers)
print(output_result)