#Buttons simply clickable labels so you can modify buttons like labels.
import tkinter
pencere = tkinter.Tk()
pencere.geometry("500x500")

buton = tkinter.Button(text ="Bana tıkla",bg = "black",fg = "white",width = 10,height = 5)
buton.pack()

pencere.mainloop()