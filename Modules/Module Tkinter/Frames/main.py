import tkinter
#Frameler arayüzü parçalara ayırır.
pencere = tkinter.Tk()

frame1 = tkinter.Frame()
frame2= tkinter.Frame()

etiket1 = tkinter.Label(master = frame1 , text = "Frame 1'e ait etiket.",height = 5,bg="blue",fg = "white")
etiket1.pack()
etiket2 = tkinter.Label(master = frame2 , text = "Frame 2'ye ait etiket",height = 5,bg="red",fg="white")
etiket2.pack()

frame1.pack()
frame2.pack()

#Çerçevelerin etrafına belirleyici sınırlar koyabiliriz.

border_effects = {
    "flat" : tkinter.FLAT, #Defaul Value
    "sunken" : tkinter.SUNKEN,
    "raised" : tkinter.RAISED,
    "groove" : tkinter.GROOVE,
    "ridge": tkinter.RIDGE
}

for relief_name, relief_kind in border_effects.items():
    frame = tkinter.Frame(master=pencere,relief = relief_kind,borderwidth = 5)
    frame.pack(side = "left")
    label = tkinter.Label(master=frame,text = relief_name)
    label.pack()

pencere.mainloop()