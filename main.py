from utils import cls, enterToContinue, storyTitle, write, divider
from scenes.future.friendRequest import fromCutieNeko
from scenes.future.futureChat import futureChat
from scenes.intro.intro import intro
from scenes.past.friendRequest import fromFishJib123
from scenes.past.pastChat import pastChat

hints = {
    0: {
        0: "Consider trying to get @FishJib123's trust and trusting @cutieneko for advice.",
        1: "Think about trying to get @FishJib123's trust to figure things out."
    },
    1: {
        0: "Imagine trusting @cutieneko to help you find a solution.",
        1: "Try not getting @FishJib123 to trust you and don't trust @cutieneko and see what happens."
    }
}

endingMessages = {
    0: {
        0: 'Ending 1/4: "Worst Ending"\n\nJimmy Cooper, previously known as @FishJib123 online, died from the Chicago heatwave in July of 2000. You died from the X disease later on.',
        1: 'Ending 2/4: "Fish No More"\n\nJimmy Cooper, previously known as @FishJib123 online, died from the Chicago heatwave in July of 2000. However, you survived the X disease thanks to @cutieneko\'s warning.'
    },
    1: {
        0: 'Ending 3/4: "Just Keep Swimming"\n\nOne day while browsing the internet, you stumble across a familiar username: @FishJib123. You are able to contact and chat with him. It turns out, Jimmy Cooper, also known as @FishJib123 online, remembered your warning and made sure he and his family was safe during the Chicago heatwave in July of 2000. However, before you could do anything, you are killed by the X disease by the time the next pandemic rolls around.',
        1: 'Ending 4/4: "True Ending"\n\nOne day while browsing the internet, you stumble across a familiar username: @FishJib123. You are able to contact and chat with him. It turns out, Jimmy Cooper, also known as @FishJib123 online, remembered your warning and made sure he and his family was safe during the Chicago heatwave in July of 2000. You survived the X disease thanks to @cutieneko\'s warning. You and Jimmy Cooper are able to meet in person and become good friends. You both are able to help each other out in the future.'
    }
}

cls()
username = intro()

cls()
talkToFish = fromFishJib123()
pastEnding = pastChat(username) if talkToFish else 0

cls()
fromCutieNeko()
futureEnding = futureChat(username)

cls()
storyTitle()
write(endingMessages[pastEnding][futureEnding] + "\n")
divider()
write("Hint: " + hints[pastEnding][futureEnding])
