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
  if type(replies) == dict:
   self.replies = replies
  elif type(replies) == str:
   self.replies = {}
    #file = open('data/support.csv', 'r')
   file = open(replies, 'r')
   while True:
    # считываем строку
    line = file.readline()
    # прерываем цикл, если строка пустая
    if not line:
     break
    list = line.split("#")
    self.replies[list[0]] = list[1]
   file.close()
 def replyTo(self, message):
# hm1: try to do this using match-case
  #match message:
   #case "Hi":
    #return "Hello!"
   #case "Bye":
    #(return "Good bye!"
  #if message == "Hi":
   #return "Hello!"
  #elif message == "Bye":
   #return "Good bye!"
  if message in self.replies:
   return self.replies[message]
  else:
   return "I can't understand you ..."