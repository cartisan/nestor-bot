import csv
from random import randint

negative_openers = ["Life sucks.","I'm sad.","What a day.","FML!","Don't you just hate it when this happens!","Bummer."]
events_weapons = ["doesnt work anymore","failed","let me down today"]
events_vehicles = ["broke down", "has a flat battery", "got towed"]
events_partner = ["left me","dumped me","walked out on me"]
events_opponent = ["beat me","vanquished me","died"]
events_creator = ["died","passed away","abandoned me"]
events_group = ["kicked me out","got rid of me","abandoned me"]
positive_responses = ["Chillax!","Don't worry.","Take it easy.","Calm down :)","Its ok.","No worries."]
response_weapons = ["broke down","failed"]
response_vehicles = ["broke down", "has a flat battery", "got towed"]
response_partner = ["left me","dumped me","walked out on me"]
response_opponent = ["beat me","vanquished me"," died"]
response_creator = [" died"," passed away"," abandoned me"]
call_0 = ["Mismatch"]
call_1 = ["You can borrow my {1}"]
call_2 = ["Don't worry you'll live", "Don't worry you'll find another one"]
call_3 = ["You'd outgrown them", "You were too good for them."]
call_4 = ["There's always room with us", "There's always room in {1}","Join {1]!","{1} always has a place for you ;)"]
PROBLEM_TYPES = ["opponent",
                     "vehicle_of_choice",
                     "weapon_of_choice",
                     "creator",
                     "group_affiliation"]


class TextPattern(object):

    def __init__(self):
        #with open('prop_data.txt', 'rb') as csvfile:
       # self.worddata = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
        self.probs = list(PROBLEM_TYPES)
        self.call = dict()
        self.response = dict()
       # self.call[self.probs[0]] = events_partner
        self.call[self.probs[0]] = events_opponent
        self.call[self.probs[1]] = events_vehicles
        self.call[self.probs[2]] = events_weapons
        self.call[self.probs[3]] = events_creator
        self.call[self.probs[4]] = events_group
        self.response[0] = call_0
        self.response[1] = call_1
        self.response[2] = call_2
        self.response[3]= call_3
        self.response[4] = call_4
        self.mapping = [[0,1,1,2,4],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,0,3],[2,1,1,2,0]]
    def get_answer_string(self,subject,problem):
        return self.response[self.get_mapping(self.get_problem_number(subject),self.get_problem_number(problem))]
    
    def generate_problem_text(self,subject,problem):
    #Get relationship between subject and object
        #print problem
        poss = ""
        if(problem == "vehicle_of_choice"):
            poss = "My "
        elif(problem == "weapon_of_choice"):
            poss = "My "
        v = self.call[problem]
        
       
            
        #print v[0]
        open = negative_openers[randint(0,len(negative_openers) - 1)]
        return "{0}: " + open + " " + poss + "{1}" + " " + v[randint(0,len(v) -1)] + " "
    

    def generate_solution_text(self,relationship,problem):
    #Get relationship between subject and object
        #print problem
        #print relationship 
        v = self.get_answer_string(relationship,problem)
        pos = positive_responses[randint(0,len(positive_responses)) -1] 
        resp = v[randint(0,len(v) -1)]
        if(relationship == problem):
            resp = ""
        return "{0}:" + " " + pos + " " + resp
    
    def get_problem_number(self,string):
        number = 0
        count = 0
        for str in self.probs:
            if str == string:
                number = count
            count+=1
        return number
    
    def get_mapping(self,x,y):
        print self.mapping[x][y]
        return self.mapping[x][y]
   # def get_prefix(self,x):
    	