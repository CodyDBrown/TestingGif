from Person import Person
import matplotlib.pyplot as plt
import Spread
import cProfile
import argparse


def main(testing=False, accuracy=0.95, rate=0.5):
    TOTAL_POPULATION = 10000000
    US_CASES = 6008588
    People = [Person() for _ in range(TOTAL_POPULATION)]
    People[0].getSick()
    weeks = 0
    totalInfected = []
    totalDead = []
    currentlyInfected = []
    while Person.currentlyInfected > 0 and Person.totalInfected < TOTAL_POPULATION:
        People = Spread.forward_one_week(People, testing, accuracy, rate)
        weeks += 1
        print("***** After {} weeks the stats are *****".format(weeks))
        print("Total people infected:", Person.totalInfected)
        print("Currently Infected:", Person.currentlyInfected)
        print("Total dead:", Person.totalDead)
        print()
        totalInfected.append(Person.totalInfected)
        totalDead.append(Person.totalDead)
        currentlyInfected.append(Person.currentlyInfected)
    plt.figure()
    plt.plot(range(weeks), totalInfected,
             range(weeks), totalDead,
             range(weeks), currentlyInfected)
    plt.legend(["Total Infected", "Total Dead", "Currently Infected"])
    plt.yscale("log")
    plt.xlabel("Weeks")
    plt.savefig("infection.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help="Profile the program to find bottle necks", default=False, type=bool)
    parser.add_argument('-t', type=bool, help="Turn on testing", default=False)
    parser.add_argument('-a', help="Accuracy of tests", type=float, default=0.95)
    parser.add_argument('-r', help="Rate of testing", type=float, default=0.5)
    args = parser.parse_args()
    print(args)
    if args.p:
        # Run basic main but with a time analyser
        cProfile.run("main()", sort='cumtime')
    else:
        main(testing=args.t, accuracy=args.a, rate=args.r)
