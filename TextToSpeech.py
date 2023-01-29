import pyttsx3
import wikipedia
from googletrans import Translator
from PyDictionary import PyDictionary
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
print("INSTRUCTIONS: ")
print("1. type 'find' to search for something in wikipedia")
print("2. type 'translate' to use the translate feature")
print("3. type 'dictionary' to use the dictionary feature")
print("4. type 'exit' to exit the program")
while True:
    query = input()
    if (query == 'find'):
        print("what do you want to search for??")
        speak("what do you want to search for??")
        x = input()
        if(x == 'exit'):
            exit(0)
        else:
            #search_results = wikipedia.search(x) 
            #result = ""
            try:
                search_result = wikipedia.summary()
                print(search_result)
                speak(search_result)
            except wikipedia.DisambiguationError as e:
                result = wikipedia.summary()
            except:
                pass
           # print(result)
            #speak(result)
    elif(query == 'translate'):
        print("Enter the word that you want to translate: ")
        trans = Translator()
        y = input()
        if(y == 'exit'):
            exit(0)
        else:
            z = trans.translate(y)
            print(z)
            speak(z)
    elif(query == 'dictionary'):
        dictionary = PyDictionary()
        w = input()
        if(w == 'exit'):
            exit(0)
        else:
            v = dictionary.meaning(w)
            print(v)
            speak(v)
    elif(query == 'exit'):
        exit(0)
    elif(query!='translate' or query != 'find' or query != 'dictionary'):
        #print(query)
        speak(query)