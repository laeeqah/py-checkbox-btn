# Tkinter exercise

#Make a window with a checkbox and a button
#When the button is clicked show if the checkbox was selected or not

from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Tkinter Exercise")
frame = Frame(root)
frame.pack()




btn=Button(root, text="Button")
btn.pack(side=LEFT)
btn.place(x=50, y= 50)


checked= IntVar()
check_btn= Checkbutton(root,text="Checkbox", onvalue=1, offvalue=0, variable=checked)
check_btn.pack(side= LEFT)
check_btn.place(x= 10, y=10)


    
root.mainloop()

