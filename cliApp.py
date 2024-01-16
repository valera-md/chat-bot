from bot import *

#                        "csv"|"dict"|
#                         V
openaiBot = BotBuilder("openai", "John")\
    .withKey("api-key")\
    .withLang("en")\
    .withDomain("physics")\
    .withModel("dall-e-2")\
    .withUrl("/v1/images/generations")\
    .build()
    #.withModel("gpt-3.5-turbo")\
    #.withUrl("/v1/chat/completion")\
#without api-key comes response 401 invalid_api_key

    
print(openaiBot.replyTo("How many parameters do you use as a midel ?"))
print(openaiBot.replyTo("Draw a red dog"))

# HW2*: try to finish with 2 openai variants: gtp-3 + dall-e-2 
#             try to finish the builder for a csv bot 

csv = BotBuilder("csv", "file")\
    .withLang("en")\
    .withDomain("physics")\
    .withUrl("data/support.csv")\
    .build()
print(csv.replyTo("Hi"))
print(csv.replyTo("Bye"))
print(csv.replyTo("What is your name ?"))
print(csv.replyTo("Do you know a joke ?"))




#https://platform.openai.com/docs/api-reference
#https://platform.openai.com/api-keys - создание ключа
#https://platform.openai.com/usage
