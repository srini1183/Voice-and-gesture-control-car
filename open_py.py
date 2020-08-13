import speech_recognition as sr


def record():
    r = sr.Recognizer()

    
    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        
        audio = r.listen(source)

        try:
            text = (r.recognize_google(audio))
            print(text)
            return text
        except sr.UnknownValueError:
            return "no"
        except sr.RequestError as e:
            return "no"
