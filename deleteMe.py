
class Robot:
    def __init__(self, dir):
        self.dir = dir

    def nameFile(self):
        return f"UR{str(self.dir)}.png"

    def turnLeft(self):
        r2d2.dir -=1
        if r2d2.dir == -1:
            r2d2.dir = 3

    def turnRight(self):
        r2d2.dir +=1
        if r2d2.dir == 4:
            r2d2.dir = 0





if __name__ == "__main__":
    r2d2 = Robot(0)

    while True:
        choice = input("Left or Right")
        if choice == "L":
            r2d2.turnLeft()

        if choice == "R":
            r2d2.turnRight()

        print(r2d2.nameFile())
        print()
