import random
from collections import OrderedDict

# -------------------------------
# Helper
# -------------------------------
def remove_duplicates(s):
    return "".join(OrderedDict.fromkeys(s))


# -------------------------------
# Wumpus World (Environment)
# -------------------------------
class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [["" for _ in range(size)] for _ in range(size)]
        self.positions = []
        self.generate_world()

    def posgen(self):
        while True:
            r1 = random.randint(0, self.size - 1)
            r2 = random.randint(0, self.size - 1)
            if not (r1 == 0 and r2 == 0):
                return [r1, r2]

    def generate_world(self):
        # generate unique positions
        while len(self.positions) != 5:
            t = self.posgen()
            if t not in self.positions:
                self.positions.append(t)

        # assign entities
        self.grid[self.positions[0][0]][self.positions[0][1]] = "W"
        self.grid[self.positions[1][0]][self.positions[1][1]] = "P"
        self.grid[self.positions[2][0]][self.positions[2][1]] = "P"
        self.grid[self.positions[3][0]][self.positions[3][1]] = "P"
        self.grid[self.positions[4][0]][self.positions[4][1]] = "G"

        # start position
        self.grid[0][0] = "A"

        self.add_percepts()

    def in_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def add_percepts(self):
        for i in range(4):
            x, y = self.positions[i]

            condition = "S" if i == 0 else "B"

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.in_bounds(nx, ny):
                    self.grid[nx][ny] += condition

        # clean duplicates
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = remove_duplicates(self.grid[i][j])

    def get_cell(self, x, y):
        return self.grid[x][y]

    def debug_print(self):
        for row in self.grid:
            print(row)


# -------------------------------
# Player
# -------------------------------
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.alive = True
        self.has_gold = False

    def move(self, direction, size):
        if direction == "w":
            self.x -= 1
        elif direction == "s":
            self.x += 1
        elif direction == "a":
            self.y -= 1
        elif direction == "d":
            self.y += 1

        # clamp to bounds
        self.x = max(0, min(size - 1, self.x))
        self.y = max(0, min(size - 1, self.y))


# -------------------------------
# Game Controller
# -------------------------------
class Game:
    def __init__(self):
        self.world = WumpusWorld()
        self.player = Player()
        self.visited = [[False]*4 for _ in range(4)]

    def show_percepts(self):
        cell = self.world.get_cell(self.player.x, self.player.y)

        if "S" in cell:
            print("👃 Smell detected (Wumpus nearby)")
        if "B" in cell:
            print("💨 Breeze detected (Pit nearby)")

    def check_cell(self):
        cell = self.world.get_cell(self.player.x, self.player.y)

        if "W" in cell:
            print("💀 Wumpus got you!")
            self.player.alive = False

        elif "P" in cell:
            print("🕳️ Fell into a pit!")
            self.player.alive = False

        elif "G" in cell:
            print("🏆 You found GOLD!")
            self.player.has_gold = True

    def display_map(self):
        for i in range(4):
            row = []
            for j in range(4):
                if i == self.player.x and j == self.player.y:
                    row.append("A")
                elif self.visited[i][j]:
                    row.append(".")
                else:
                    row.append("?")
            print(row)

    def play(self):
        print("🎮 Welcome to Wumpus World!")

        while self.player.alive and not self.player.has_gold:
            self.visited[self.player.x][self.player.y] = True

            print("\nMap:")
            self.display_map()

            self.show_percepts()

            move = input("Move (W/A/S/D): ").lower()
            self.player.move(move, 4)

            self.check_cell()

        if self.player.has_gold:
            print("🎉 You Win!")
        else:
            print("Game Over!")

        print("\n🔍 Debug Grid (Full World):")
        self.world.debug_print()


# -------------------------------
# Run Game
# -------------------------------
if __name__ == "__main__":
    game = Game()
    game.play()