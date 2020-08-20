import moviepy.editor as mp
import speech_recognition as sr

clip=mp.VideoFileClip(r"video.mp4")
clip.audio.write_audiofile(r"converted.wav")

r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")

with audio as source:
  r.adjust_for_ambient_noise(source)
  audio_file = r.record(source)

result = r.recognize_google(audio_file)
print(result)

with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")