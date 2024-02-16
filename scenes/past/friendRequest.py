from utils import write, options, title


def fromFishJib123():
    title()
    write("Notification: You received a new friend request from @FishJib123!")
    print("\n")
    acceptFishJib123 = options(["Accept", "Ignore"])
    while True:
        if acceptFishJib123 == 1 or acceptFishJib123 == 2:
            break
    return acceptFishJib123 == 1
