"""
Define state predicates as following:
    Site(x,y): x is at y;
    Hang(w,y): w is hanging on y;
    On(z): z is standing on the box;
    Holds(z): bananas are held by z;
Define 4 operations:
    Goto(u,v): monkey goes to v from u;
    PushBox(v,w): monkey goes to w from v with boxes;
    ClimeBox: monkey climbs up box;
    Grasp: monkey gets the banana;

Define initial state:
    S_0 = Site(Monkey, a)
        && Hang(banana, b)
        && Site(Box, c)
        && !On(Monkey)
        && !Holds(Monkey)

Define final state:
    S_g = Site(Monkey, b)
        && !Hang(banana, b)
        && Site(Box, b)
        && On(Monkey)
        && Holds(Monkey)
"""


# Define the monkey class
class monkey:
    def __init__(self, site, On, Holds):
        self.site = site
        self.On = On
        self.Holds = Holds
        self.report()

    def report(self):
        print("Monkey is at", self.site)
        if self.On:
            print("Monkey is on the box.")
        else:
            print("Monkey is not on the box.")
        if self.Holds:
            print("Monkey holds the banana. Congratulations! ")
        else:
            print("Monkey does not hold the banana.")


# Define the box class
class box:
    def __init__(self, site):
        self.site = site
        self.report()

    def report(self):
        print("Box is at ", self.site)


# Define the banana class
class banana:
    def __init__(self, y):
        self.hang = y
        print("Banana is hanging on the " + y)


# Monkey goes to u from v
def Goto(monkey, u, v):
    print("|---------------------------------")
    print("|Action GOTO:")
    print("|        Monkey go to ", v, "from", u)
    print("|---------------------------------")
    if (~monkey.On) and (monkey.site == u):
        monkey.site = v
        monkey.report()
    else:
        print("No effect.")


# Monkey goes to v from w with box
def PushBox(monkey, box, v, w):
    print("|---------------------------------")
    print("|Action PushBox:")
    print("|        Monkey go to", w, "from", v, "with box")
    print("|---------------------------------")
    if ~monkey.On and monkey.site == v and box.site == v:
        monkey.site = w
        box.site = w
        monkey.report()
        box.report()
    else:
        print("No effect.")


# Monkey climbs up box
def ClimbBox(monkey, box):
    print("|---------------------------------")
    print("|Action ClimbBox:")
    print("|        Monkey climbs up the box")
    print("|---------------------------------")
    if monkey.site == box.site and ~monkey.On:
        monkey.On = True
        monkey.report()
        box.report()
    else:
        print("No effect.")


# Monkey tris to get banana
def Grasp(monkey, box, banana):
    print("|---------------------------------")
    print("|Action Grasp:")
    print("|        Monkey tris to get the banana.")
    print("|---------------------------------")
    if monkey.On and box.site == banana.hang:
        monkey.Holds = True
        monkey.report()
    else:
        print("No effect.")


def determine(monkey, box, banana, lace):
    flag = False
    for i in place:
        Goto(monkey, monkey.site, i)
        tempMonkey = monkey
        tempBox = box
        for j in place:
            tempMonkey1 = monkey
            tempBox1 = box

            PushBox(monkey, box, monkey.site, j)
            ClimbBox(monkey, box)
            Grasp(monkey, box, banana)
            if monkey.Holds and box.site == monkey.site and monkey.site == banana.hang:
                flag = True
                return flag

            monkey = tempMonkey1
            box = tempBox1
        monkey = tempMonkey
        box = tempBox
    if not flag:
        print("No solution.")


if __name__ == "__main__":
    print("Initial states:")
    Monkey = monkey("a", False, False)
    Box = box("c")
    Banana = banana("b")
    place = ["a", "b", "c"]
    determine(Monkey, Box, Banana)
