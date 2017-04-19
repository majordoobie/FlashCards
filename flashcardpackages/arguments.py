#!/usr/bin/python3




def argvParser(arguments):
	
	helpList = ['-h', '--help']
	#[i in sys.argv for i in help ] returns a list of true and falses while any is true
	#if either is true
	if any(i in arguments for i in helpList):
		return('help')

	#makes sure that there is one option switch per argument specified by user
	elif len(arguments) % 2 == 0:
		argvDict = dict(arguments[i:i+2] for i in range(0, len(arguments),2))
		return argvDict

	else:
		return 

