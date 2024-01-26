class Soldier:
    def __init__(self, soldier_type, soldier_id, x, y):
        self.type = soldier_type
        self.id = soldier_id
        self.health = 100
        self.x = x
        self.y = y

class Game:
    def __init__(self, n):
        self.board_size = n
        self.players = {'archer': [], 'melee': []}

    def new_soldier(self, soldier_type, soldier_id, x, y):
        if soldier_id in [s.id for s in self.players['archer'] + self.players['melee']]:
            print("duplicate tag")
        elif x >= self.board_size or y >= self.board_size:
            print("out of bounds")
        else:
            new_soldier = Soldier(soldier_type, soldier_id, x, y)
            self.players[soldier_type].append(new_soldier)

    def move_soldier(self, soldier_id, direction):
        for soldier_type in self.players:
            for soldier in self.players[soldier_type]:
                if soldier.id == soldier_id:
                    if direction == "up" and soldier.y > 0:
                        soldier.y -= 1
                    elif direction == "down" and soldier.y < self.board_size - 1:
                        soldier.y += 1
                    elif direction == "left" and soldier.x > 0:
                        soldier.x -= 1
                    elif direction == "right" and soldier.x < self.board_size - 1:
                        soldier.x += 1
                    else:
                        print("out of bounds")
                    return
        print("soldier does not exist")

    def attack(self, attacker_id, target_id):
        for attacker_type in self.players:
            for attacker in self.players[attacker_type]:
                if attacker.id == attacker_id:
                    for target_type in self.players:
                        for target in self.players[target_type]:
                            if target.id == target_id:
                                distance = abs(attacker.x - target.x) + abs(attacker.y - target.y)
                                if attacker_type == "archer" and distance > 2:
                                    print("the target is too far")
                                elif attacker_type == "melee" and distance > 1:
                                    print("the target is too far")
                                else:
                                    if attacker_type == "archer":
                                        target.health -= 10
                                    elif attacker_type == "melee":
                                        target.health -= 20

                                    if target.health <= 0:
                                        self.players[target_type].remove(target)
                                        print("target eliminated")
                                    return
                    print("soldier does not exist")
                    return
        print("soldier does not exist")

    def get_info(self, soldier_id):
        for soldier_type in self.players:
            for soldier in self.players[soldier_type]:
                if soldier.id == soldier_id:
                    print(f"health: {soldier.health}")
                    print(f"location: {soldier.x} {soldier.y}")
                    return
        print("soldier does not exist")

    def game_status(self):
        archer_health = sum([soldier.health for soldier in self.players['archer']])
        melee_health = sum([soldier.health for soldier in self.players['melee']])

        if archer_health > melee_health:
            return "archer"
        elif archer_health < melee_health:
            return "melee"
        else:
            return "draw"
            
n = int(input())
game = Game(n)

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
