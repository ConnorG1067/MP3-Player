from tkinter import *
import pygame
import os
from tkinter import filedialog

pygame.mixer.init()

root = Tk()
root.title("MP3 Player")
root.geometry("340x200")

def songpicker():
    global song
    song = filedialog.askopenfilename()
    

def play():
    pygame.mixer_music.load(song)
    pygame.mixer_music.play()


def stop():
    pygame.mixer_music.stop()


def volumeControl(val):
    volume = int(val)/100
    pygame.mixer_music.set_volume(volume)



playButton = Button(root, text="Play", command=play, padx=40, pady = 25)
playButton.grid(row=3, column=0)

stopButton = Button(root, text="Stop", command=stop, padx=40, pady=25)
stopButton.grid(row=3, column=1)

songFile = Button(root, text="Pick a song", command=songpicker, padx=20, pady=25)
songFile.grid(row=3, column=2)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command= volumeControl)
scale.grid(row=4, column= 1)


root.mainloop()