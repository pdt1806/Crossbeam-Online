import sys
import os
from time import sleep


def write(text):
    for char in text:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()


def options(list):
    try:
        print("─" * 50 + "\n")
        for i in range(len(list)):
            print(f"[{i+1}] {list[i]}")
        print("")
        option = int(input("> "))
        divider()
        return option
    except ValueError:
        return 0


def cls():
    os.system('clear')


def divider():
    print("\n" + "─" * 50 + "\n")


def responseDecision(username, responses):
    decision = options(responses)
    if decision > len(responses) or decision < 1:
        return "", 0
    response = f"<{username}> {responses[decision-1]}"
    print("\n")
    return decision, response


def enterToContinue():
    divider()
    input("Hit Enter to continue.")
    divider()


def title():
    divider()
    print(" " * 15 + "CROSSBEAM ONLINE")
    print(" " * 20 + "vX.X.X")
    divider()


def storyTitle():
    divider()
    print(" " * 15 + "CROSSBEAM ONLINE")
    divider()


def messageLine(sender, message):
    line = f"<{sender}> {message}"
    write(line)
    print("\n")
    return line


def usernameGet():
    global username
    username = input("\n\nUSERNAME: ")
    while True:
        if username == "FishJib123" or username == "cutieneko":
            write(
                "\nThis temporary username is currently being used. Please try another.")
            username = input("\n\nUSERNAME: ")
            continue
        if username == "":
            username = input("\n\nUSERNAME: ")
            continue
        else:
            break
    return username
