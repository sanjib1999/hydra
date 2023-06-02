import pyttsx3
import speech_recognition as s
import time
import jinja2
import pdfgen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',104)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    sr=s.Recognizer()
    with s.Microphone() as m:
        sr.adjust_for_ambient_noise(m)
        print("listening....")
        sr.pause_threshold=1
        audio=sr.listen(m)
    try:
        print("Recognizing...")   
        query = sr.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    return query

def ask_name():
    speak('name section..')
    while True:
        print('for voice input say a and for manual entry say b')
        speak('for voice input say a and for manual entry say b')
    
        opt=takecommand()
        if opt!="None":
            print(opt)
            
        
        if opt=='a':
            print('please tell me your name')
            speak('please tell me your name')
            audio=takecommand()
            print(audio)
            speak('is your name correct here')
            opt=takecommand()
            if opt=="yes":
                return audio
                break
            else:
                continue
        elif opt=='b':
            audio=input('please type your name here')
            print(audio)
            speak('is your name correct here')
            opt=takecommand()
            if opt=="yes":
                return audio
                break
            else:
                continue
        else:
            speak('please tell a valid option')
            continue
def ask_email():
    speak('email section...')
    while True:
        print('for voice input say a and for manual entry say b')
        speak('for voice input say a and for manual entry say b')
    
        opt=takecommand()
        if opt!="None":
            print(opt)
            
        
        if opt=='a':
            print('please tell me the first part of your email before @')
            speak('please tell me the first part of your email brfore @')
            audio=takecommand()
            print(audio)
            speak('is your email correct here')
            opt=takecommand()
            if opt=="yes":
                return audio+'@gmail.com'
                break
            else:
                continue
        elif opt=='b':
            audio=input('please type the first of your email')
            print(audio)
            speak('is your email correct here')
            opt=takecommand()
            if opt=="yes":
                return audio+'@gmail.com'
                break
            else:
                continue
        else:
            speak('please tell a valid option')
            continue

        
def ask_number():
    speak('contact details section')
    while True:
        print('for voice input say a and for manual entry say b')
        speak('for voice input say a and for manual entry say b')
    
        opt=takecommand()
        if opt!="None":
            print(opt)
            
        
        if opt=='a':
            print('please tell me your contact number')
            speak('please tell me your contact number')
            audio=takecommand()
            print(audio)
            speak('is your contact number correct here')
            opt=takecommand()
            if opt=="yes":
                return audio
                break
            else:
                continue
        elif opt=='b':
            audio=input('please type your contact number here:- ')
            print(audio)
            speak('is your contact number correct here')
            opt=takecommand()
            if opt=="yes":
                return audio
                break
            else:
                continue
        else:
            speak('please tell a valid option')
            continue


def ask_skills():
    speak('skills section')
    skills=[]
    while True:
        print('for voice input say a and for manual entry say b')
        speak('for voice input say a and for manual entry say b')
    
        opt=takecommand()
        if opt!="None":
            print(opt)
            
        
        if opt=='a':
           print('please tell me your skill')
           speak('please tell me your skill')
           audio=takecommand()
           print(audio)
           skills.append(audio)
           print('do you have any other skills')
           speak('do you have any other skills')
           opt=takecommand()
           
           if opt=='yes':
               continue
           else:
               return skills
               break

            
            

        elif opt=='b':
            audio=input('please tell me your skill ')
            print(audio)
            skills.append(audio)
            speak('do you have any other skills ')
            opt=takecommand()
            if opt=="yes":
                continue
            else:
                return skills
                break
        else:
            speak('please tell a valid option')
            continue

def ask_career_objective():
    speak('career objective section')
    while True:
        print('for voice input say a and for manual entry say b')
        speak('for voice input say a and for manual entry say b')
    
        opt=takecommand()
        if opt!="None":
            print(opt)
            
        
        if opt=='a':
            print('please tell me your career objective.')
            speak('please tell me your career objective.')
            audio=takecommand()
            print(audio)
            speak('is your sentence is correct.')
            opt=takecommand()
            if opt=="yes":
                return audio
                break
            else:
                continue
        elif opt=='b':
            audio=input('please type your career objective here...')
            print(audio)
            speak('is your sentence is correct.')
            opt=takecommand()
            if opt=="yes":
                return audio
                break
            else:
                continue
        else:
            speak('please tell a valid option')
            continue


if __name__=="__main__":
    speak("hii i am hydra and i am your personal resume builder")
    q=takecommand()
    yes=['yes','sure','okay','yeah','ok','alright','yep','ay','aye','all right','yo','yea','certainly','absolutely','exactly']
    if q:
        speak('can i ask you some question')
        que1=takecommand()
        if que1 in yes:
            #name=ask_name()
            #email=ask_email()
            #number=ask_number()
            #skills=ask_skills()
            #objective=ask_career_objective()
            
            name='sanjib kumar'
            email='kumarssanjib@gmail.com'
            number='9776804422'
            skills=['python','java','django','rest API']
            objective='i am a good guy.'
            print(name,email,number,skills,objective)

            jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
            template=jinja_env.get_template('layout.html')
            html_str=template.render(name=name,email=email,number=number,skills=skills,objective=objective)
            print(html_str)
            pdfgen.sync.from_string(html_str,'output.pdf')

        else:
            print('fail')
        

 