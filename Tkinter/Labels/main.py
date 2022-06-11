import tkinter
pencere = tkinter.Tk()

etiket = tkinter.Label(text = "Deneme",foreground = "white",background = "black")
#Fg yazının rengi, bg arkaplan rengi.
etiket.pack()

etiket2 = tkinter.Label(text = "Deneme 2",foreground = "red",background = "#34A2FE")
#Hexadecimal RGB değerleride işe yarar.
etiket2.pack()

etiket3 = tkinter.Label(text ="Deneme 3",fg = "yellow",bg = "green")
#Kısaltmaları kullanabilirsin. (fg,bg)
etiket3.pack()

etiket4 = tkinter.Label(text = "Deneme 4",bg="black",fg="white",width = 10,height = 5)
etiket4.pack()
#Boyutunu ayarlayabilirsin.

pencere.mainloop()