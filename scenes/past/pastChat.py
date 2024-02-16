from utils import messageLine, responseDecision, write, enterToContinue, cls, title, divider

ending = False

messages = []


def addAndWriteMessage(username, message):
  messages.append(messageLine(username, message))


def continuousMessages():
  cls()
  title()
  for i in range(len(messages) - 1):
    print(messages[i] + "\n")
  write(messages[-1])
  print("\n")


def fishJibIntro():
  addAndWriteMessage("FishJib123", "Hey, are you new to this platform?")
  addAndWriteMessage(username, "Yeah, I am")
  addAndWriteMessage(
      "FishJib123",
      "Wow, I cannot believe this really works. This is really revolutionary")
  addAndWriteMessage(username, "Eh, it's not that impressive")
  addAndWriteMessage("FishJib123",
                     "Anyway, I can't believe it's almost the year 2000!")
  addAndWriteMessage(username, "What? It's 2024")
  addAndWriteMessage("FishJib123", "Hahaha funny joke!")
  addAndWriteMessage(username, "No, I'm serious")
  addAndWriteMessage("FishJib123", "What?")
  responseOption, response = responseDecision(
      username, ["It's literally February of 2024 rn", "nvm"])
  messages.append(response)
  while True:
    if responseOption == 1:
      convinceFishJib()
      break
    if responseOption == 2:
      nevermindFishJib()
      break
    else:
      responseOption, response = responseDecision(
          username, ["It's literally February of 2024 rn", "nvm"])
      continue


def convinceFishJib():
  continuousMessages()
  addAndWriteMessage("FishJib123", "Stop messing with me.")
  addAndWriteMessage("FishJib123", "That's not funny.")
  responseOption, response = responseDecision(username,
                                              ["You're not funny", "Whatever"])

  while True:
    if responseOption == 1:
      messages.append(response)
      fishJibBadEnd()
      break
    if responseOption == 2:
      messages.append(response)
      addAndWriteMessage(username, "Who are you anyway?")
      learnAboutFishJib()
      break
    else:
      responseOption, response = responseDecision(
          username, ["You're not funny", "Whatever"])
      continue


def nevermindFishJib():
  continuousMessages()
  addAndWriteMessage("FishJib123", "???")
  addAndWriteMessage(username, "Nevermind*")
  addAndWriteMessage("FishJib123",
                     "Oh okay hahaha how do you forget so many letters?")
  responseOption, response = responseDecision(
      username, ["Sooooo you said it's almost 2000?", "Who are you anyway?"])
  while True:
    if responseOption == 1:
      messages.append(response)
      almost2000()
      break
    if responseOption == 2:
      messages.append(response)
      learnAboutFishJib()
      break
    else:
      responseOption, response = responseDecision(
          username,
          ["Sooooo you said it's almost 2000?", "Who are you anyway?"])
      continue


def learnAboutFishJib():
  continuousMessages()
  global getJimmyInfo
  getJimmyInfo = True
  addAndWriteMessage("FishJib123", "My name is Jimmy. What about you?")
  name = input("<" + username + ">" + " My name is \n\n> ")
  messages.append(f"<{username}> My name is {name}")
  print("")
  messages.append(
      f"<FishJib123> Cool, {name.capitalize()}. I live in Chicago, by the way."
  )
  almost2000()


def almost2000():
  continuousMessages()
  addAndWriteMessage(username, "Sooooo you said it's almost 2000?")
  addAndWriteMessage("FishJib123", "Yes? Why do you keep bringing this up?")
  addAndWriteMessage("FishJib123", "It's 1999. Everybody knows this!")
  if getJimmyInfo is True:
    while True:
      responseOption, response = responseDecision(
          username, ["Stop lyinggg", "Listen... about the future"])
      if responseOption == 1:
        messages.append(response)
        fishJibBadEnd()
        break
      if responseOption == 2:
        messages.append(response)
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
  messageLine("FishJib123", "Whatever")
  divider()
  write("FishJib123 unfriended you.\n")
  enterToContinue()
  cls()


def saveJimmy():
  continuousMessages()
  addAndWriteMessage(
      username, "I don't know you in real life, but you have to trust me")
  addAndWriteMessage(
      username,
      "In July of 2000, Chicago experiences a deadly heat wave and hundreds of people die"
  )
  addAndWriteMessage(
      username,
      "if you're not joking your current year, just be wary about that")
  addAndWriteMessage("FishJib123",
                     "Umm... I think we should stop talking about the years")
  addAndWriteMessage(username, "Okay, sure")
  addAndWriteMessage(username, "We can talk about something else")
  global ending
  ending = True
  divider()
  write(
      "After that, you and @FishJib123 talked about lots of different stuff.\n")
  enterToContinue()
  cls()


def pastChat(name):
  global username
  username = name
  cls()
  title()
  fishJibIntro()
  return ending
