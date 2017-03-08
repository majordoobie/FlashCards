import sys
import getopt
import os

def askQuestion(q):
	print(q)
	variable = input('Press enter to reveal answer, q to exit:\n')
	if variable in ('q', 'Q'):
		sys.exit()
	else:
		pass 
	return

def tellAnswer(a):
	print(a)
	variable = input('Press enter to get next question, q to exit:\n')
	if variable in ('q', 'Q'):
		sys.exit()
	else:
		pass 
	os.system('cls')
	return
	
#PROGRAM HANGSOUT HERE ITERATING THROUGH YOUR STUDY MATERIAL
def game(stack):
	while 1:
		os.system('cls') 
		for q, a in stack.items():
			askQuestion(q)
			tellAnswer(a)
			

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
			opts, args = getopt.getopt(sys.argv[1:],'hi:', ["help"])  #fucking colon is important, fuck.
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
	
