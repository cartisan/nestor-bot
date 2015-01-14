from cc_pattern.noc import noc as NOC
from person import Person
from text_pattern import TextPattern, PROBLEM_TYPES
from random import randint
from tweeter import Tweeter
import time


PROBLEM_TYPES = set(PROBLEM_TYPES)



def choose_actor():
    people_count = len(NOC)

    # choose random charcter
    person_number = randint(0, people_count-1)

    actor = Person(NOC[person_number])
    return actor


# TODO: Repeat until one is found?
def choose_problem(actor):
    # choose random problem
    missing_properties = actor.missing_attributes()

    # problems possible for our character
    possible_problems = list(PROBLEM_TYPES - missing_properties)

    problem = possible_problems[randint(0, len(possible_problems))-1]
    return problem


def choose_partner(actor, problem):
    people_count = len(NOC)
    partner = None

    #partner can't be the same as the actor
    while partner is None or partner == actor:
        # choose random charcter
        person_number = randint(0, people_count-1)

        partner = Person(NOC[person_number])

    return partner


def generate_problem_tweet(actor, problem):
    # call function from pattern module
    print problem
    pattern = TextPattern()
    problem_text = pattern.generate_problem_text(actor, problem)
    return problem_text.format(actor.character[0],getattr(actor,problem)[0])


def generate_solution_tweet(partner,relationship, problem):
    print problem
    pattern = TextPattern()
    problem_text = pattern.generate_solution_text(relationship,problem)
    
    tmp = partner.character[0]
    prob = getattr(partner,problem)[0]
    
    return problem_text.format(tmp,prob)


actor = choose_actor()
problem = choose_problem(actor)

#print problem
problem_tweet = generate_problem_tweet(actor, problem)

partner = choose_partner(actor, problem)

problem_2 = choose_problem(partner)
solution_tweet = generate_solution_tweet(partner,"opponent",problem)



print problem_tweet
print solution_tweet

 #To go online, make it True!
tweetme = True
if tweetme:
    twitt = Tweeter()
    twitt.tweetmessage(problem_tweet)
    time.sleep(30)
    twitt.tweetmessage(solution_tweet)
