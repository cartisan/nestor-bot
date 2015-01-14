import csv

negative_openers = ["Life sucks. ","I'm sad because ","What a day. ","FML"]
events_weapons = ["broke down","failed"]
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
call_1 = ["You can borrow {1}]"]
call_2 = ["Don't worry you'll live", "Don't worry you'll find another one"]
call_3 = ["You'd outgrown them", "You were too good for them."]
call_4 = ["There's always room with us", "There's always room in {1}","Join {1]!"]


PROBLEM_TYPES = ["marital_status",
                     "opponent",
                     "vehicle_of_choice",
                     "weapon_of_choice",
                     "creator",
                     "group_affiliation"]


class TextPattern(object):

	

	

	
					 
	

	def __init__(self):
		#with open('prop_data.txt', 'rb') as csvfile:
	   # self.worddata = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
		self.call = dict()
		self.response = dict()
		self.call[PROBLEM_TYPES[0]] = events_partner
		self.call[PROBLEM_TYPES[1]] = events_opponent  
		self.call[PROBLEM_TYPES[2]] = events_vehicles 
		self.call[PROBLEM_TYPES[3]] = events_weapons 
		self.call[PROBLEM_TYPES[4]] = events_creator
		self.call[PROBLEM_TYPES[5]] = events_group
		self.response[1] = call_1
		self.response[2] = call_2
		self.response[3]= call_3
		self.response[4] = call_4
		mapping = [[0,1,1,1,2,3],[1,0,1,1,2,4],[0,0,0,0,0,0],[0,0,0,0,0,0],[3,1,1,1,0,3],[3,2,1,1,2,0],]

	def generate_problem_text(self,subject,problem):
	#Get relationship between subject and object
		return "{0}:" + negative_openers[1] + "My " + "{1}" + self.call[problem][0]
	

	def generate_solution_text(self,relationship,problem):
	#Get relationship between subject and object
		return "{0}:" + get_answer_string(relationship,problem)[0]

	def get_answer_string(self,subject,problem):
		return response(get_mapping(get_problem_number(subject),get_problem_number(problem)))
	
	def get_problem_number(self,string):
		number = 0
		count = 0
		for str in PROBLEM_TYPES:
			if str == string:
				number = count
			count+=1
		return count
	
	def get_mapping(self,x,y):
		return mapping[x,y]
