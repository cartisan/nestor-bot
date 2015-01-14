import csv

negative_openers = ["Life sucks. ","I'm sad because ","What a day. ","FML"]
events_weapons = ["lost my","failed"]
events_vehicles = ["broke down", "has a flat battery", "got towed"]
events_partner = ["left me","dumped me","walked out on me"]
events_opponent = ["beat me","vanquished me","died"]
events_creator = ["died","passed away","abandoned me"]
events_group = ["kicked me out","got rid of me","abandoned me"]
positive_responses = ["Chillax","Don't worry","Take it easy"]
response_weapons = ["broke down","failed"]
response_vehicles = ["broke down", "has a flat battery", "got towed"]
response_partner = ["left me","dumped me","walked out on me"]
response_opponent = ["beat me","vanquished me","died"]
response_creator = ["died","passed away","abandoned me"]
call_0 = ["Mismatch"]
call_1 = ["You can borrow my {1}]"]
call_2 = ["Don't worry you'll live", "Don't worry you'll find another one"]
call_3 = ["You'd outgrown them", "You were too good for them."]
call_4 = ["There's always room with us", "There's always room in {1}","Join {1]!"]
PROBLEM_TYPES = set(["Marital Status",
                     "Opponent",
                     "Vehicle of Choice",
                     "Weapon of Choice",
                     "Creator",
                     "Group Affiliation"])

class TextPattern(object):

    def __init__(self):
        #with open('prop_data.txt', 'rb') as csvfile:
       # self.worddata = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
        self.probs = list(PROBLEM_TYPES)
        self.call = dict()
        self.response = dict()
        self.call[self.probs[0]] = events_partner
        self.call[self.probs[1]] = events_opponent  
        self.call[self.probs[2]] = events_vehicles 
        self.call[self.probs[3]] = events_weapons 
        self.call[self.probs[4]] = events_creator
        self.call[self.probs[5]] = events_group
        self.response[0] = call_0
        self.response[1] = call_1
        self.response[2] = call_2
        self.response[3]= call_3
        self.response[4] = call_4
        self.mapping = [[0,1,1,1,2,3],[1,0,1,1,2,4],[0,0,0,0,0,0],[0,0,0,0,0,0],[3,1,1,1,0,3],[3,2,1,1,2,0],]
    def get_answer_string(self,subject,problem):
        return self.response[self.get_mapping(self.get_problem_number(subject),self.get_problem_number(problem))]
    
    def generate_problem_text(self,subject,problem):
    #Get relationship between subject and object
        return "{0}:" + negative_openers[1] + "my " + "{1}" + self.call[problem][0]
    

    def generate_solution_text(self,relationship,problem):
    #Get relationship between subject and object
        v = self.get_answer_string(relationship,problem)
        return "{0}:" + v[0]

    
    def get_problem_number(self,string):
        number = 0
        count = 0
        for str in self.probs:
            if str == string:
                number = count
            count+=1
        return number
    
    def get_mapping(self,x,y):
        return self.mapping[x][y]