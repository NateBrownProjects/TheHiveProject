import datetime
import hive
import pyttsx3
from pyttsx3 import Engine
def hdate():
        now = datetime.datetime.now()
        talk("Current date and time : ")
        talk(now.strftime("%d/%m/%Y"))
        print("Current date and time : ")
        print(now.strftime("%d/%m/%Y"))
        engine.setProperty("rate", 178)