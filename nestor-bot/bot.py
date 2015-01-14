from cc_pattern.noc import noc as NOC
from cc_pattern.noc import NAMES_INDEX, ROWS, assoc
from person import Person
from text_pattern import TextPattern, PROBLEM_TYPES
from random import randint, choice


PROBLEM_TYPES = set(PROBLEM_TYPES)
RELATION_TYPES = set(["opponent",
                      "creator",
                      "portrayed_by"])


def create_person_from_name(name):
    for i, row in enumerate(NOC):
        if name == row["Character"]:
            return Person(row)
    raise Exception("Name {} not found".format(name))


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
    # only use relations that actor does have
    possible_relations = RELATION_TYPES - actor.missing_attributes()

    # for each relation get a list of names
    #thus possible names is a list of lists
    possible_names = [getattr(actor, relation)
                      for relation in possible_relations]
    #flatten the list of lists
    possible_names = [item for sublist in possible_names
                      for item in sublist]

    possible_partners = []
    for name in possible_names:
        if name in NAMES_INDEX.keys():
            partner = create_person_from_name(name)
            possible_partners.append(partner)

    print ("bot.py: num of partners is {}".format(len(possible_partners)))

    if possible_partners:
        return choice(possible_partners)

    partner = Person(choice(NOC))
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
