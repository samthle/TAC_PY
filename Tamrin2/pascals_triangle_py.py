def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    for row in triangle:
        print(' '.join(map(str, row)))

def main():
    n = int(input("Enter the number of rows for Pascal's Triangle: "))
    generate_pascals_triangle(n)

if __name__ == "__main__":
    main()
