from cc_pattern.noc import noc as NOC
from text_pattern import TextPattern
from random import randint

PROBLEM_TYPES = set(["Marital Status",
                     "Opponent",
                     "Vehicle of Choice",
                     "Weapon of Choice",
                     "Creator",
                     "Group Affiliation"])


def choose_actor():
    people_count = len(NOC)

    # choose random charcter
    person_number = randint(0, people_count-1)

    actor = NOC[person_number]
    return actor


# TODO: Repeat until one is found?
def choose_problem(actor):
    # choose random problem
    # find missing entries:
    missing_properties = set()
    for k, v in actor.items():
        if type(v) == list:
            if not v[0]:
                missing_properties.add(k)
        else:
            if not v:
                missing_properties.add(k)

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

        partner = NOC[person_number]

    return partner


def generate_problem_tweet(actor, problem):
    # call function from pattern module
    pattern = TextPattern()
    problem_text = pattern.generate_problem_text(actor, problem)
    return problem_text.format(actor["Character"],actor[problem])


def generate_solution_tweet(partner,relationship, problem):
    pattern = TextPattern()
    problem_text = pattern.generate_solution_text(relationship, problem)
    return problem_text.format(partner["Character"],actor[problem])


actor = choose_actor()
problem = choose_problem(actor)
#print problem
problem_tweet = generate_problem_tweet(actor, problem)

partner = choose_partner(actor, problem)
solution_tweet = generate_solution_tweet(partner,"Opponent", problem)


print problem_tweet
print solution_tweet
