# H.I.V.E V.0.1.5 BETA: Home-Assistant Intergrated Virtual Environment
# #VIEW THE HIVE PROJECT AT HTTPS://natebrownprojects.github.io/TheHiveProject/
# Copyright: Nate Brown Projects 2021 / Nate Brown 2021 / TheHiveProjectNZ 2021
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import math
from datetime import timedelta
import wikipedia
import pyjokes
import vosk
import rasa
from pyttsx3 import Engine

listener = sr.Recognizer()
engine: Engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0]  .id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
talk('Systems Loading, Welcome to the HIVE.')
talk('How, can i help, you Sir?')
print('Communication Log:')

def take_command():
    opt = input('Would you like to type your command (y/n)?: ')
    if opt.lower() == "y":
        return input("Please type your command: ").lower()
    if opt.lower() == "n":
        print('Ok, Please speak into the Mic.')
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hive' in command:
                command = command.replace('hive', '')
                print('Command: ' + command)

    except:
        pass

    return command

def run_hive():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        now = datetime.datetime.now()
        talk("Current date and time : ")
        talk(now.strftime("%d         %m                %Y"))
        engine.setProperty("rate", 178)
    elif 'calculator' in command:
            print('Loading up the H.I.V.E Calculator...')
            talk('Loading up the HIVE Calculator...')
            print('H.I.V.E Calculator Successfully loaded!')
            talk('HIVE Calculator Successfully loaded!')
            operation = input('''
        Please type in the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        ''')

            number_1 = int(input('Please enter the first number: '))
            number_2 = int(input('Please enter the second number: '))

            if operation == '+':
                print('{} + {} = '.format(number_1, number_2))
                print(number_1 + number_2)

            elif operation == '-':
                print('{} - {} = '.format(number_1, number_2))
                print(number_1 - number_2)

            elif operation == '*':
                print('{} * {} = '.format(number_1, number_2))
                print(number_1 * number_2)

            elif operation == '/':
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)


            else:
               run_hive()

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1, auto_suggest=False)

        print(info)
        talk(info)
    elif 'what is pi' in command:
        print(math.pi)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open project 65' in command:
        talk('Access Denied')
    elif 'hi' in command:
        talk('Hello, i dont know you. Whats your name')
        name = input('Whats your name?: ')
        talk('Hi, ' + name + 'How are you?')
        har = input('How are you?')
        talk('You are,,,. ' + har + 'Thats Great,,, ' + name + 'Have,a great Day!')


    elif 'admin override' in command:
        talk('Insufficient Permissions, Request Denied!')
    elif 'status report' in command:
        talk('All Systems Operational Sir!')
    elif 'hive' in command:
        talk('Yes, sir?')
    elif 'shut down' in command:
        talk('Shutting all Hive Systems Down.')
        talk('Thank you for using hive! Goodbye!')
        print('Thank you for using H.I.V.E!')
        exit()

    elif 'exit' in command:
        talk('Shutting all Hive Systems Down.')
        talk('Thank you for using hive! Goodbye!')
        print('Thank you for using H.I.V.E!')
        exit()
    elif 'awesome thanks' in command:
        talk('Your, Welcome!')
    elif 'thanks' in command:
        talk('Ny Pleasure!')
    elif 'thank you' in command:
        talk('No Problem!')
    elif 'awesome' in command:
        talk('No Problem, is there anything i, can help you, with?')
    elif ' no' in command:
         talk('ok!')
    elif 'yes' in command:
        talk('Ok, what is it?')
    elif 'how are you' in command:
        talk('I am Great! ,, How are you!?')
    elif 'you still there' in command:
        talk('Yes Sir, i am ready for your command!')
    elif 'who are you' in command:
        talk('My name is Hive. It stands for Home Assistant Intergrated Virtual Environment. I am here to help you with whatever i can')
    elif 'hello' in command:
        talk('hello, how are you today?')
        har = input('How are you?: ')
        talk('You are,,,. ' + har + 'Thats Great,,, ' + 'Have,a great Day!')
    elif 'version' in command:
        talk('I am currently running on Version 0.1.5 as of Monday March 22nd 7:05PM')
    else:
        print('Please say the command again.')
        input('Please Type Your Command: ')
        take_command()


while True:
    try:
        run_hive()
    except UnboundLocalError:
        talk('An Error has occurred, Please reload the System. If this error continues please open an issue on Github.com/NateBrownProjects/TheHiveProject/Issues.')
        print('An Error has occurred, Please reload the System. If this error continues please open an issue on Github.com/NateBrownProjects/TheHiveProject/Issues.')
        continue
