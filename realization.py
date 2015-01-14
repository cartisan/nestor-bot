from pattern.en import wordnet
from pattern.en import conjugate
from pattern.en import ADJECTIVE, NOUN
from random import choice, shuffle, randrange
import re

def allsynonyms(word, kind = NOUN):
    return list(set([syn for s in wordnet.synsets(word, kind) for syn in s.synonyms]))

def realizevehicletext(vehicle):
    wrong = allsynonyms('broken', ADJECTIVE)
    brokeverb = conjugate(choice(wrong), "3sgp")
    return choice(("my {} is {}".format(vehicle.capitalize(), brokeverb),))

sadness = allsynonyms('depressed', ADJECTIVE)

def realize(reason):

    augmentative = choice(("so", ""))
    theproperty = choice(sadness)
    mood = "I'm {} {}".format(augmentative, theproperty)

    sentences = [mood.capitalize(), reason.capitalize()]

    shuffle(sentences)

    return re.sub(" +", " ", "{}. {}.".format(*sentences))


def realizevehicle(vehicle):
    """
    how to call this function:

        print realizevehicle(name_of_vehicle)
    """
    return realize(realizevehicletext(vehicle))


print realizevehicle("batmobile")

