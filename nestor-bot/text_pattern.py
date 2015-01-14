import csv

class TextPattern(object):

def __init__(self):
	with open('prop_data.txt', 'rb') as csvfile:
    self.worddata = list(csv.reader(csvfile, delimiter=',', quotechar='"'))

def generate_problems(subject,object,domain):
#Get relationship between subject and object
