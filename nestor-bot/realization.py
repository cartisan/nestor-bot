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
    return choice(("my {} is {}".format(vehicle.capitalize(), brokeverb),)).capitalize()

def realizeweapontext(weapon):
    wrong = allsynonyms('broken', ADJECTIVE)
    brokeverb = conjugate(choice(wrong), "3sgp")
    return choice(("my {} is {}".format(weapon.capitalize(), brokeverb),))

def realizegrouptext(group):
    wrong = allsynonyms('expel', VERB)
    expelverb = conjugate(choice(wrong), "3sgp")
    return choice(("I've been {} from the {}".format(expelverb, group.capitalize()),))


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

def realizejoingroup(group):
    joinword = choice(allsynonyms("join", VERB))
    return "you can {} the {}!".format(joinword, group.capitalize()).capitalize()

def realizevehicle(sad, vehicle, friend, solution):
    texts = [realizedepression(), realizevehicletext(vehicle)]
    shuffle(texts)
    return (correctspaces("{}: {}. {}".format(sad.title(), *texts)), 
                correctspaces("{}: {}".format(friend.title(), realizetakevehicle(solution))))

def realizeweapon(sad, weapon, friend, solution):
    texts = [realizedepression(), realizeweapontext(weapon)]
    shuffle(texts)
    return (correctspaces("{}: {}. {}".format(sad.title(), *texts)), 
                correctspaces("{}: {}".format(friend.title(), realizetakeweapon(solution))))

def realizegroupmembership(sad, weapon, friend, solution):
    texts = [realizedepression(), realizegrouptext(weapon)]
    shuffle(texts)
    return (correctspaces("{}: {}. {}".format(sad.title(), *texts)), 
                correctspaces("{}: {}".format(friend.title(), realizejoingroup(solution))))


print realizevehicle("batman", "batmobile", "robin", "motorbike")
print realizeweapon("obiwan", "lightsaber", "vader", "tie fighter")
print realizegroupmembership("luke skywalker", "jedi order", "vader", "sith")

