import pyttsx
import winsound
engine = pyttsx.init()
engine.say('good morning santhosh.')
command= raw_input("Enter text ")
engine.say(command)
engine.runAndWait()
winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
print ("TTS Success")
