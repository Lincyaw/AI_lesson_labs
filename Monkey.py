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
        print(" ")



class box:
    def __init__(self, site):
        self.site = site
        self.report()

    def report(self):
        print("Box is at ", self.site)
        print(" ")


class banana:
    def __init__(self, y):
        self.hang = y
        print("Banana is hanging on the" + y)
        print(" ")



def Goto(monkey, u, v):
    print("|---------------------------------")
    print("|Action GOTO:")
    print("|        Monkey go to ", u, "from",v)
    print("|---------------------------------")
    if (~monkey.On) and (monkey.site == u):
        monkey.site = v
    monkey.report()


def PushBox(monkey, box, v, w):
    print("|---------------------------------")
    print("|Action PushBox:")
    print("|        Monkey go to", v, "from",w,"with box")
    print("|---------------------------------")
    if ~monkey.On and monkey.site == v and box.site == v:
        monkey.site = w
        box.site = w
    monkey.report()
    box.report()


def ClimbBox(monkey, box):
    print("|---------------------------------")
    print("|Action ClimbBox:")
    print("|        Monkey climbs up the box")
    print("|---------------------------------")
    if monkey.site == box.site and ~monkey.On:
        monkey.On = True
    monkey.report()
    box.report()


def Grasp(monkey, box, banana):
    print("|---------------------------------")
    print("|Action Grasp:")
    print("|        Monkey gets the banana.")
    print("|---------------------------------")
    if monkey.On and box.site == banana.hang:
        monkey.Holds = True
        banana.hang = False
    monkey.report()


if __name__ == "__main__":
    print("Initial states:")
    Monkey = monkey("a", False, False)
    Box = box("c")
    Banana = banana("b")

    Goto(Monkey, Monkey.site, Box.site)
    PushBox(Monkey, Box, Box.site, Banana.hang)
    ClimbBox(Monkey, Box)
    Grasp(Monkey, Box, Banana)
