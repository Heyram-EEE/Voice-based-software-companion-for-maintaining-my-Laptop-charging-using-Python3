import pyttsx3
import psutil
import time

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

stat=None
print("LapLiMate - A Laptop Battery Companian")
while(True):
    battery = psutil.sensors_battery()
    cstat= battery.power_plugged
    percent=battery.percent
    if((stat==False)and(cstat==True)):
        say("Thanks for Connecting the Charger")
    if(stat!=cstat):
        stat=cstat
    if((percent>85)and(cstat==True)):
        say("Please disconnect the charger Battery is "+str(percent))
        time.sleep(30)
    elif((percent<20)and(cstat==False)):
        say("Connect the charger Battery percentage is "+str(percent))
        time.sleep(30)
    time.sleep(1)
