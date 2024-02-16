from scenes.future.accountTerminated import accountTerminated
from utils import messageLine, enterToContinue, responseDecision, cls, title, write

ending = True

messages = []


def continuousMessages():
  cls()
  title()
  if len(messages) > 2:
    for i in range(len(messages) - 1):
      print(messages[i] + "\n")
  else:
    print(messages[0] + "\n")
  write(messages[-1])
  print("\n")


def talkingAboutServer():
  continuousMessages()
  messages.append(messageLine("cutieneko", "we should get our friends on here"))
  messages.append(messageLine("cutieneko", "and make a server so we can all talk <33"))
  messages.append(messageLine(username, "Make a server? This is only the beta"))
  messages.append(messageLine(username, "It will not be here until the first release"))

def happyEnding():
  continuousMessages()
  messages.append(messageLine("cutieneko", "let's hope this is not a joke. keep yourse"
                              "lf safe bro"))
  messages.append(messageLine(username, "you too. gtg now. cya"))
  messages.append(messageLine("cutieneko", "cya"))
  enterToContinue()

def nahBroNoX():
  continuousMessages()
  global ending
  messages.append(messageLine("cutieneko", "aight whatever"))
  ending = False
  enterToContinue()

def warningTheXPandemic():
  continuousMessages()
  messages.append(messageLine("cutieneko", "ohh u bypassed the censorship, that's smar"
                              "t"))
  messages.append(messageLine("cutieneko", 
              "remember I mentioned the X pandemic that would change our history?"))
  messages.append(messageLine("cutieneko", "u should be prepared for that!"))
  messages.append(messageLine(username, "X? u mean covid? man that was a nightmare"))
  messages.append(messageLine("cutieneko", "no, another one after the covid"))
  responseOption, response = responseDecision(username, 
    ["be real bro there's no other pandemic. stop the cap", 
     "ok... i have some masks are stuff from covid so maybe i should be prepared"])
  messages.append(response)
  nahBroNoX() if responseOption == 1 else happyEnding()

def talkingAbout2112():
  continuousMessages()
  messages.append(messageLine("cutieneko", "man it's 2112 r u trapped behind?"))
  messages.append(messageLine(username, 
              "no it's freaking 2024 rn! is this a kind of joke on this platform?"))
  messages.append(messageLine("cutieneko", "bro... hear me out... "))
  messages.append(messageLine("cutieneko", "i think something is real wrong with this."))
  messages.append(messageLine("cutieneko", "what year are you in?"))
  responseOption, response = responseDecision(username, 
    ["2024. trust me, i'm not kidding", "it's been 24 years into the 3rd millennium"])
  messages.append(response)
  accountTerminated() if responseOption == 1 else warningTheXPandemic()

def nekoLeaves():
  continuousMessages()
  global ending
  messages.append(messageLine("cutieneko", "actually i gtg now. see ya later <3"))
  messages.append(messageLine(username, "ok see ya"))
  ending = False
  enterToContinue()

def howAboutYou():
  continuousMessages()
  messages.append(messageLine("cutieneko", 
              "how about you? probably u r also using one without letting me know =)))"))
  responseOption, response = responseDecision(username, 
    ["nah i don't have one", "honestly, i have no idea what you are talking about"])
  messages.append(response)
  nekoLeaves() if responseOption == 1 else talkingAbout2112()

def talkingAboutBetaAnd60():
  continuousMessages()
  messages.append(messageLine("cutieneko", "beta? what r u talking about XD"))
  messages.append(messageLine("cutieneko", 
              "nvm u know im texting u via the new apple vision 60 pro max!"))
  messages.append(messageLine("cutieneko", "the X pandemic really led to many great in"
                              "novations"))
  responseOption, response = responseDecision(username, 
    ["fr fr", "apple vision 60 pro max... is that the name of a new macintosh?"])
  messages.append(response)
  howAboutYou() if responseOption == 1 else talkingAbout2112()

def chatBeginning():
  messages.append(messageLine("cutieneko", "hey sweetheart <3 i see u r new to this pl"
                              "atform"))
  responseOption, response = responseDecision(username, 
    ["Yeah i'm pretty new to this. Any tips for me to use this platform?", 
     "I mean yeah it is still beta"])
  messages.append(response)
  match responseOption:
    case 1:
      talkingAboutServer()
      talkingAboutBetaAnd60()
    case 2:
      talkingAboutBetaAnd60()
    case 3:
      talkingAbout2112()


def futureChat(name):
  global username
  username = name
  cls()
  title()
  chatBeginning()
  return ending
