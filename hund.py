import vlc
import time
import readchar
import sys

def play(fileName):
	print("playing " + fileName)
	p = vlc.MediaPlayer(fileName + ".mp3")
	p.play()
	p.audio_set_volume(100)
	time.sleep(1)

print("ready, wainting for input")

while 1:
	c = readchar.readchar()
	if c == 'c':
		print("exit key detected")
		sys.exit()
	if c == 'r':
		play("test")
