import tkinter
#Text ile entry aynıdır ancak text bir satırdan fazlasını alır bu sebeple height özelliğide sorunsuz çalışır.
pencere = tkinter.Tk()

etiket1 = tkinter.Label(text = "Entry")
etiket1.pack()
entry = tkinter.Entry()
entry.pack()

etiket2 = tkinter.Label(text = "Text")
etiket2.pack()
text = tkinter.Text()
text.pack()

etiket3 = tkinter.Label(text = "Boyutu Ayarlama")
etiket3.pack()
text1 = tkinter.Text(height = 10, width = 10)
text1.pack()

pencere.mainloop()