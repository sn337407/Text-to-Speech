import pyttsx
import winsound
engine = pyttsx.init()
engine.say('Hello santhosh.')
file= open("sample.txt","rt")
test_in_file=file.read()
engine.say(test_in_file)
engine.runAndWait()
winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
print ("TTS Success")
