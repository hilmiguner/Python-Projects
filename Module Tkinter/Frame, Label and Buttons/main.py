import tkinter
nesne = tkinter.Tk() #Pencereyi oluşturduk.
nesne.geometry("700x200") #Bouyutunu belirledik. (Default = 200x200)

etiket = tkinter.Label(text = "Başlık") #Etiket oluşturduk(Yazı ve resimler için)
etiket.pack() #Görünür hale getirdik.

tus = tkinter.Button(text = "Tamam",command = nesne.destroy) #Tuş oluşturduk, tuşa basınca pencere kapanır.
tus.pack() #Görünür hale getirdik.

nesne.mainloop() #Pencereyi çalıştırdık.