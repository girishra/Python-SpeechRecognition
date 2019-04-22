import speech_recognition as sr
r=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    print("speak")
    voice=r.listen(source)
    try:
        text = r.recognize_google(voice)
        print("you speak: " + text)
    except sr.UnknownValueError:
        print("Not audible")
    except sr.RequestError as e:
            print("Not found results from Google Speech Recognition service; {0}".format(e))
