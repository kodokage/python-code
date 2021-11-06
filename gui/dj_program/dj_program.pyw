from tkinter import *
import pygame.mixer

app = Tk()
app.title("DJ Mixer")
app.geometry("400x100+200+100")

sound_file = "sounds/50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer
mixer.init()

def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()

def change_volume(v):
    track.set_volume(volume.get())

track_playing = IntVar()
track_btn = Checkbutton(app, variable=track_playing, command= track_toggle, text=sound_file)
track_btn.pack()

volume = DoubleVar()

volume_scale = Scale(app, variable = volume,
                from_=0.0, to=1.0,
                resolution=0.1, command=change_volume,
                label="Volume", orient=HORIZONTAL)
volume_scale.pack(side=RIGHT)

track = mixer.Sound(sound_file)

# start_btn = Button(app, text="Start", command=track_start)
# start_btn.pack( side=RIGHT, padx=10, pady=10)

# stop_btn = Button(app, text="Stop", command=track_stop)
# stop_btn.pack(side=LEFT, pady=10, padx=10)


app.mainloop()