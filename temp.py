import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(5)

positions_main = pt.locateOnScreen("Smiley.png", confidence=.5)
x = positions_main[0]
y = positions_main[1]


# Gets Message
def get_messages():
    global x, y
    position = pt.locateOnScreen("Smiley.png", confidence=.5)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 110, y - 90, duration=.05)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(20, -230)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Received:" + whatsapp_message)
    return whatsapp_message


# posts
def post_response(message):
    global x, y
    position = pt.locateOnScreen("Smiley.png", confidence=.5)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n", interval=.01)


# processes response
def process_response(message):
    if "?" in str(message).lower():
        return "Don't ask me any questions"
    else:
        random_no = random.randrange(3)
        if random_no == 0:
            return "that's cool"
        elif random_no == 1:
            return "Remember to subscribe"
        else:
            return "I want Something"


# Check For New messages
def check_for_new_messages():
    pt.moveTo(x + 110, y - 55, duration=0.05)
    while True:
        # Continuously Check for green dot and new
        try:
            position = pt.locateOnScreen("unread.png", confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-200, 0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("no new msgs")
        if pt.pixelMatchesColor(int(x+110), int(y-55), (255,255,255), tolerance=10):
            print("is white")
            processed_message = process_response(get_messages())
            post_response(processed_message)
        else:
            print("no new msgs")
        sleep(5)

check_for_new_messages()
