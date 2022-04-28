import speech_recognition as sr
r = sr.Recognizer()
name = "z.wav"

with sr.AudioFile(name) as source:
    print('Speak anything')
    audio = r.listen(source)

    try:
      text = r.recognize_google(audio)
      print('you said:{}'.format(text))
    except:
        print('Sorry could not recognize speech')


