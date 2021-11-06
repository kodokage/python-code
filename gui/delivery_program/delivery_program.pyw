from tkinter import *
import tkinter.messagebox
import read_depots

def save_data():
    try:
        file = open('delivery.txt', 'a')
        file.write('Depot:\n')
        file.write(depot.get())
        file.write("%s\n" %depot.get())
        # file.write("%07d%s%16s\n" %(price * 100,credit_card, description))
        file.write('Address:\n')
        file.write("%s\n" %address.get())
        file.write('Decription\n')
        file.write("%s\n" %description.get("1.0",END))
        file.close()

        #depot.delete(0, END)
        address.delete(0, END)
        description.delete("1.0", END)
    except Exception as ex:
        tkinter.messagebox.shower("Error", "There was an error due to %s" %ex)



app = Tk()
app.title('Delivery Application')
#app.geometry('400x200+600+200')

depot_label =Label(app, text='Depot')
depot_label.pack()

depot = StringVar()
depot.set(None)

options = read_depots.read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()


# Radiobutton(app, variable= depot, text="Borikiri, Port Harcourt", value="Borikiri, Port Harcourt").pack()
# Radiobutton(app, variable=depot ,text="Borikiri, Bonny Island", value="Borikiri, Bonny Island").pack()
# Radiobutton(app, variable=depot,text="Bori Camp, Port Harcourt", value="Bori Camp, Port Harcourt").pack()



address_label = Label(app, text='Address')
address_label.pack()

address = Entry(app,)
address.pack()

desc_label = Label(app, text='Description')
desc_label.pack()

description = Text(app)
description.pack()

btn_save = Button(app, text='Save', width=15, command = save_data)
btn_save.pack()

app.mainloop()