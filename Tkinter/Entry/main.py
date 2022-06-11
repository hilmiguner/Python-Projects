import tkinter
pencere = tkinter.Tk()
pencere.geometry("500x300")

etiket = tkinter.Label(text = "Name")
etiket.pack()

entry = tkinter.Entry(fg = "yellow",bg = "blue",width = 50)
#Entry widgetları height özelliği alamaz.
entry.pack()

pencere.mainloop()