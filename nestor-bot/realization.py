from pattern.en import wordnet
from pattern.en import conjugate
from pattern.en import ADJECTIVE, NOUN, VERB
from random import choice, shuffle, randrange
import re

def allsynonyms(word, kind = NOUN):
    return list(set([syn for s in wordnet.synsets(word, kind) for syn in s.synonyms]))

def realizevehicletext(vehicle):
    wrong = allsynonyms('broken', ADJECTIVE)
    brokeverb = conjugate(choice(wrong), "3sgp")
    return choice(("my {} is {}".format(vehicle.capitalize(), brokeverb),))

def realizeweapontext(vehicle):
    wrong = allsynonyms('broken', ADJECTIVE)
    brokeverb = conjugate(choice(wrong), "3sgp")
    return choice(("my {} is {}".format(vehicle.capitalize(), brokeverb),))

sadness = allsynonyms('depressed', ADJECTIVE)
def realizedepression():
    augmentative = choice(("so", ""))
    theproperty = choice(sadness)
    return "I'm {} {}".format(augmentative, theproperty).capitalize()

def correctspaces(text):
    return re.sub(" +", " ", text)

def realizetakevehicle(vehicle):
    takeword = choice(allsynonyms("borrow", VERB))
    return "you can {} my {}!".format(takeword, vehicle.capitalize()).capitalize()

def realizetakeweapon(vehicle):
    takeword = choice(allsynonyms("borrow", VERB))
    return "you can {} my {}!".format(takeword, vehicle.capitalize()).capitalize()

def realizevehicle(sad, vehicle, friend, solution):
    return (correctspaces("{}: {}. {}".format(sad.title(), realizedepression(), realizevehicletext(vehicle))), 
                correctspaces("{}: {}".format(friend.title(), realizetakevehicle(solution))))


def realizeweapon(sad, weapon, friend, solution):
    return (correctspaces("{}: {}. {}".format(sad.title(), realizedepression(), realizeweapontext(weapon))), 
                correctspaces("{}: {}".format(friend.title(), realizetakeweapon(solution))))


print realizevehicle("batman", "batmobile", "robin", "motorbike")
print realizeweapon("obiwan", "lightsaber", "vader", "tie fighter")

