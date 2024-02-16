from utils import write, options, sys, usernameGet, cls, enterToContinue, storyTitle
from utils import *
from time import sleep


def intro():
    storyTitle()
    write("The year is 2024. After signing up for to beta test for new messaging platform, you receive an email.\n\n")
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
    cls()
    storyTitle()
    write("From: CrossTeam\n\n    Thank you for signing up! Please download the following attachment.\n\n(This email has 1 attachment)\n\n")
    download = options(["Download"])
    while True:
        if download == 1:
            break
        else:
            download = options(["Download"])
            continue
    cls()
    storyTitle()
    for i in range(101):
        sleep(0.02)
        sys.stdout.write("\rDownloading... %d%%" % i)
        sys.stdout.flush()
    write("\n\nDownload complete! Opening program...\n")
    enterToContinue()
    cls()
    title()
    write("Welcome to the beta version of Crossbeam Online!\n\nPlease enter a username. This will be seen by others.")
    username = usernameGet()
    write("\nReminder: Users are able to send friend requests with one another and chat."
          "\nHave fun!\n")
    enterToContinue()
    return username
