# cli - command-line interface - chat bot app
#Интерфейс командной строки (CLI) — способ взаимодействия между человеком и компьютером путём отправки компьютеру команд, представляющих собой последовательность символов.
#Команды интерпретируются с помощью специального интерпретатора, называемого оболочкой. Интерфейс командной строки противопоставляется системам управления программой на основе меню, а также различным реализациям графического интерфейса.
# module with client-side ligic
# functional programming
from service import Bot
faqBot = Bot("support", "data/support.csv")
#faqBot = Bot("support", {
#"Hi": "Hello!",
#"Bye": "Good bye!",
#"What is your name ?": "my name is support"
#})
# testing
message = "Hi"
reply = faqBot.replyTo(message)
print(message, " -> ", reply)
message = "Bye"
reply = faqBot.replyTo(message)
print(message, " -> ", reply)
message = "What is your name ?"
reply = faqBot.replyTo(message)
print(message, " -> ", reply)
