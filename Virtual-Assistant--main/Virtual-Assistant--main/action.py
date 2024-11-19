import datetime
import speak
import webbrowser
import weather
import os




def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey , How i can  help you !")  
        return "Hey , How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great . How about You ") 
            return "I am doing great . How about You "   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure")
           return "its my pleasure"      

    elif "good morning" in data_btn:
           speak.speak("Good morning , How can I help you")
           return "Good morning , How can I help you"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("Okay.See You Again")
            return "Okay.See You Again"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://www.youtube.com/")   
        speak.speak("Let's go to Youtube and enjoy music")                   
        return "Let's go to Youtube and enjoy music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    else :
        speak.speak( "i'm able to understand!")
        return "i'm able to understand!"       

