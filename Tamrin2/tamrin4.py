def create_maze(n, moves):
    maze = [['.' for _ in range(n)] for _ in range(n)]
    x, y = 0, 0

    for move in moves:
        if move == 'R':
            y += 1
        elif move == 'L':
            y -= 1
        elif move == 'B':
            x += 1

        if not (0 <= x < n and 0 <= y < n):
            print_maze(maze)
            print("There’s no way out!")
            return

        maze[x][y] = '*'

    print_maze(maze)

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

def main():
    n = int(input("Enter the number of columns (n): "))
    moves = []

    while True:
        move = input("Enter the next move (R/L/B) or END to finish: ")
        if move == "END":
            break
        moves.append(move)

    create_maze(n, moves)

if __name__ == "__main__":
    main()
