'''
from service import BotDict
faqBot = BotDict("support", {
 "Hi": "Hello there", 
 "Bye": "Good bye !", 
 "What is your name ?": "My name is support.",
 "Do you know a joke ?": "Why don't scientists trust atoms ? Because they make up everything !" 
})
print(faqBot.replyTo("Hi"))
print(faqBot.replyTo("Bye"))
print(faqBot.replyTo("What is your name ?"))
print(faqBot.replyTo("Do you know a joke ?"))

from service import BotFile
fileBot = BotFile("support", "data/support.csv")
print(fileBot.replyTo("Hi"))
print(fileBot.replyTo("Bye"))
print(fileBot.replyTo("What is your name ?"))
print(fileBot.replyTo("Do you know a joke ?"))
'''

#https://platform.openai.com/docs/api-reference
#https://platform.openai.com/api-keys - создание ключа
#https://platform.openai.com/usage
from service import BotGPT
gptBot = BotGPT("support", "api_key")
#print(gptBot.replyTo("Hello, are you GPT bot ?"))
#print(gptBot.replyTo("What is the air temperature Moldova / Chisinau today ?")) # не натринирован работать в реальном времени, cannot provide real-time information, gpt-3.5 с 2021 года.
print(gptBot.replyTo("Show me how to use recuests in python"))
#hm1: make this bot CLI interactive
while True:
 message = input("Ask ai a question or press enter to exit: ")
 if message != "":
  print(gptBot.replyTo(message))
 else:
  exit()

'''
#pip install openai
#via openai Python library
from service import BotGPT2
gptBot2 = BotGPT2("support", "api_key")
print(gptBot2.replyTo("Hello, are you GPT bot ?"))
'''
