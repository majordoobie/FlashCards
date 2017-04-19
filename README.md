MyFlashCards.py
===============


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
