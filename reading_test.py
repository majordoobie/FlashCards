#!/usr/bin/python3

contents=[]
with open('tester.txt', 'r') as infile:
    for line in infile:
        contents.append(line.rstrip())




"""


#Make our two variables that will be used for dictionaries
#deck[question] = answer
#contents is used to create a list from our file, ever line is it's own item
question = ''
answer = ''
contents = []
deck = {}
with open('tester.txt', 'r') as infile:
    for line in infile:
        contents.append(line.rstrip())


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
for k, v in dictDeck.items():
    print(k, v)






while 1:
    try:
        filename = input("File name:")
        with open(filename, 'r') as shit:
            contents = shit.read()
    except FileNotFoundError:
        msg = "Sorry, the file" + filename + " does not exist."
        print(msg)




while 1:
    try:
        filename = input("File name:")
        with open(filename, 'r') as shit:
            contents = shit.read()
    except:
        print('error')







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









def clearScreen():
    subprocess.Popen( 'cls' if platform.system() == "Windows" else "clear" )

subprocess.call("cls" if platform.system()=="Windows" else "clear", stdout=None)


============================================================================
Fail attempts

while contents:
    for i in range(0, contents.index('')):
        question += ' ' + contents[i]
        contents.pop(i)
    

"""





"""
question = ''
answer = ''
with open('tester.txt', 'r') as infile:
    lines = infile.readlines()


for line in lines:
    if 'Q:' in line:
        for line in lines:
            if not line.strip():
                continue
            else:
                question += line.lstrip()
        break
    else:
        for line in lines:
            if not line.strip():
                break
            else:
                answer += line.lstrip()
        break

print(question)
print('')
print(answer )
"""

"""
    elif line.startswith('A'):
        if not line.strip():
            break
        else:
            answer += line.lstrip()
print(question, answer)
"""



"""
with open('tester.txt', 'r') as infile:
    lines = infile.readlines()
question = ''
for line in lines:
    if not line.strip():
        break
    else:
        question += line.lstrip()
print(question)
"""

"""
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
"""