import tkinter

def cikis(): #Tuşa basınca çalıştırılacak bir fonksiyon yazdık.
    etiket["text"] = "Pencere kapatılıyor" #Etiketin text değerini değiştirir.
    tus["text"] = "Bekleyiniz..." #Tuşun text değerini değiştirir.
    tus["state"] = "disabled" #Tuşun basılabilme özelliğini kapatır.
    nesne.after(2000,nesne.destroy) #Son olarak pencereyei 2000 milisaniye yani 2 saniye sonra kapatır.


nesne = tkinter.Tk()
nesne.geometry("700x200")

etiket = tkinter.Label(text = "Pencere açık")
etiket.pack()

tus = tkinter.Button(text = "Kapatmak için tıklayın",command = cikis) #Command değerini cikis fonksiyonumuz yaptık.
tus.pack()

nesne.protocol("WM_DELETE_WINDOW",cikis) #Pencerenin çarpı tuşuna basınca devreye girecek fonksiyonu belirledik.

nesne.mainloop() #Pencereyi çalıştırdık.