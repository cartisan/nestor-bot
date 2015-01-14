from cc_pattern.noc import noc as NOC, parse, xlsx
from pattern.db import pd
from cc_pattern.noc import NAMES_INDEX, ROWS, assoc
from person import Person
from text_pattern import TextPattern, PROBLEM_TYPES
from random import randint, choice
from tweeter import Tweeter
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

def choose_one_random_actor():
    people_count = len(NOC)
    # choose random charcter
    person_number = randint(0, people_count-1)
    actor = Person(NOC[person_number])
    return actor

def choose_actor():
    # choose random charcter
    partners = []
    while not partners:
        actor = Person(choice(NOC))
        print("bot.py: Trying if {} has enough partners."
              .format(actor.character))
        partners = calculate_partners(actor)

    print "bot.py: Yes, he does!"
    return actor


def choose_problem(actor):
    # choose random problem
    missing_properties = actor.missing_attributes()

    # problems possible for our character
    possible_problems = list(PROBLEM_TYPES - missing_properties)

    problem = possible_problems[randint(0, len(possible_problems))-1]
    return problem


def partners_from_group(actor):
    prohibited_list = [actor.character[0]]
    partners = []

    #for each row
    for r in NOC:
        for v in r["Group Affiliation"]:
            for actor_group in actor.group_affiliation:
                if actor_group in v:
                    partner = create_person_from_name(r["Character"])
                    if not partner.character[0] in prohibited_list:
                        partners.append(partner)
                        prohibited_list.append(partner.character[0])

    #TODO: Identify only the important ones
    #right now only chance decision
    amount = min(2, len(partners))
    relevant_partners = []
    for i in range(amount):
        partner = choice(partners)
        relevant_partners.append(partner)
    return relevant_partners


def calculate_partners(actor, problem=None):
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

    if actor.group_affiliation and not problem == "group_affiliation":
        more_peeps = partners_from_group(actor)
        possible_partners += more_peeps

    return possible_partners


def choose_partner(actor, problem):
    possible_partners = calculate_partners(actor, problem)

    #add most similar character
    #print "bot.py: Start similarity computation for actor"
    #similar_partners = semantic_similarity(actor.character[0])

    print ("bot.py: num of partners is {}".format(len(possible_partners)))

    if possible_partners:
        return choice(possible_partners)

    partner = Person(choice(NOC))
    return partner

#### helpers to special vehicle break down path
def second_person_vehicle_weapon_breakdown(actor):
    pers = choose_one_random_actor()
    weapon = pers.weapon_of_choice[0]
    vehicle = actor.vehicle_of_choice[0]
    aff = get_affordance_of_vehicle(vehicle)
    return "{3}: I feel sad because I was hit by {1}'s {2} while {4} my {0}".format(vehicle, pers.character[0], weapon, actor.character[0], aff)

def get_affordance_of_vehicle(vehicle):
    VEH = parse("Veale's vehicle fleet.xlsx")
    for r in VEH:
        if r["Vehicle"] == vehicle:
            return r["Affordances"][0]
    return "getting errors in"
####



def generate_problem_tweet(actor, problem):
    # call function from pattern module
    #print problem
    if problem == "vehicle_of_choice" and randint(0,9)<3:
        return second_person_vehicle_weapon_breakdown(actor)
    else:
        pattern = TextPattern()
        problem_text = pattern.generate_problem_text(actor, problem)
        return problem_text.format(actor.character[0],getattr(actor,problem)[0])


def generate_solution_tweet(actor,partner,relationship,problem):
    actor_on_twitter = "@" + Tweeter().get_twitter_name(actor.character[0])
    # Every now and then the pattern about fiction...
    if actor.fictive_status and randint(0,9)<2:
        return "{0}: #{1}, Cheer up, you're just living in fiction all along!".format(partner.character[0], actor_on_twitter)
    #print problem
    pattern = TextPattern()
    problem_text = pattern.generate_solution_text(relationship,problem)

    tmp = partner.character[0]
    prob = getattr(partner,problem)[0]

    return problem_text.format(tmp,actor_on_twitter,prob)

def generate_problem_solution(actor,partner,actor_problem,partner_problem):
    if(problem == "vehicle_of_choice"):
        sol_prob = realizevehicle(actor,partner,actor_problem,partner_problem)
    elif(problem == "weapon_of_choice"):
        sol_prob = realizeweapon(actor,partner,actor_problem,partner_problem)
    elif(problem == "group_affiliation"):
        sol_prob = realizegroupmembership(actor,partner,actor_problem,partner_problem)
    return sol_prob


actor = choose_actor()
problem = choose_problem(actor)

#print problem
problem_tweet = generate_problem_tweet(actor, problem)

partner = choose_partner(actor, problem)

problem_2 = choose_problem(partner)
solution_tweet = generate_solution_tweet(actor,partner,"opponent",problem)
call_repo = generate_problem_solution(actor.character[0],getattr(actor,problem)[0],partner.character[0],getattr(partner,problem)[0])

problem_list = [call_repo[1],problem_tweet]
solution_list = [call_repo[0],solution_tweet]

print problem_list[1]
print solution_list[1]

# To go online, make it True!
tweetme = True
if tweetme:
    twitt = Tweeter()
    distressed_tweet = problem_list[1]
    consoling_tweet = solution_list[1]
    
    twitt.tweet_it_all(actor, distressed_tweet, partner, consoling_tweet)
    
