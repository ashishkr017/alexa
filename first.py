import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import pywhatkit


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning!")
    elif hour>=12 and hour<18:
        speak("good Afternoon")
    else:
        speak("good Evening")
    speak("I am akira how may i help you")


def takeCommand():
    # for taking micropone input and return output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1 
        audio=r.listen(source)
    try:
        print("reconizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

 


if __name__ =="__main__":

    if "akira" in takeCommand().lower():

        wishMe()
        while True:
            query = takeCommand().lower()
   #logic for task based on query
            if 'wikipedia' in query:
                speak("searching wikipedia.....")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stack' in query:
                 webbrowser.open("stackoverflow.com")

            elif 'open insta' in query:
                webbrowser.open("instagram.com")

            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code'in query:
                codePath="C:\\Users\\ashiu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'play' in query:
                song=query.replace("play","")
                speak("playing"+song)
                pywhatkit.playonyt(song)
            elif 'who are you' in query:
                speak("i am a bot made for some task")








            elif 'quiet' in query:
                break
            
            elif 'stop' in query:
                speak("thnk you for using me have a nice day ")
                break

            


#     while True:
#         query = takeCommand().lower()
#    #logic for task based on query
#         if 'wikipedia' in query:
#             speak("searching wikipedia.....")
#             query=query.replace("wikipedia","")
#             results=wikipedia.summary(query,sentences=2)
#             speak("according to wikipedia")
#             print(results)
#             speak(results)
#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")

#         elif 'open google' in query:
#             webbrowser.open("google.com")

#         elif 'open stack' in query:
#             webbrowser.open("stackoverflow.com")
#         elif 'open insta' in query:
#             webbrowser.open("instagram.com")
#         elif 'the time' in query:
#             strTime=datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"Sir, the time is {strTime}")
#         elif 'open code'in query:
#             codePath="C:\\Users\\ashiu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#             os.startfile(codePath)
        # elif'email to ashiu' in query:
        #     try:
        #         speak("what should i say")
        #         content=takeCommand()
        #         to="ashiumartin@gmai.com"
        #         sendEmail(to,content)
        #         speak("email has been sent! ")
        #     except Exception as e:
        #         print(e)
        #         speak("sorry i can't able to send email ")





