from Person import Person
import Spread
import cProfile
import argparse


def main(testing, accuracy, rate):
    TOTAL_POPULATION = 300000000
    US_CASES = 6008588
    People = []
    PatientZero = Person()
    People.append(PatientZero)
    weeks = 0
    while Person.totalInfected < US_CASES:

        People = Spread.forward_one_week(People, testing, accuracy, rate)
        weeks += 1
        print("***** After {} weeks the stats are *****".format(weeks))
        print("Total people infected:", Person.totalInfected)
        print("Currently Infected:", Person.currentlyInfected)
        print("Total dead:", Person.totalDead)
        assert(Person.currentlyInfected == len(People))
        print()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help="Profile the program to find bottle necks", default=False, type=bool)
    parser.add_argument('-t', type=bool, help="Turn on testing", default=False)
    parser.add_argument('-a', help="Accuracy of tests", type=float, default=0.95)
    parser.add_argument('-r', help="Rate of testing", type=float, default=0.5)
    args = parser.parse_args()
    print(args)
    if args.p:
        # Run basic main but with
        cProfile.run("main()", sort='cumtime')
    else:
        main(testing=args.t, accuracy=args.a, rate=args.r)
