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

 
#volumeGET = pygame.mixer_music.get_volume()
#print(volumeGET)




playButton = Button(root, text="Play", command=play, padx=40, pady = 25)
playButton.grid(row=3, column=0)

stopButton = Button(root, text="Stop", command=stop, padx=40, pady=25)
stopButton.grid(row=3, column=1)

songFile = Button(root, text="Pick a song", command=songpicker, padx=20, pady=25)
songFile.grid(row=3, column=2)

volumeUP = Button(root, text="+", padx=20, pady=15)
volumeUP.grid(row=4, column=2)

volumeDOWN = Button(root, text="-", padx=20, pady=15)
volumeDOWN.grid(row=4, column=0)

root.mainloop()