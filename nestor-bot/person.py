class Person:
    def __init__(self, d):
        for key, value in d.items():
            k2 = key.lower()
            k3 = k2.replace(" ", "_")
            # Input is a mix of strings, list, and lists of empty strings. Want lists of strings or empty lists.
            newvalue = []
            if type(value) == list:
                for v in value:
                    if v:
                        newvalue.append(v)
            elif type(value) == str and value:
                newvalue.append(value)
            else:
                print "Value " + value + " is neither list nor string"
            setattr(self, k3, newvalue)

    def missing_attributes(self):
        # find missing entries:
        missing_properties = set()
        for k, v in self.__dict__.items():
            if not v:
                missing_properties.add(k)

        return missing_properties
