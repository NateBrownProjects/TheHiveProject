import hive
import datetime
from pyttsx3 import Engine
def htime():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)
    print('Current time is ' + time)