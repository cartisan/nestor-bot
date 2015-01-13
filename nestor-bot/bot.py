from cc_pattern.noc import noc
from random import randint

people_count = len(noc)

# choose random charcter
person_number = randint(0, people_count-1)

# mock the number for development
person_number = 0

actor = noc[person_number]
print actor

