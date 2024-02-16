from scenes.future.accountTerminated import accountTerminated
from utils import messageLine, enterToContinue, responseDecision, cls, title, write

ending = False

messages = []


def addAndWriteMessage(username, message):
    messages.append(messageLine(username, message))


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
    addAndWriteMessage(
        "cutieneko", "we should get our friends on here")
    addAndWriteMessage(
        "cutieneko", "and make a server so we can all talk <33")
    addAndWriteMessage(
        username, "Make a server? This is only the beta")
    messages.append(
        f"<{username}> It will not be here until the first release")


def happyEnding():
    continuousMessages()
    addAndWriteMessage(
        "cutieneko", "let's hope this is not a joke. keep yourself safe bro")
    addAndWriteMessage(username, "you too. gtg now. cya")
    addAndWriteMessage("cutieneko", "cya")
    global ending
    ending = True
    enterToContinue()


def nahBroNoX():
    continuousMessages()
    addAndWriteMessage("cutieneko", "aight whatever")
    enterToContinue()


def warningTheXPandemic():
    continuousMessages()
    addAndWriteMessage(
        "cutieneko", "ohh u bypassed the censorship, that's smart")
    addAndWriteMessage("cutieneko",
                       "remember I mentioned the X pandemic that would change our history?")
    addAndWriteMessage("cutieneko", "u should be prepared for that!")
    addAndWriteMessage(
        username, "X? u mean covid? man that was a nightmare")
    addAndWriteMessage(
        "cutieneko", "no, another one after the covid")
    responseOption = 0
    while responseOption not in [1, 2]:
        responseOption, response = responseDecision(username,
                                                    ["be real bro there's no other pandemic. stop the cap",
                                                     "ok... i have some masks are stuff from covid so maybe i should be prepared"])
    messages.append(response)
    nahBroNoX() if responseOption == 1 else happyEnding()


def talkingAbout2112():
    continuousMessages()
    addAndWriteMessage(
        "cutieneko", "man it's 2112! u dont know this? r u trapped behind?")
    addAndWriteMessage(username,
                       "no it's freaking 2024 rn! is this a kind of joke on this platform?")
    addAndWriteMessage("cutieneko", "bro... hear me out... ")
    addAndWriteMessage(
        "cutieneko", "i think something is real wrong with this.")
    addAndWriteMessage("cutieneko", "what year are you in?")
    responseOption = 0
    while responseOption not in [1, 2]:
        responseOption, response = responseDecision(username,
                                                    ["2024. trust me, i'm not kidding", "it's been 24 years into the 3rd millennium"])
    messages.append(response)
    accountTerminated() if responseOption == 1 else warningTheXPandemic()


def nekoLeaves():
    continuousMessages()
    addAndWriteMessage(
        "cutieneko", "actually i gtg now. see ya later <3")
    addAndWriteMessage(username, "ok see ya")
    enterToContinue()


def howAboutYou():
    continuousMessages()
    addAndWriteMessage("cutieneko",
                       "how about you? probably u r also using one without letting me know =)))")
    responseOption = 0
    while responseOption not in [1, 2]:
        responseOption, response = responseDecision(username,
                                                    ["nah i don't have one", "honestly, i have no idea what you are talking about"])
    messages.append(response)
    nekoLeaves() if responseOption == 1 else talkingAbout2112()


def talkingAboutBetaAnd60():
    continuousMessages()
    addAndWriteMessage(
        "cutieneko", "beta? what r u talking about XD")
    addAndWriteMessage("cutieneko",
                       "nvm u know im texting u via the new apple vision 60 pro max!")
    addAndWriteMessage(
        "cutieneko", "the X pandemic really led to many great innovations")
    responseOption = 0
    while responseOption not in [1, 2]:
        responseOption, response = responseDecision(username,
                                                    ["fr fr", "apple vision 60 pro max... is that the name of a new macintosh?"])
    messages.append(response)
    howAboutYou() if responseOption == 1 else talkingAbout2112()


def chatBeginning():
    cls()
    title()
    addAndWriteMessage(
        "cutieneko", "hey sweetheart <3 i see u r new to this platform")
    responseOption = 0
    while responseOption not in [1, 2]:
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


def futureChat(name):
    global username
    username = name
    chatBeginning()
    return ending
