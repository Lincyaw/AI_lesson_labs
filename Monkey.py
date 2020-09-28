class Monkey:
    def __init__(self, pos):
        self.pos = pos

    def determine(self, banana, box):
        if self.pos[2] < banana[2]:
            self.find_box(box, True)
            self.find_box(banana, False)
        else:
            self.find_box(banana, False)

    def find_box(self, box, flag):
        while box != self.pos:
            temp = [box[0] - self.pos[0], box[1] - self.pos[1], box[2] - self.pos[2]]
            if temp[0] != 0:
                print("x + %d" % (temp[0] / abs(temp[0])))
                self.pos[0] += temp[0] / abs(temp[0])
            elif temp[1] != 0:
                print("y + %d" % (temp[1] / abs(temp[1])))
                self.pos[1] += temp[1] / abs(temp[1])
            elif temp[2] != 0:
                print("Can not reach.")
        self.pos[2] += 1
        if flag:
            print("Find the box.")
        else:
            print("Find the banana.")


if __name__ == "__main__":
    print("Please input coordinate as \"x y z\" forms.")
    monkey_pos = input("Input monkey postion: ")
    monkey_pos = [int(n) for n in monkey_pos.split()]
    monkey = Monkey(monkey_pos)
    banana = input("Input banana postion: ")  # [15, 4, 1]
    banana = [int(n) for n in banana.split()]
    box = input("Input box postion: ")  # [2, 4, 0]
    box = [int(n) for n in box.split()]

    monkey.determine(banana, box)
