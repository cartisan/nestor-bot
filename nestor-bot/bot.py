from cc_pattern.noc import noc as NOC
from person import Person
from random import randint


PROBLEM_TYPES = set(["marital_status",
                     "opponent",
                     "vehicle_of_choice",
                     "weapon_of_choice",
                     "creator",
                     "group_affiliation"])


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
    return "{0}: I feel sad because of {1}.".format(actor.character[0],
                                                    getattr(actor, problem)[0])


def generate_solution_tweet(partner, problem):
    return "{0}: Cheer up!".format(partner.character[0])


actor = choose_actor()
problem = choose_problem(actor)
#print problem
problem_tweet = generate_problem_tweet(actor, problem)

partner = choose_partner(actor, problem)
solution_tweet = generate_solution_tweet(partner, problem)


print problem_tweet
print solution_tweet
