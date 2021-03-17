# H.I.V.E V.0.0.1 BETA: Home-Assistant Intergrated Virtual Environment
#VIEW THE HIVE PROJECT AT HTTPS://natebrownprojects.github.io/TheHiveProject/
#Copyright: Nate Brown Projects 2021 / Nate Brown 2021 / TheHiveProjectNZ 2021
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0]  .id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
print('How can i help you Sir?')

def take_command():
    try:

        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hive' in command:
                command = command.replace('hive', '')
                print(command)
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
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1, auto_suggest=False)

        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open project 65' in command:
        talk('Access Denied')
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
        talk('Im Great, How are you!?')
    elif 'you still there' in command:
        talk('Yes Sir, i am ready for your command!')
    elif 'who are you' in command:
        talk('My name is Hive. It stands for Home Assistant Intergrated Virtual Environment. I am here to help you with whatever i can')
    elif 'hello' in command:
        talk('hello, how are you today?')

    else:
        talk('Please say the command again.')


while True:
    try:
        run_hive()
    except UnboundLocalError:

        continue
