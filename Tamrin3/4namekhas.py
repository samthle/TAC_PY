def find_house(post_codes, target_sum):
    pairs = []

    # Iterate over all pairs of indices
    for i in range(len(post_codes)):
        for j in range(i + 1, len(post_codes)):
            if post_codes[i] + post_codes[j] == target_sum:
                pairs.append((i, j))

    if pairs:
        # Calculate sums of pairs and sort
        result = [sum(pair) for pair in pairs]
        result.sort()

        # Print the results
        for r in result:
            print(r)
    else:
        print("Not Found!")

def main():
    input_post_codes = input("Enter space-separated post codes: ")
    input_sum1 = int(input("Enter the target sum: "))
    post_codes = list(map(int, input_post_codes.split()))
    find_house(post_codes, input_sum1)

if __name__ == "__main__":
    main()
