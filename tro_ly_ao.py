import speech_recognition
import pyttsx3
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

with speech_recognition.Microphone() as mic:
	print("Robot: I'm Listening")
	audio = robot_ear.listen(mic)
try:
	you = robot_ear.recognize_google(audio)
except:
	you == ""
print(you)

if you == "":
	rebot_brain = "I can't hear you, try again"
elif you == "Hello":
	rebot_brain = "Hello G"
elif you == "today":
	today = date.today()
	robot_brain = today.strftime("%B %d, %Y")
elif you =="time":
	robot_brain = datetime.now()
else:
	robot_brain = " I'm fine thank you and you"

print("Robot: " + robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()