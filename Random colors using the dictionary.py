from tkinter import *
import random
root=Tk()
root.title("Dictionary")
root.geometry("500x400") 
dic={}
dic["Color"]=["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]
def Change():
    ran=random.randint(0, len(dic["Color"])-1)
    print(dic["Color"][ran])
    root.configure(background=dic["Color"][ran])
btn1=Button(root,text="click me",command=Change)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()