class Bot:
# semantic versioning
 version = "1.0.0"
 def __init__(self, name, replies):
  self.name = name
# hm2: check if the "replies" is of type dict ?
# else if it is a string - suppose this is the name of the file with replies
# if it is file - open it
# parse the file -> dict
# -----
# Hi#Hello!
# Bye#Good bye!
# hm2*: check via isinstance()
  if isinstance(replies, dict):
  #if type(replies) == dict:
   self.replies = replies
  elif isinstance(replies, str):
  #elif type(replies) == str:
   repliesDict = dict()
   #self.replies = {}
  #file = open('data/support.csv', 'r')
   file = open(replies, 'r')
  # loop till the file ends
   while True:
    # считываем строку
    line = file.readline()
    # прерываем цикл, если строка пустая
    if line == "":
    #if not line:
     #print("работает")
     break
    fragments =  line.split("#")
    repliesDict[fragments[0]] = fragments[1]
    self.replies  = repliesDict
    #list = line.split("#")
    #self.replies[list[0]] = list[1]
   file.close()
 def replyTo(self, message):
# hm1: try to do this using match-case
  #variant2
  match message:
   case "Hi":
    return "Hello!"
   case "Bye":
    return "Good bye!"
   case "What is your name?":
    return "My name is support."
   case _:
    return "I can't understand you ..."
  #variant2
  #if message == "Hi":
   #return "Hello!"
  #elif message == "Bye":
   #return "Good bye!"
  #elif message == "What isyour name?":
   #return "My name is support."
  #variant3
  #if message in self.replies:
   #return self.replies[message]
  #else:
   #return "I can't understand you ..."