import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipediaapi


engine=pyttsx3.init()
listener=sr.Recognizer()

voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def start():
    engine.say("I am Alexa")
    engine.say("What can I do for you?")
    engine.runAndWait()
    run_command()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration = 1)
            print('Listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            print(command)
            command=command.lower()
            if 'alexa' in command:
                command= command.replace('alexa', '')

    except:
        command="thuis sdijrbj"
        print('Couldn\'t understand command')
    return command

def run_command():
    command=listen()
    stop=0
    if 'play' in command:
        song=command.replace('play', '')
        talk('playing '+ song)
        stop=1
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' +time)
    elif 'who is' in command:
        thing=command.replace('who is', '')
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page=wiki_wiki.page(thing)
        content=page.summary[:]
        try:
            parts=content.split('.')
            short_content=parts[0]+ ". "+ parts[1]
        except:
            short_content=content
        print(short_content)
        talk(short_content)
    elif 'what is' in command:
        thing=command.replace('what is', '')
        #info= wikipedia.summary(thing, 1)
        #talk(info)
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page=wiki_wiki.page(thing)
        content=page.summary[:]
        try:
            parts=content.split('.')
            short_content=parts[0]+ ". "+ parts[1]
        except:
            short_content=content
        print(short_content)
        talk(short_content)
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'how are you' in command:
        response='I am fine. Hope you are having a great day too'
        print(response)
        talk(response)
    elif 'are you single' in command:
        response='No. I am married to google'
        print(response)
        talk(response)
    elif 'what are you' in command:
        response='I am just a python program created by Aakash. You can ask me to play a song or to tell a joke or information about something.'
        print(response)
        talk(response)
    elif 'stop' in command:
        stop=1
    else:
        talk('I can not understand that. Please speak again')
    if stop==0:
        run_command()

start()

