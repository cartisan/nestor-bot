from cc_pattern.noc import noc
from random import randint

PROBLEM_TYPES = set(["Marital Status",
                     "Opponent",
                     "Vehicle of Choice",
                     "Weapon of Choice",
                     "Creator",
                     "Group Affiliation"])

people_count = len(noc)

# choose random charcter
person_number = randint(0, people_count-1)

actor = noc[person_number]

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
print problem
