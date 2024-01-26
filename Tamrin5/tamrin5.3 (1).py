class Soldier:
    def __init__(self, soldier_type, soldier_id, x, y):
        self.type = soldier_type
        self.id = soldier_id
        self.health = 100
        self.x = x
        self.y = y

class Game:
    def __init__(self, board_size):
        self.board_size = board_size
        self.players = {'archer': [], 'melee': []}

    def new_soldier(self, soldier_type, soldier_id, x, y):
        if self._is_duplicate_tag(soldier_id) or not self._is_within_bounds(x, y):
            return
        new_soldier = Soldier(soldier_type, soldier_id, x, y)
        self.players[soldier_type].append(new_soldier)

    def move_soldier(self, soldier_id, direction):
        soldier = self._find_soldier_by_id(soldier_id)
        if soldier:
            if self._is_valid_movement(soldier, direction):
                self._update_soldier_position(soldier, direction)
            else:
                print("out of bounds")

    def attack(self, attacker_id, target_id):
        attacker = self._find_soldier_by_id(attacker_id)
        target = self._find_soldier_by_id(target_id)
        
        if not attacker or not target:
            print("soldier does not exist")
            return

        distance = abs(attacker.x - target.x) + abs(attacker.y - target.y)
        if not self._is_valid_attack(attacker.type, distance):
            return

        self._perform_attack(attacker, target)

    def get_info(self, soldier_id):
        soldier = self._find_soldier_by_id(soldier_id)
        if soldier:
            print(f"health: {soldier.health}")
            print(f"location: {soldier.x} {soldier.y}")
        else:
            print("soldier does not exist")

    def game_status(self):
        archer_health = sum(soldier.health for soldier in self.players['archer'])
        melee_health = sum(soldier.health for soldier in self.players['melee'])

        if archer_health > melee_health:
            return "archer"
        elif archer_health < melee_health:
            return "melee"
        else:
            return "draw"

    def _is_duplicate_tag(self, soldier_id):
        return soldier_id in [s.id for s in self.players['archer'] + self.players['melee']]

    def _is_within_bounds(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def _find_soldier_by_id(self, soldier_id):
        for soldier_type in self.players:
            for soldier in self.players[soldier_type]:
                if soldier.id == soldier_id:
                    return soldier
        return None

    def _is_valid_movement(self, soldier, direction):
        if direction == "up" and soldier.y > 0:
            return True
        elif direction == "down" and soldier.y < self.board_size - 1:
            return True
        elif direction == "left" and soldier.x > 0:
            return True
        elif direction == "right" and soldier.x < self.board_size - 1:
            return True
        return False

    def _update_soldier_position(self, soldier, direction):
        if direction == "up":
            soldier.y -= 1
        elif direction == "down":
            soldier.y += 1
        elif direction == "left":
            soldier.x -= 1
        elif direction == "right":
            soldier.x += 1

    def _is_valid_attack(self, attacker_type, distance):
        if attacker_type == "archer" and distance > 2:
            print("the target is too far")
            return False
        elif attacker_type == "melee" and distance > 1:
            print("the target is too far")
            return False
        return True

    def _perform_attack(self, attacker, target):
        if attacker.type == "archer":
            target.health -= 10
        elif attacker.type == "melee":
            target.health -= 20

        if target.health <= 0:
            self.players[target.type].remove(target)
            print("target eliminated")


def main():
    board_size = int(input())
    game = Game(board_size)

    while True:
        command = input().split()
        if command[0] == "new":
            game.new_soldier(command[1], int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "move":
            game.move_soldier(int(command[1]), command[2])
        elif command[0] == "attack":
            game.attack(int(command[1]), int(command[2]))
        elif command[0] == "info":
            game.get_info(int(command[1]))
        elif command[0] == "who":
            print(game.game_status())
        elif command[0] == "end":
            break


if __name__ == "__main__":
    main()
