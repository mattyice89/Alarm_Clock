'''
The goal of this project is to create an alarm that will play a randomly generated
Youtube video (from a list) at the time specified by the user.  I got this
project recommendation from reddit:
https://www.reddit.com/r/beginnerprojects/comments/4n9hne/project_idea_alarm_clock/
'''

import time
import webbrowser
import random

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def video_link():
    lines = open('youtubeurls.txt').readlines()
    url = lines[random.randint(0,file_len('youtubeurls.txt'))]
    video_link = webbrowser.open(url, new=1, autoraise = True)

print("Enter when the alarm should go off.")
print("Be sure to use this format: HH:MM (i.e. 06:30)")
Alarm = input("> ")

Time = time.strftime('%H:%M')

while Time != Alarm:
    print("The time is: " + Time)
    Time = time.strftime('%H:%M')
    time.sleep(1)

    if Time == Alarm:
        print("It's time to wake up!")
        video_link()
