def find_house(post_codes, sum1):
    pairs = []
    for i in range(len(post_codes)):
        for j in range(i+1, len(post_codes)):
            if post_codes[i] + post_codes[j] == sum1:
                pairs.append((i, j))
    if len(pairs) > 0:
        result = [sum(pair) for pair in pairs]
        result.sort()
        for r in result:
            print(r)
    else:
        print("Not Found!")
        
input_post_codes = input()
input_sum1 = int(input())
post_codes = list(map(int, input_post_codes.split()))
find_house(post_codes, input_sum1)