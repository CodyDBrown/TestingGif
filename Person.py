class Person:

    totalInfected = 0
    totalDead = 0
    currentlyInfected = 0

    def __init__(self):
        self.infected = False
        self.tested = False
        self.immune = False
        self.alive = True
        self.weeksSick = 0

    def print_stats(self):
        print("infected: {}\talive: {}".format(self.infected, self.alive))
        return 0

    def getSick(self):
        self.infected = True
        Person.totalInfected += 1
        Person.currentlyInfected += 1
        return 0

