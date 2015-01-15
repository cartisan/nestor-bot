from pattern.en import wordnet
from pattern.en import conjugate
from pattern.en import ADJECTIVE, NOUN, VERB
from random import choice, shuffle, randrange
import re

def allsynonyms(word, kind = NOUN):
    return list(set([syn for s in wordnet.synsets(word, kind) for syn in s.synonyms]))

def realizevehicletext(vehicle):
    wrong = allsynonyms('broken', ADJECTIVE)
    brokeverb = choice(wrong)
    return choice(("My {} is {}".format(vehicle, brokeverb),))

def realizeweapontext(weapon):
    wrong = allsynonyms('redundant', ADJECTIVE)
    brokenverbinf = choice(wrong)
    return choice(("My {} is {}".format(weapon, brokenverbinf),))

def realizegrouptext(group):
    wrong = allsynonyms('expel', VERB)
    expelverbinf = choice(wrong)
    expelverb = ""
    expelverbfin = ""
    if(len(expelverb.split(" ")) == 1):
        expelverb = conjugate(expelverbinf, "3sgp")
        expelverbfin = expelverb
    elif(len(expelverb.split(" ")) == 2):
        print "auxiliary"
        expelverb2part = expelverb.split(" ")
        expelverb = conjugate(expelverb2part[0], "3sgp")
        expelverbfin = expelverb + " " + expelverb2part[1]
    return choice(("I've been {} from {}".format(expelverbfin, group.lower()),))


sadness = allsynonyms('depressed', ADJECTIVE)
def realizedepression():
    augmentative = choice(("really", ""))
    theproperty = choice(sadness)
    return "I'm feeling {} {}".format(augmentative, theproperty)

def correctspaces(text):
    return re.sub(" +", " ", text)

def realizetakevehicle(vehicle):
    takeword = choice(allsynonyms("borrow", VERB))
    return "you can {} my {}!".format(takeword, vehicle.lower())

def realizetakeweapon(vehicle):
    takeword = choice(allsynonyms("borrow", VERB))
    return "you can {} my {}!".format(takeword, vehicle.lower())

def realizejoingroup(group):
    joinword = choice(allsynonyms("join", VERB))
    return "you can {} the {}!".format(joinword, group.lower())

def realizevehicle(sad, vehicle, friend, solution):
    texts = [realizedepression(), realizevehicletext(vehicle)]
    shuffle(texts)
    return (correctspaces("{}: {}. {}.".format(sad.title(), *texts)), 
                correctspaces("{}: {}".format(friend.title(), realizetakevehicle(solution))))

def realizeweapon(sad, weapon, friend, solution):
    texts = [realizedepression(), realizeweapontext(weapon)]
    shuffle(texts)
    return (correctspaces("{}: {}. {}.".format(sad.title(), *texts)), 
                correctspaces("{}: {}".format(friend.title(), realizetakeweapon(solution))))

def realizegroupmembership(sad, weapon, friend, solution):
    texts = [realizedepression(), realizegrouptext(weapon)]
    shuffle(texts)
    return (correctspaces("{}: {}. {}.".format(sad.title(), *texts)), 
                correctspaces("{}: {}".format(friend.title(), realizejoingroup(solution))))


#print realizevehicle("batman", "batmobile", "robin", "motorbike")
#print realizeweapon("obiwan", "lightsaber", "vader", "tie fighter")
#print realizegroupmembership("luke skywalker", "jedi order", "vader", "sith")

