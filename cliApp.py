from service import BotDict
faqBot = BotDict("support", {"Hi":"Hello there", 
    "Bye":"Good bye !", 
    "What is your name ?":"My name is support.",
    "Do you know a joke ?":"Why don't scientists trust atoms ? Because they make up everything !" 
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
from service import BotGPT
gptBot = BotGPT("support", "api_key")
print(gptBot.replyTo("Hello, are you GPT bot ?"))

#pip install openai
#via openai Python library
from service import BotGPT2
gptBot2 = BotGPT2("support", "api_key")
print(gptBot2.replyTo("Hello, are you GPT bot ?"))
'''
