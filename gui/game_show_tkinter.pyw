from tkinter import *
import pygame.mixer



def play_correct_sound():
    number_correct.set(number_correct.get()+1)
    correct_s.play()

def play_wrong_sound():
    number_wrong.set(number_wrong.get() + 1)
    wrong_s.play()

app = Tk()
app.title('Game Show App')
app.geometry('400x200+600+200')

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound('Sounds/correct.wav')
wrong_s = sounds.Sound('Sounds/wrong.wav')

number_correct = IntVar()
number_correct.set(0)

number_wrong = IntVar()
number_wrong.set(0)

label_0 = Label(app, text="When you are ready, click the buttons", height=5)
label_0.pack()

label_1 = Label(app, textvariable = number_correct, height = 5)
label_1.pack(side=RIGHT)

label_2 = Label(app, textvariable = number_wrong, height = 5)
label_2.pack(side=LEFT)

btn_1 = Button(app,  text='Correct', width = 10, command= play_correct_sound )
btn_1.pack(side=RIGHT, pady = 10, padx = 10)


btn_2 = Button(app,  text='Wrong', width = 10, command= play_wrong_sound )
btn_2.pack(side=LEFT, pady = 10, padx = 10)

app.mainloop()

print(str(number_correct) + " were correctly answered.")
print(str(number_wrong) + " were answered incorrectly.")
