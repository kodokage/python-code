from tkinter import *
from sound_panel import *
import pygame.mixer

app = Tk()
app.title('DJ Mix Program')

mixer = pygame.mixer
mixer.init()

sound_file1 = 'sounds/45414_M_RED_Trance_Train.wav'
sound_file2 = 'sounds/41312_M_RED_Sonar_Line.wav'

create_gui(app, mixer, sound_file1)
create_gui(app, mixer, sound_file2)

# panel = SoundPanel(app, mixer, sound_file1).pack()
# panel_2 = SoundPanel(app, mixer, sound_file2).pack()

app.mainloop()
