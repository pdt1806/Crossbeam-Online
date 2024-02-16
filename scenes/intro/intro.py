from utils import write, options, divider, sys, usernameGet, cls, enterToContinue, storyTitle
from utils import *

def intro():
  storyTitle()
  write("The year is 2024. After signing up for to beta test for new messaging platform"
        ", you receive an email.\n\n")
  start = options(["Open it", "Ignore it"])
  while True:
    if start == 1:
      break
    if start == 2:
        write("Nothing happens.")
        sys.exit()
    else:
      start = options(["Open it", "Ignore it"])
      continue
  write("From: CrossTeam\n\n    Thank you for signing up! Please download the "
        "following attachment.\n\n(This email has 1 attachment)\n\n")
  download = options(["Download"])
  while True:
    if download == 1:
      break
    else:
      download = options(["Download"])
      continue
  write("Downloading...")
  write("\n\n...")
  write("\n\n...")
  write("\n\n...")
  write("\n\nDownload complete! Opening program...\n")
  enterToContinue()
  cls()
  divider()
  write("Welcome to the beta version of Crossbeam Online!\n\nPlease choose a temporary"
        " username. This will be seen by others.")
  username = usernameGet()
  return username