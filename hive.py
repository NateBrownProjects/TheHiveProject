# H.I.V.E V.2.0 BETA : Home-Assistant Integrated Virtual Environment
# VIEW THE HIVE PROJECT AT HTTPS://NateBrownProjects.GitHub.io/TheHiveProject/
# Copyright: Nate Brown Projects 2021 / Nate Brown 2021 / TheHiveProjectNZ 2021
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import math
from datetime import timedelta
import wikipedia
import pyjokes
import json
from pyttsx3 import Engine
import requests
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import commands
#import var
import calc
#import weatherhive
import sys
import hivelog  
import wolframalpha
#import wfa

## Engine Settings ##
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0]  .id)
wolframalpha = wolframalpha

## Boot Settings
def talk(text, console=True, consoleText=""):
    if console:
        print('\nCommunication Log: ' + text + '\n')
    elif not console and consoleText:
        print('Communication Log: ' + consoleText + '\n')
    engine.say(text)
    engine.runAndWait()

def qt():
    print('WolframAlpha has loaded!')
    question = input('Question: ')
    app_id = ('PETG7K-RRQQ6VK8PK')
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    talk(answer)

def qtalk(listener):
    print('WolframAlpha has loaded!')
    question = input('Question: ')
    app_id = ('PETG7K-RRQQ6VK8PK')
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    talk(answer)
    
def take_command():
    opt = input('Would you like to type your command (y/n)?: ')
    if opt.lower() == "y":
        return input("Please type your command: ").lower()
    if opt.lower() == "n":
        with sr.Microphone() as source:
            print('Ok, Please speak into the Mic.')
            voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            command = command.lower()
        except:
            pass
        return command
    return

def exit_hive():
    talk('Shutting all Hive Systems Down. Thank you for using hive! Goodbye!', False, 'Thank you for using H.I.V.E!')
    exit()

# Command List & Settings
def run_hive():
    command = take_command()
    print(command)
    if 'hive' in command:
        command = command.replace('hive', '')
        print('Command: ' + command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song, False)
        pywhatkit.playonyt(song)
    elif 'qtalk' in command:
        qtalk(listener)
    elif 'news' in command:
        talk("This feature isn't available yet. Please check back soon.")
    elif 'question' in command:
        print('WolframAlpha is now loading!')
        qt()
    elif 'help' in command:
        print('WolframAlpha is now loading!')
        qt()
    elif 'save' in command: 
        hivelog.save()
    elif 'joke' in command:
        res = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
        if res.status_code == requests.codes.ok:
            talk(str(res.json()['joke']))
        else:
            talk('Oops!I ran out of jokes')
    elif 'hey' in command:
        talk('Hey there!')
    elif 'date' in command:
        now = datetime.datetime.now()
        talk("Current date and time : ")
        talk(now.strftime("%d , %m , %Y"), False, now.strftime("%d-%m-%Y"))
        engine.setProperty("rate", 178)
    elif 'calculator' in command:
        calc.calculator()
    elif 'who is' in command:
        person = command.replace('who is', '')
        try:
            info = wikipedia.summary(person, 1, auto_suggest=False)
        except:
            info = "Sorry. I couldn't find any results about that!"
        talk(info)
    elif 'question' in command:
        qt()
    elif 'what is pi' in command:
        #print(math.pi)
        talk("Pi is equal to " + math.pi)
    #elif 'version' in command:
    #    print(var.version)
    elif 'quote' in command:
        talk('This Feature is coming soon!')   
    elif 'hi' in command or 'hello' in command:
        talk('Hello, i dont know you. Whats your name?', False)
        name = input('Whats your name?: ')
        talk('Hi, ' + name + '. How are you?')
        har = input('How are you?: ')
        talk('You are ' + har + '. Thats Great ' + name + '. Have,a great Day!',)
    
    
    ## WEATHER CONFIG COMMANDS
    elif 'current weather' in command:
        weatherhive.newweather()
    elif 'current wind' in command:
        weatherhive.windw()
    elif 'current temp' in command:
        weatherhive.tempw()
    elif 'cloud' in command:
        weatherhive.cloudw()
    ## END OF WEATHER CONFIG COMMANDS
    

    elif 'shut down' in command:
        exit_hive()
    elif 'exit' in command:
        exit_hive()
    elif 'awesome thanks' in command:
        talk('Your Welcome!')
    elif 'thanks' in command:
        talk('My Pleasure!')
    elif 'thank you' in command:
        talk('No Problem!')
    elif 'awesome' in command:
        talk('No Problem. Is there anything i can help you with?')
    elif 'no' in command:
         talk('ok!')
    elif 'yes' in command:
        talk('Ok, what is it?')
    elif 'how are you' in command:
        talk('I am Great!. How are you?', False)
        input('How are you?: ')
        talk('Thats Good!')
    elif 'wake up' in command:
        talk('Yes sir, how can I be of help today?')
    elif 'you still there' in command:
        talk('Yes Sir, I am ready for your command!')
    elif 'who are you' in command:
        talk('My name is Hive. It stands for Home Assistant Intergrated Virtual Environment. I am here to help you with whatever I can.')
    else:
        talk('Invalid Command!', False, 'Please say the command again.')
        input('Please Type Your Command: ')
        take_command()

talk('Systems Loaded, Welcome to HIVE!.\n\nHow can I help you Sir?\n')

while True:
    try:
        run_hive()
    except UnboundLocalError:
        talk('An Error has occurred, Please reload the System. If th'
             'is error continues please open an issue on Github.com/NateBrownProjects/TheHiveProject/Issues. Please refrence ERROR CODE 942. Thank you.')
        print('An Error has occurred, Please reload the System. If '
              'this error continues please open an issue on Github.com/NateBrownProjects/TheHiveProject/Issues.Please refrence ERROR CODE 942. Thank you.')
    continue
