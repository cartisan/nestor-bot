from cc_pattern.noc import noc
from cc_pattern.noc import NAMES_INDEX, ROWS, assoc
from person import Person


RELATION_TYPES = set([#"marital_status",
                      "opponent",
                      "creator",
                      "portrayed_by"])


def create_person_from_name(name):
    for i, row in enumerate(noc):
        if name == row["Character"]:
            return Person(row)
    raise Exception("Name {} not found".format(name))


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

    return possible_partners

linked_people = []
for pers_dat in noc:
    person = Person(pers_dat)
    print "."
    pos_pa = choose_partner(person, "naught")
    if pos_pa:
        try:
            linked_people.append((person.character[0], len(pos_pa)))
        except:
            print person.character


print len(linked_people)
for name, num in linked_people:
    print "{} has {} related people in db".format(name, num)
