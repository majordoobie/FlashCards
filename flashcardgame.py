#!/usr/bin/python3

import sys
from os import get_terminal_size
from os import system as ossys
from platform import system
from flashcardpackages.terminalcolors import TerminalColors as tc
from flashcardpackages import arguments



def console():
	ts = get_terminal_size()
	return ts.columns 

def askQuestion(q, ts):
	ts = console()
	qvar = "Question:"
	print(tc.GREEN + tc.BOLD + tc.UNDERLINE + "{}".format(qvar.center(ts)) + tc.ENDC)
	print(tc.GREEN + "{}".format(q.center(ts)) + tc.ENDC)
	print('\n')
	variable = input(tc.RED + tc.ITALIC + 'Press Enter to reveal your answer.\nPress'\
					' q + Enter to exit:\n' + tc.ENDC)
	if variable in ('q', 'Q'):
		sys.exit()
	else:
		pass 
	return

def tellAnswer(a, ts):
	ts = console()
	avar = "Answer:"
	print(tc.BLUE + tc.BOLD + tc.UNDERLINE + "{}".format(avar.center(ts)) + tc.ENDC)
	if '<n>' in a:
		tempList = [ i for i in a.split() ]
	#if ['<n>' in i for i in a] == [True]:
		#tempList = [ x for i in a for x in i.split() ]
		for i in tempList:
			if i == '<n>':
				continue
			else:
				print(tc.BLUE +"\t\t\t\t- {}".format(i) + tc.ENDC)
				
	else:
		print(tc.BLUE + "{}".format(a.center(ts)) + tc.ENDC)
	print('\n')
	variable = input(tc.RED + tc.ITALIC + 'Press Enter to get next question.\nPress'\
					' q + Enter to exit:\n' + tc.ENDC)
	if variable in ('q', 'Q'):
		sys.exit()
	else:
		pass 
	ossys("cls" if system()=="Windows" else "clear")
	return
	
#PROGRAM HANGSOUT HERE ITERATING THROUGH YOUR STUDY MATERIAL
def game(dictDeck):
	while 1:
		ts = get_terminal_size()
		ossys("cls" if system()=="Windows" else "clear")
		for q, a in dictDeck.items():
			askQuestion(q, ts)
			tellAnswer(a, ts)
		


def fileParser(inputfile):		
	try:
#The new parser, took me for ever to make
		contents=[]
		with open(inputfile, 'r') as infile:
		    for line in infile:
		    	if not line.rstrip().startswith('#'):  #added the ignore comment feature
		        	contents.append(line.rstrip())

#This will fix the issue with some files not working because of white
#space at the end and or front after comments
		while contents[0] =='':
			del contents[0]
		while contents[-1] == '':
			del contents[-1]
#this will enumerate our contents list to find the spaces or new lines
#which is how we are seperating our questions and answers
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
		msg = "Sorry, the file " + '"' +inputfile+'"'+ " cannot be found."
		print(msg)
		sys.exit()

#TELLS USER WHAT TO DO
def usage():
	msg ="""
Usage: 
	./flashcardgame.py [-options] 

options:
	-h 		help
	-i 		location of input file

examples:
	./MyFlashCards.py -i studylist.txt
	or
	python MyFlashCards.py -i studylist.txt
	"""
	print(msg)
	sys.exit()

def help():
	msg = """
Description:
  This is a flash card program used to help you study by displaying a question then 
  revealing the answer when you're ready to reveal it. Think of it as a deck of 
  flash cards, with questions on one side and answers on the other side.

  To start studying simply call the program with the -i option and give it the 
  full path of your file that you're using to study from.

  Keep in mind that the parser uses blank lines as it's delimiter between questions
  and answers. If you have too many lines in between or not enough it will mess up
  the order of your deck.

Study file example:
---------------------------------------------------------------
  #Example of how your text file should look like..
  #hashtags / comments are ignored, you can add your
  #name or title if you wish.
  
  What is your name?
  
  Sarah.
  
  Where have you lived?
  
  I've lived in Europe, Africa, and South America.
  
  Can you print that as a list?
  
  Europe				
  <n>
  Africa
  <n>
  South America
---------------------------------------------------------------

Troubleshoot:
  Notice the blank lines between each question and answer. If you want to keep a group
  of text together then keep them in the same block don't add a new line in between
  them.
  
  If you want to print a proper list like so:
  Europe
  Africa
  South America
  
  You  must use a <n> between each item in a list format like so:
  Europe
  <n>
  Africa
  <n>
  South America

	 """
	print(msg)
	sys.exit()

def argumentParser(result):
	if len(result.keys()) <2:
		if '-i' in result.keys():
			fileParser(result['-i'])
		else:
			usage()
	else:
		usage()
		

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
	else:
		result = arguments.argvParser(sys.argv[1:])

	if result == 'help':
		help()
	elif type(result) == dict:
		argumentParser(result)
	else:
		usage()
	
