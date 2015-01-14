from cc_pattern.noc import noc as NOC
from cc_pattern.noc import NAMES_INDEX, ROWS, assoc
from person import Person
from text_pattern import TextPattern, PROBLEM_TYPES
from random import randint, choice
from tweeter import Tweeter
import time
from realization import realizevehicle
from realization import realizeweapon
from realization import realizegroupmembership

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
    # choose random charcter
    partners = []
    while not partners:
        actor = Person(choice(NOC))
        print("bot.py: Trying if {} has enough partners."
              .format(actor.character))
        partners = calculate_partners(actor)

    print "bot.py: Yes, he does!"
    return actor, partners


def choose_problem(actor):
    # choose random problem
    missing_properties = actor.missing_attributes()

    # problems possible for our character
    possible_problems = list(PROBLEM_TYPES - missing_properties)

    problem = possible_problems[randint(0, len(possible_problems))-1]
    return problem


def calculate_partners(actor):
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

    return possible_partners


def choose_partner(actor, partners):
    possible_partners = partners

    #add most similar character
    #print "bot.py: Start similarity computation for actor"
    #similar_partners = semantic_similarity(actor.character[0])

    print ("bot.py: num of partners is {}".format(len(possible_partners)))

    if possible_partners:
        return choice(possible_partners)

    partner = Person(choice(NOC))
    return partner


def generate_problem_tweet(actor, problem):
    # call function from pattern module
    #print problem
    pattern = TextPattern()
    problem_text = pattern.generate_problem_text(actor, problem)
    return problem_text.format(actor.character[0],getattr(actor,problem)[0])


def generate_solution_tweet(actor,partner,relationship,problem):
    #print problem
    pattern = TextPattern()
    problem_text = pattern.generate_solution_text(relationship,problem)
    
    tmp = partner.character[0]
    prob = getattr(partner,problem)[0]
    actor_name = actor.character[0].replace(" ","")
    
    return problem_text.format(tmp,actor_name,prob)
    
def generate_problem_solution(actor,partner,actor_problem,partner_problem):
    if(problem == "vehicle_of_choice"):
        sol_prob = realizevehicle(actor,partner,actor_problem,partner_problem)
    elif(problem == "weapon_of_choice"):
        sol_prob = realizeweapon(actor,partner,actor_problem,partner_problem)
    elif(problem == "group_affiliation"):
        sol_prob = realizegroupmembership(actor,partner,actor_problem,partner_problem)
    return sol_prob


actor, partners = choose_actor()
problem = choose_problem(actor)

#print problem
problem_tweet = generate_problem_tweet(actor, problem)

partner = choose_partner(actor, partners)

problem_2 = choose_problem(partner)
solution_tweet = generate_solution_tweet(actor,partner,"opponent",problem)
call_repo = generate_problem_solution(actor.character[0],getattr(actor,problem)[0],partner.character[0],getattr(partner,problem)[0])

problem_list = [call_repo[1],solution_tweet]
solution_list = [call_repo[0],problem_tweet]

#print problem_tweet
#print solution_tweet
print call_repo[0]
print call_repo[1]

# To go online, make it True!
tweetme = True
if tweetme:
    twitt = Tweeter()
    distressed_tweet = problem_list[1]
    consoling_tweet = solution_list[1]
    
    tweet_it_all(actor, distressed_tweet, partner, consoling_tweet)
    
    
