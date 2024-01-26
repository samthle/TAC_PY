def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

def count_primes_in_range(start, end):
    return sum(1 for num in range(start, end + 1) if is_prime(num))

def main():
    a, b = map(int, input("Enter two integers separated by space: ").split())
    min_ab = min(a, b)
    max_ab = max(a, b)

    count_primes = count_primes_in_range(min_ab, max_ab)

    order = 'main' if a <= b else 'reverse'
    print(f'{order} order - amount: {count_primes}')

if __name__ == "__main__":
    main()
