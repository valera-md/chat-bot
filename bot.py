class _Bot:
# semantic versioning
 version = "1.0.0"
 def __init__(self, name):
  if len(name) >= 3:
   self.name = name
  else:
   print("ERROR: bot name must be at least 3 characters")
   exit()

 def replyTo(self, message):
  return f"{self.name}: Hello!"
 
#pip install requests
#https://platform.openai.com/docs/api-reference/authentication - документация по подключению к чат боту
import requests
import json
class _OPENAI(_Bot):
 def __init__(self, name):
  super().__init__(name)
 def replyTo(self, message):
  headers = {"Authorization": f"Bearer {self.gpt_key}" } 
  if self.model == "gpt-3.5-turbo":
   payload = {
    "model": self.model,
    "messages": [{"role": "user", "content": message}],
    "temperature": 0.7
} 
  elif self.model == "dall-e-2":
   payload = { 
    "model": self.model,
    "prompt": message
} 
  res = requests.post(
  f"https://api.openai.com{self.url}", 
  headers=headers, 
  json=payload
) 
  if res.status_code == 200:
   response = res.content.decode('utf-8')
   data = json.loads(response)
   if self.model == "gpt-3.5-turbo":
    return data["choices"][0]["message"]["content"]
   elif self.model == "dall-e-2":
    return data
  else:
   return "Error\n\n" + str(res) + str(res.content)
  #print(res.status_code)
  #print(res.content)

class _BotCSV(_Bot):
 def __init__(self, name):
  super().__init__(name)
 def replyTo(self, message):
  repliesDict = dict()
  file = open(self.url, 'r')
  while True:
   line = file.readline()
   line = line.replace("\n", "")
   if line == "":
    break
   fragments =  line.split("#")
   repliesDict[fragments[0]] = fragments[1]
   self.replies  = repliesDict
  file.close()
  if message in self.replies:
   return f"{self.name}: {self.replies[message]}"

class BotBuilder:
 def __init__(self, botType, botName):
# HW1: use match/case]
  match botType:
   case "openai":
    self.__bot = _OPENAI(botName)
   case "csv":
    self.__bot = _BotCSV(botName)
 def withKey(self,key):
  self.__bot.gpt_key = key
  return self
 def withLang(self,lang):
  self.__bot.lang = lang
  return self
 def withDomain(self,domain):
  self.__bot.domain = domain
  return self
 def withModel(self,model):
  self.__bot.model = model
  return self
 def withUrl(self,url):
  self.__bot.url = url
  return self
 def build(self):
  return self.__bot
