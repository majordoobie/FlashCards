#!/usr/bin/python3

import sys
import getopt
import os
import subprocess
import platform
from TerminalColors import TerminalColors as tc




def console():
	ts = os.get_terminal_size()
	return ts.columns 

def askQuestion(q, ts):
	ts = console()
	print(tc.GREEN + "{}".format(q.center(ts)) + tc.ENDC)
	variable = input('Press enter to reveal your answer.\nPress q to exit:\n')
	if variable in ('q', 'Q'):
		sys.exit()
	else:
		pass 
	return

def tellAnswer(a, ts):
	ts = console()
	print(tc.BLUE + "{}".format(a.center(ts)) + tc.ENDC)
	variable = input('Press enter to get next question.\nPress q to exit:\n')
	if variable in ('q', 'Q'):
		sys.exit()
	else:
		pass 
	subprocess.call("cls" if platform.system()=="Windows" else "clear")
	return
	
#PROGRAM HANGSOUT HERE ITERATING THROUGH YOUR STUDY MATERIAL
def game(dictDeck):
	while 1:
		ts = os.get_terminal_size()
		subprocess.call("cls" if platform.system()=="Windows" else "clear")
		for q, a in dictDeck.items():
			askQuestion(q, ts)
			tellAnswer(a, ts)
		


def parse(inputfile):		
	try:
#The new parser, took me for ever to make
		contents=[]
		with open(inputfile, 'r') as infile:
		    for line in infile:
		        contents.append(line.rstrip())
#this will enumerate our contents list to find the spaces or new lines
#which is how we are seperating our questions and answers
		print('hi')
		spaces = [ i for i,x in enumerate(contents) if x == '' ]
#now remove those blank spaces
		for i in reversed(spaces):
		    del contents[i]
#update our space list now that we removed our blanks
		x = 0
		for i in spaces[1:]: #skip the first one since that will always be fine
		    spaces[spaces.index(i)] = i - 1 - x
		    x += 1
#now append a length so that we don't lost our last answer when appending
#to our list coming up
		spaces.append(len(contents))
#This will concatenate the question items and answer items into one item
		x = 0
		listDeck = []
		for i in spaces:
		    listDeck.append(' '.join(contents[x:i]))
		    x = i
#now we seperate the questions and 
		dictDeck = dict(listDeck[i:i+2] for i in range(0, len(listDeck), 2))
		game(dictDeck)    

	except FileNotFoundError:
		msg = "Sorry, the file " + '"' +inputfile+'"'+ " does not exist."
		print(msg)
		sys.exit()
"""
#PARSES THROUGH THE FILE TO CREATE A DICT OF Q AND A
def parse(inputfile):
	if os.path.isfile(inputfile) == True:
		file = open(inputfile, 'r') 
		stack = {}
		for line in file: 
			if line.startswith('Q'):
				question = line.rstrip() 
			elif line.startswith('A'):
				answer = line.rstrip() 
				stack[question] = answer	
		game(stack)
	else:
		print('foolish human, file does not exit.')
		sys.exit()
"""
#TELLS USER WHAT TO DO
def usage():
	print("Use -i to give the location of the input file to read from.")
	print("Example: python MyFlashCards.py -i studylist.txt")
	return
	
#ESTABLISH WHAT FILE TO READ
def main(): 
	inputfile = ''
	if len(sys.argv) < 2:
		usage()
		sys.exit()
	else:
		try:
			opts, args = getopt.getopt(sys.argv[1:],'h:i:')  #fucking colon is important, fuck.
		except getopt.GetoptError:
			usage()
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				usage()
				sys.exit(2)
			elif opt == '-i':
				#print("Args: %r " % sys.argv[1:]) <-- good way to test how many fuckers you got
				inputfile = arg
				parse(inputfile)
			else:
				usage()
				sys.exit()
				
if __name__ == "__main__":
	main()
	