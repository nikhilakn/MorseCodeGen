import keyboard
import ffmpeg
from playsound import playsound
from pydub import AudioSegment
import subprocess

dah="sound/dah.mp3"
dot="sound/dot.mp3"
cd={".-":"A","-...":"B"}
cs="-. "	
out=AudioSegment.silent(duration=2)

while True:
	if keyboard.is_pressed("enter"):
		m=input()
		if all( c in cs for c in m):
			
			for c in m:
				if c=="-":
					out=out+AudioSegment.from_mp3(dah)
					#playsound(dah)
				if c==".":
					out=out+AudioSegment.from_mp3(dot)
					#playsound(dot)
				if c==" ":
					#out=out+AudioSegment.silent(duration=0.444082)
					out=out+AudioSegment.silent(duration=1000)
				
			#print(m)
			out.export("sound/out.mp3", format="mp3")
			out="sound/out.mp3"
			playsound(out)
		
		#playsound("sound/dot.mp3")
		break
	
