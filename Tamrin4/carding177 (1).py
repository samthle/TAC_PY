def calculate_damage(card, damage_values):
    damage = 0
    for c in card:
        if c == 'A':
            damage += damage_values[0]
        elif c == 'B':
            damage += damage_values[1]
        elif c == 'C':
            damage += damage_values[2]
    return damage

def main():
    try:
        names = input("Enter space-separated names: ").split()
        healths = list(map(int, input("Enter space-separated healths: ").split()))
        damages = list(map(int, input("Enter space-separated damages: ").split()))
        cards = [['A', 'B'], ['B', 'C'], ['A', 'C']]

        scores = [calculate_damage(cards[i], damages) for i in range(3)]
        healths[0] -= scores[1]
        healths[1] -= scores[0]

        for i in range(2):
            print(f"{names[i]} -> Score: {scores[i] // 100}, Health: {healths[i]}")

    except ValueError:
        print("Invalid Command.")

if __name__ == "__main__":
    main()
