from utils import write, cls, options, title


def fromCutieNeko():

  ignoreCounter = 0
  acceptCutieNeko = 0
  while acceptCutieNeko != 1:
    title()
    write("Notification: You received a new friend request from @cutieneko!")
    if ignoreCounter > 2:
      print("")
      print("Hint: You cannot block this person. Just accept their request :)")
    print("\n")
    acceptCutieNeko = options(["Accept", "Ignore"])
    if acceptCutieNeko == 2:
      cls()
      ignoreCounter += 1
