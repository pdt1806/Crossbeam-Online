from utils import messageLine, responseDecision, write, enterToContinue, cls, title, divider

ending = True

messages = []


def continuousMessages():
  cls()
  title()
  for i in range(len(messages) - 1):
    print(messages[i] + "\n")
  write(messages[-1])
  print("\n")


def fishJibIntro():
  messages.append(messageLine("FishJib123", "Hey, are you also a beta tester?"))
  messages.append(messageLine(username, "Yeah, I am"))
  messages.append(messageLine("FishJib123", "Wow, I can believe this really works. This"
                              " is really revolutionary"))
  messages.append(messageLine(username, "Eh, it's not that impressive"))
  messages.append(messageLine("FishJib123","Anyway, I can't believe it's almost the ye"
                              "ar 2000!"))
  messages.append(messageLine(username, "What? It's 2024"))   
  messages.append(messageLine("FishJib123", "Hahaha funny joke!"))
  messages.append(messageLine(username, "No, I'm serious"))
  messages.append(messageLine("FishJib123", "What?"))
  responseOption, response = responseDecision(username, ["It's literally February of 2"
                                                         "024 rn", "Nvm"])
  messages.append(response)
  while True:
    if responseOption == 1:
      convinceFishJib()
      break
    if responseOption == 2:
      nevermindFishJib()
      break
    else:
      responseOption, response = responseDecision(username, ["It's literally February "
                                                             "of 2024 rn",
                                                             "Nevermind"])
      continue


def convinceFishJib():
  continuousMessages()
  messages.append(messageLine("FishJib123", "Stop messing with me."))
  messages.append(messageLine("FishJib123", "That's not funny."))
  responseOption, response = responseDecision(username, ["You're not funny", "Whatever"])
  messages.append(response)
  while True:
    if responseOption == 1:
      fishJibBadEnd()
      break
    if responseOption == 2:
      messages.append(messageLine(username, "Who are you anyway?"))
      learnAboutFishJib()
      break
    else:
      responseOption, response = responseDecision(username, ["You're not funny", "What"
                                                             "ever"])
      continue


def nevermindFishJib():
  continuousMessages()
  messages.append(messageLine("FishJib123", "???"))
  messages.append(messageLine(username, "Nevermind*"))
  messages.append(messageLine("FishJib123",
              "Oh okay hahaha how do you forget so many letters?"))
  responseOption, response = responseDecision(username, ["Sooooo you said it's almost "
                                                         "2000?", "Who are "
                                                         "you anyway?"])
  messages.append(response)
  while True:
    if responseOption == 1:
      almost2000()
      break
    if responseOption == 2:
      learnAboutFishJib()
      break
    else:
      responseOption, response = responseDecision(username, ["Sooooo you said it's alm"
                                                             "ost 2000?", "Who "
                                                             "are you anyway?"])
      continue


def learnAboutFishJib():
  continuousMessages()
  global getJimmyInfo
  getJimmyInfo = True
  messages.append(messageLine("FishJib123", "My name is Jimmy. What about you?"))
  name = input("<" + username + ">" + " My name is \n>")
  messages.append(f"<{username}> My name is {name}")
  print("")
  messages.append(f"<FishJib123> Cool, {name.capitalize()}. I live in Chicago, by the"
                  + " way.")
  almost2000()


def almost2000():
  continuousMessages()
  messages.append(messageLine(username, "Sooooo you said it's almost 2000?"))
  messages.append(messageLine("FishJib123", "Yes? Why do you keep bringing this up?"))
  messages.append(messageLine("FishJib123", "It's 1999. Everybody knows this!"))
  if getJimmyInfo is True:
    while True:
      responseOption, response = responseDecision(
          username, ["Stop lyinggg", "Listen... about the future"])
      messages.append(response)
      if responseOption == 1:
        fishJibBadEnd()
        break
      if responseOption == 2:
        saveJimmy()
        break
      else:
        responseOption, response = responseDecision(
            username, ["Stop lyinggg", "Listen... about the future"])
        continue
  else:
    fishJibBadEnd()


def fishJibBadEnd():
  continuousMessages()
  global ending
  ending = False
  messageLine("FishJib", "Whatever")
  divider()
  write("FishJib123 unfriended you.\n")
  enterToContinue()
  cls()


def saveJimmy():
  continuousMessages()
  messageLine(username,
              "I don't know you in real life, but you have to trust me")
  messageLine(
      username, "In July of 2000, Chicago experiences a deadly heat wave and"
      " hundreds of people die")
  messageLine(username, "if you're not joking your current year, just be wary about th"
              "at")
  messageLine("FishJib",
              "Umm... I think we should stop talking about the years")
  messageLine(username, "Okay, sure")
  messageLine(username, "We can talk about something else")
  enterToContinue()
  cls()

getJimmyInfo = ()

def pastChat(name):
  global username
  username = name
  cls()
  title()
  fishJibIntro()
  return ending
