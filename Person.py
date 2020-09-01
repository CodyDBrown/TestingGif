class Person:

    totalInfected = 0
    totalDead = 0
    currentlyInfected = 0

    def __init__(self):
        self.infected = True
        self.tested = False
        self.testResults = None
        self.alive = True
        self.weeksSick = 0
        Person.totalInfected += 1
        Person.currentlyInfected += 1

    def print_stats(self):
        print("infected: {}\talive: {}".format(self.infected, self.alive))
