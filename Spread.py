from Person import Person
import numpy as np

FATALITY_RATE = 0.031


def _alive_or_dead(person):
    if np.random.rand() <= FATALITY_RATE:
        person.alive = False
        Person.totalDead += 1
    else:
        person.immune = True
        person.infected = False
    Person.currentlyInfected -= 1
    return person

def _test_people(People, accuracy, rate):
    for person in People:
        pass

def _spread_sickness(People):
    new_infected_person = np.random.randint(0, len(People))
    if not People[new_infected_person].immune and not People[new_infected_person].infected:
        People[new_infected_person].getSick()
    # print("Person {} just got {} sick".format(p, new_infected_person))
    return People

def forward_one_week(People, testing, accuracy, rate):
    for p in range(len(People)):
        if People[p].infected:
            if People[p].weeksSick > 0:
                People = _spread_sickness(People)

            if People[p].weeksSick == 2:
                People[p] = _alive_or_dead(People[p])
    for person in People:
        if person.infected:
            person.weeksSick += 1
    People = [person for person in People if person.alive]
    return People
