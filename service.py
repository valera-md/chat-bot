class Bot:
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
 
 # inheriting classes
class BotDict(Bot):
 def __init__(self, name, dict):
  #self.name = name # <-!
  #Bot.__init__(self,name)
  super().__init__(name)
  self.dict = dict
 def replyTo(self, message):
  if message in self.dict:
   return f"{self.name}: {self.dict[message]}"

class BotFile(Bot):
 #HM1* finish the (csv) file variant
 def __init__(self, name, replies):
  super().__init__(name)
  repliesDict = dict()
  file = open(replies, 'r')
  while True:
   line = file.readline()
   line = line.replace("\n", "")
   if line == "":
    break
   fragments =  line.split("#")
   repliesDict[fragments[0]] = fragments[1]
   self.replies  = repliesDict
  file.close()
 def replyTo(self, message):
  if message in self.replies:
   return f"{self.name}: {self.replies[message]}"
 
"""
#pip install requests
#https://platform.openai.com/docs/api-reference/authentication - документация по подключению к чат боту
import requests
class BotGPT(Bot):
 def __init__(self, name, gpt_key):
  super().__init__(name)
  self.gpt_key = gpt_key
 def replyTo(self, message):
  headers = {"Authorization": f"Bearer {self.gpt_key}" } 
  json = { 
   "model": "gpt-3.5-turbo", 
   "messages": [{"role": "user", "content": message}], 
   "temperature": 0.7
} 
  res = requests.post("https://api.openai.com/v1/chat/completions", 
  headers=headers, 
  json=json
) 
  print(res.status_code)
  print(res.content)

# VARIANTS:
# 1. use gpt openai library: install with pip, import ... (hw optional) 
# 2. use http requests -> api (in class) 

from openai import OpenAI
class BotGPT2(Bot):
 def __init__(self, name, gpt_key):
  super().__init__(name)
  self.gpt_key = gpt_key
 def replyTo(self, message):
  openai.api_key = {self.gpt_key}
  client = OpenAI()
  stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": message}],
    stream=True,
)
  for chunk in stream:
   if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
"""
