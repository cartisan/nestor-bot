import csv
from random import randint, choice

negative_openers = ["Life sucks.","I'm sad.","What a day.","FML!","Don't you just hate it when this happens!","Bummer.","Totally gutted."]
events_weapons = ["wont work anymore","failed me today","let me down today","just wont cut it anymore"]
intensifiers = ["finally ","ultimately ","resoundingly ",]
events_vehicles = ["broke down.", "has a flat battery.", "got towed."]
events_partner = ["left me.","dumped me.","walked out on me."]
events_opponent = ["beat me","vanquished me","died"]
events_creator = ["died","passed away","abandoned me"]
events_group = ["kicked me out","got rid of me","abandoned me","put me out to pasture", "retired me","went for beers and didnt invite me!","had a party and didnt invite me"]
positive_responses = ["Chillax!","Don't worry","Take it easy :)","Calm down :)","It's ok","No worries","Don't sweat it"]
response_weapons = ["broke down","failed"]
response_vehicles = ["broke down", "has a flat battery", "got towed"]
response_partner = ["left me","dumped me","walked out on me"]
response_opponent = ["beat me","vanquished me"," died"]
response_creator = [" died"," passed away"," abandoned me"]
call_0 = ["Mismatch"]
call_1 = ["You can borrow my {2}","I'll lend you my {2}", "You can take a loan of my {2}","You can always try my {2}"]
call_2 = ["Don't worry you'll live", "Don't worry you'll find another one"]
call_3 = ["You'd outgrown them", "You were too good for them.","You were a big fish in a small pond"]
call_4 = ["There's always room with us at {2}", "There's always room in {2}","Join {2}!","{2} always has a place for you ;)","I hear {2} is hiring ;)"]

PROBLEM_TYPES = [ "vehicle_of_choice",
                     "weapon_of_choice",
                     "opponent",
                     "group_affiliation"]


class TextPattern(object):

    def __init__(self):
        #with open('prop_data.txt', 'rb') as csvfile:
       # self.worddata = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
        self.probs = list(PROBLEM_TYPES)
        self.call = dict()
        self.response = dict()
       # self.call[self.probs[0]] = events_partner
        
        self.call[self.probs[0]] = events_vehicles
        self.call[self.probs[1]] = events_weapons
        self.call[self.probs[2]] = events_opponent
       # self.call[self.probs[3]] = events_creator
        self.call[self.probs[3]] = events_group
        self.response[0] = call_0
        self.response[1] = call_1
        self.response[2] = call_2
        self.response[3]= call_3
        self.response[4] = call_4
        self.mapping = [[0,0,0,0],[0,0,0,0],[1,1,3,4],[2,1,1,1]]
    def get_answer_string(self,subject,problem):
        return self.response[self.get_mapping(self.get_problem_number(subject),self.get_problem_number(problem))]
    
    def generate_problem_text(self,subject,problem):
    #Get relationship between subject and object
        #print problem
        poss = ""
        intense = ""
        if(problem == "vehicle_of_choice"):
            poss = "My "
        elif(problem == "weapon_of_choice"):
            poss = "My "
            intense = choice(intensifiers)
        elif(problem == "opponent"):
            intense = choice(intensifiers)   
        v = self.call[problem]
        
       
            
        #print v[0]
        open = negative_openers[randint(0,len(negative_openers) - 1)]
        return "{0}: " + open + " " + poss + "{1}" + " " + intense + v[randint(0,len(v) -1)] + " "
    

    def generate_solution_text(self,relationship,problem):
    #Get relationship between subject and object
        #print problem
        #print relationship 
        v = self.get_answer_string(relationship,problem)
        pos = positive_responses[randint(0,len(positive_responses)) -1] 
        resp = v[randint(0,len(v) -1)]
        if(relationship == problem):
            resp = ""
        return "{0}:" + " " + pos + "{1}. " + resp
    
    def get_problem_number(self,string):
        number = 0
        count = 0
        for str in self.probs:
            if str == string:
                number = count
            count+=1
        return number
    
    def get_mapping(self,x,y):
        #print self.mapping[x][y]
        return self.mapping[x][y]
   # def get_prefix(self,x):
    	
