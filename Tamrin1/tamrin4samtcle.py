#by samtcle
def tashkhis_adad_aval(number):
    
    if number < 2:
    
        return False
    
    for i in range(2, int(number**0.5) + 1):
    
        if number % i == 0:
    
            return '0'
    
    return '1'

a, b = map(int, input().split())

count_prime_numbers = 0

minab = min(a, b)
maxab = max(a, b)

for number in range(minab, maxab + 1):

    if tashkhis_adad_aval(number) == '1':
    
        count_prime_numbers += 1


if a <= b:
    
    print(f'main order - amount: {count_prime_numbers}')

else:

    print(f'reverse order - amount: {count_prime_numbers}')
