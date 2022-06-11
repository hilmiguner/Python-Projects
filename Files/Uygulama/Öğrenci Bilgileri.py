# encoding:utf-8
from tkinter import *
def getinfo():
    import re

    def war_button_command1():
        war_pen.destroy()
    name = (e1.get()).lower()
    if re.search("[0-9]", name):
        check1 = False
        war_pen = Tk()
        war_label = Label(master=war_pen, text="Adınız sayı içeremez.")
        war_label.pack()
        war_button = Button(master=war_pen, text="Tamam", command=war_button_command1)
        war_button.pack()
        war_pen.mainloop()
    else:
        check1 = True
    surname = (e2.get()).lower()
    if re.search("[0-9]", surname):
        check2 = False
        war_pen = Tk()
        war_label = Label(master=war_pen, text="Soyadınız sayı içeremez.")
        war_label.pack()
        war_button = Button(master=war_pen, text="Tamam", command=war_button_command1)
        war_button.pack()
        war_pen.mainloop()
    else:
        check2 = True
    age = (e3.get()).lower()
    if re.search("[a-z]", age):
        check3 = False
        war_pen = Tk()
        war_label = Label(master=war_pen, text="Yaşınız harf içeremez.")
        war_label.pack()
        war_button = Button(master=war_pen, text="Tamam", command=war_button_command1)
        war_button.pack()
        war_pen.mainloop()
    else:
        check3 = True
    mark1 = (e4.get()).lower()
    if re.search("[a-z]", mark1):
        check4 = False
        war_pen = Tk()
        war_label = Label(master=war_pen, text="Notunuz harf içeremez.")
        war_label.pack()
        war_button = Button(master=war_pen, text="Tamam", command=war_button_command1)
        war_button.pack()
        war_pen.mainloop()
    else:
        check4 = True
    mark2 = (e5.get()).lower()
    if re.search("[a-z]", mark2):
        check5 = False
        war_pen = Tk()
        war_label = Label(master=war_pen, text="Notunuz harf içeremez.")
        war_label.pack()
        war_button = Button(master=war_pen, text="Tamam", command=war_button_command1)
        war_button.pack()
        war_pen.mainloop()
    else:
        check5 = True
    mark3 = (e6.get()).lower()
    if re.search("[a-z]", mark3):
        check6 = False
        war_pen = Tk()
        war_label = Label(master=war_pen, text="Notunuz harf içeremez.")
        war_label.pack()
        war_button = Button(master=war_pen, text="Tamam", command=war_button_command1)
        war_button.pack()
        war_pen.mainloop()
    else:
        check6 = True
    if check1 and check2 and check3 and check4 and check5 and check6:
        lastcheck = True
    else:
        lastcheck = False
    if not lastcheck:
        ogrenci_kayit_command2()
    elif lastcheck:
        try:
            studentinfofile = open("studentinfo.txt", "r", encoding="utf-8")
        except Exception:
            with open("studentinfo.txt", "x", encoding="utf-8"):
                pass
        else:
            studentinfofile.close()
        studentinfofile = open("studentinfo.txt", "r", encoding="utf-8")
        studentinfofile.seek(0)
        content = studentinfofile.read()
        if re.search(f"{name}\n{surname}", content):
            def war_button_command2():
                war_pen.destroy()
                pencere2.destroy()
                main1()
            war_pen = Tk()
            war_label = Label(master=war_pen, text="Girdiğiniz bilgiler sisteme daha önceden dahil edilmiş.")
            war_label.pack()
            war_button = Button(master=war_pen, text="Tamam", command=war_button_command2)
            war_button.pack()
            war_pen.mainloop()
        else:
            studentinfofile.seek(0)
            temp1 = len(studentinfofile.read())
            studentinfofile.close()
            studentinfofile = open("studentinfo.txt", "a", encoding="utf-8")
            studentinfofile.seek(temp1)
            studentinfofile.write(f"{name}\n")
            studentinfofile.write(f"{surname}\n")
            studentinfofile.write(f"{age}\n")
            studentinfofile.write(f"{mark1}\n")
            studentinfofile.write(f"{mark2}\n")
            studentinfofile.write(f"{mark3}\n")
            studentinfofile.write(f"{(float(mark1)+float(mark2)+float(mark3))/3}\n")
            studentinfofile.close()
            pencere2.destroy()
            main1()
def ogrenci_kayit_command2():
    global e1, e2, e3, e4, e5, e6, pencere2
    pencere2 = Tk()

    f1 = Frame(master=pencere2, pady=10)
    l1 = Label(master=f1, text="Adınız", padx=10)
    l1.pack(side="left")
    e1 = Entry(master=f1)
    e1.pack(side="left")
    f1.pack()

    f2 = Frame(master=pencere2, pady=10)
    l2 = Label(master=f2, text="Soyadınız", padx=1)
    l2.pack(side="left")
    e2 = Entry(master=f2)
    e2.pack(side="left")
    f2.pack()

    f3 = Frame(master=pencere2, pady=10)
    l3 = Label(master=f3, text="Yaşınız", padx=9)
    l3.pack(side="left")
    e3 = Entry(master=f3)
    e3.pack(side="left"),
    f3.pack()

    f4 = Frame(master=pencere2, pady=10)
    f4_1 = Frame(master=f4)
    l4 = Label(master=f4_1, text="Notlarınız")
    l4.pack()
    f4_1.pack(side="left")
    f4_2 = Frame(master=f4)
    e4 = Entry(master=f4_2)
    e4.pack()
    e5 = Entry(master=f4_2)
    e5.pack()
    e6 = Entry(master=f4_2)
    e6.pack()
    f4_2.pack(side="left")
    f4.pack()

    f5 = Frame(master=pencere2, pady=10)
    b1 = Button(master=f5, text="Gönder", command=getinfo)
    b1.pack()
    f5.pack()
    pencere2.mainloop()
def ogrenci_kayit_command():
    global e1, e2, e3, e4, e5, e6, pencere2
    pencere1.destroy()

    pencere2 = Tk()

    f1 = Frame(master=pencere2, pady=10)
    l1 = Label(master=f1, text="Adınız", padx=10)
    l1.pack(side="left")
    e1 = Entry(master=f1)
    e1.pack(side="left")
    f1.pack()

    f2 = Frame(master=pencere2, pady=10)
    l2 = Label(master=f2, text="Soyadınız", padx=1)
    l2.pack(side="left")
    e2 = Entry(master=f2)
    e2.pack(side="left")
    f2.pack()

    f3 = Frame(master=pencere2, pady=10)
    l3 = Label(master=f3, text="Yaşınız", padx=9)
    l3.pack(side="left")
    e3 = Entry(master=f3)
    e3.pack(side="left"),
    f3.pack()

    f4 = Frame(master=pencere2, pady=10)
    f4_1 = Frame(master=f4)
    l4 = Label(master=f4_1, text="Notlarınız")
    l4.pack()
    f4_1.pack(side="left")
    f4_2 = Frame(master=f4)
    e4 = Entry(master=f4_2)
    e4.pack()
    e5 = Entry(master=f4_2)
    e5.pack()
    e6 = Entry(master=f4_2)
    e6.pack()
    f4_2.pack(side="left")
    f4.pack()

    f5 = Frame(master=pencere2, pady=10)
    b1 = Button(master=f5, text="Gönder", command=getinfo)
    b1.pack()
    f5.pack()
    pencere2.mainloop()
def ogrenciyi_bul_command():
    global age, mark1, mark2, mark3, avgmark, tempname, tempsurname, tempcheck

    def displaying_student_info():
        global age, mark1, mark2, mark3, avgmark, tempname, tempsurname
        age = templist[tempnumber+2]
        mark1 = templist[tempnumber+3]
        mark2 = templist[tempnumber+4]
        mark3 = templist[tempnumber+5]
        avgmark = templist[tempnumber+6]
        tempname = (templist[tempnumber][0].upper() + templist[tempnumber][1:])
        tempsurname = (templist[tempnumber+1][0].upper() + templist[tempnumber+1][1:])

    def war_button_command():
        war_pen.destroy()

    def student_info_button_command():
        studentinfo_pen.destroy()
    name = str(e3_1.get().lower())
    surname = str(e3_2.get().lower())
    with open("studentinfo.txt", "r", encoding="utf-8") as file:
        file.seek(0)
        content = file.read()
        templist = content.split("\n")
    for i in range(0, len(templist)-1):
        if templist[i] == name and templist[i+1] == surname:
            tempcheck = True
            tempnumber = i
            break
        else:
            tempcheck = False
    if tempcheck == False:
        war_pen = Tk()
        war_label = Label(master=war_pen, text="Aradığınız öğrenci sisteme kayıtlı değildir.")
        war_label.pack()
        war_button = Button(master=war_pen, text="Tamam", command=war_button_command)
        war_button.pack()
        war_pen.mainloop()
    elif tempcheck == True:
        displaying_student_info()
        studentinfo_pen = Tk()
        studentinfo_label1 = Label(master=studentinfo_pen, text=f"Öğrencinin adı {tempname}")
        studentinfo_label1.pack()
        studentinfo_label2 = Label(master=studentinfo_pen, text=f"Öğrencinin soyadı {tempsurname}")
        studentinfo_label2.pack()
        studentinfo_label3 = Label(master=studentinfo_pen, text=f"Öğrencinin yaşı {age}")
        studentinfo_label3.pack()
        studentinfo_label4 = Label(master=studentinfo_pen, text=f"Öğrencinin birinci notu {mark1}")
        studentinfo_label4.pack()
        studentinfo_label5 = Label(master=studentinfo_pen, text=f"Öğrencinin ikinci notu {mark2}")
        studentinfo_label5.pack()
        studentinfo_label6 = Label(master=studentinfo_pen, text=f"Öğrencinin üçüncü notu {mark3}")
        studentinfo_label6.pack()
        studentinfo_label7 = Label(master=studentinfo_pen, text=f"Öğrencinin not ortalaması {avgmark}")
        studentinfo_label7.pack()
        studentinfo_button = Button(master=studentinfo_pen, text="Tamam", command=student_info_button_command)
        studentinfo_button.pack()
        studentinfo_pen.mainloop()
def varolan_ogrenci():
    global e3_1, e3_2
    pencere3 = Tk()
    f3_1 = Frame(master=pencere3)
    l3_1 = Label(master=f3_1, text="Öğrencinin Adı", padx=10)
    l3_1.pack(side="left")
    e3_1 = Entry(master=f3_1)
    e3_1.pack(side="left")
    f3_1.pack()
    f3_2 = Frame(master=pencere3)
    l3_2 = Label(master=f3_2, text="Öğrencinin Soyadı")
    l3_2.pack(side="left")
    e3_2 = Entry(master=f3_2)
    e3_2.pack(side="left")
    f3_2.pack()
    b3_1 = Button(master=pencere3, text="Öğrenciyi Bul", command=ogrenciyi_bul_command)
    b3_1.pack()
    pencere3.mainloop()
def main1():
    global pencere1
    pencere1 = Tk()
    pencere1.geometry("220x50")
    pencere1.resizable(False, False)
    f1 = Frame(master=pencere1)
    b1 = Button(master=f1, text="Öğrenci Kayıt", command=ogrenci_kayit_command)
    b1.pack()
    f1.pack(side="left")
    f2 = Frame(master=pencere1)
    b2 = Button(master=f2, text="Varolan Öğrenci Bilgileri", command=varolan_ogrenci)
    b2.pack()
    f2.pack(side="left")
    pencere1.mainloop()
main1()
