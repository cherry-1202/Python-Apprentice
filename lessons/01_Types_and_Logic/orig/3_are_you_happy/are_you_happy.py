from tkinter import Tk, simpledialog, messagebox



# TODO: Look at the AreYouHappy.png image
#       Use pop-ups to recreate the chart using if and elif statements

pass

name=simpledialog.askstring(None, "Are you happy?")

if name == "Yes":
    
   messagebox.showinfo(message="Keep doing whatever you're doing.")

elif name == "No":
    #TODO
    name=simpledialog.askstring(None, "Do you want to be happy?")

    if name == "Yes":
      messagebox.showinfo(message="Change somethimg.")

    elif name == "No":
      messagebox.showinfo(message="Keep doing whatever you're doing.")






