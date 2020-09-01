from Person import Person
import numpy as np

FATALITY_RATE = 0.031


def _alive_or_dead(person):
    person.infected = False
    Person.currentlyInfected -= 1
    if np.random.rand() <= FATALITY_RATE:
        person.alive = False
        Person.totalDead += 1

def _test_people(People, accuracy, rate):
    for person in People:


def forward_one_week(People, testing, accuracy, rate):
    new_infections = []
    if testing:
        _test_people(People, accuracy, rate)
    for person in People:
        if person.alive and person.infected and not person.tested:
            new_infections.append(Person())
        person.weeksSick += 1
        if person.weeksSick >= 2:
            _alive_or_dead(person)

    People = [person for person in People if person.infected]
    People.extend(new_infections)
    return People
