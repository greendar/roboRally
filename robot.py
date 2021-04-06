class Robot:
    def __init__(self, name, x = 0, y = 0, dir = 1):
        self.name = name
        self.x = x
        self.y = y
        self.dir = dir
        self.img = None
        self.moveMult = 0

    def nameFile(self):
        return f"UR{str(self.dir)}.png"

    def setMoveMult(self, gridSize):
        self.moveMult = gridSize


    def turnLeft(self):
        self.dir -=1
        if self.dir == -1:
            self.dir = 3

    def turnRight(self):
        self.dir +=1
        if self.dir == 4:
            self.dir = 0

    def moveRight(self):
        self.x += self.moveMult

    def moveDown(self):
        self.y += self.moveMult

    def moveLeft(self):
        self.x -= self.moveMult

    def moveUp(self):
        self.y -= self.moveMult

if __name__ == "__main__":
    r2d2 = Robot('R2D2')

    while True:
        choice = input("Left or Right")
        if choice == "L":
            r2d2.turnLeft()

        if choice == "R":
            r2d2.turnRight()

        print(r2d2.nameFile())
        print()
