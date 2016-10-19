import pyttsx
import winsound
engine = pyttsx.init()
engine.say('Hello santhosh.')
command=raw_input("Enter text to speak")
engine.say(command)
engine.runAndWait()
winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
print ("TTS Success")
