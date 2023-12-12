# module with client-side logic
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
