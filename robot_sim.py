# robot_sim.py
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 'N'
        print("[INIT] Robot starting at (0, 0), heading N")

    def move_forward(self, dist):
        print(f"[MOVE] Moving {dist} units forward")
        if self.heading == 'N':
            self.y += dist
        elif self.heading == 'S':
            self.y -= dist
        elif self.heading == 'E':
            self.x += dist
        elif self.heading == 'W':
            self.x -= dist
        print(f"    New position: ({self.x}, {self.y})")

    def turn(self, direction):
        directions = ['N', 'E', 'S', 'W']
        idx = directions.index(self.heading)
        if direction == 'right':
            self.heading = directions[(idx + 1) % 4]
        else:
            self.heading = directions[(idx - 1) % 4]
        print(f"[TURN] Turned {direction}, now heading {self.heading}")
