from tkinter import *

app = Tk()

app.title("My Tkinter Application")
app.geometry("450x100+200+100")

def btn_click():
    print('I have just been clicked')

b1 = Button(app, text = "Correct!", width = 10, command = btn_click)
b1.pack(side= RIGHT, padx=10, pady=10)

b2 = Button(app, text = "Incorrect!", width = 10)
b2.pack(side= LEFT, padx=10, pady=10)

b3 = Button(app, text = "Quit !", width = 15 )
b3.pack(side = BOTTOM, pady=15, padx=15)


app.mainloop()



   
