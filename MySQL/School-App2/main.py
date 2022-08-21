from datetime import datetime
from Tables.teacher import Teacher
from Tables.student import Student
from dbmanager import DBManager

dbmanager = DBManager()

msg = "*****************\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Çıkış"
while True:
    print(msg)
    cvp = int(input("Seçiminiz: "))
    match cvp:
        case 1:
            students = dbmanager.get_all_students()
            for student in students:
                student = list(student)
                student.pop(6)
                student.pop(6)
                student.pop(7)
                student.pop(7)
                student.pop(7)
                student.pop(9)
                print("ID: {}, Student No: {}, Student Name and Surname:{} {}, Student Birthdate: {}, Student Gender: {}, Student Class Name: {}, Teacher's Name and Surname: {} {}".format(*student))
        case 2:
            txt = input("Sırasıyla öğrenci id, no, isim, soyisim, doğum tarihi, cinsiyeti ve sınıf id'sini aralarına virgül koyarak yazınız:")
            txt = txt.split(",")
            for index, data in enumerate(txt):
                txt[index] = data.strip()
            if txt[0] == "None":
                txt[0] = None
            txt[4] = txt[4].split("-")
            for index, data in enumerate(txt[4]):
                txt[4][index] = int(data)
            txt[4] = datetime(*txt[4], 0, 0, 0, 0)
            dbmanager.add_student(Student(*txt))
        case 3:
            txt = input("Düzenlemek istediğin öğrencinin ID numarasını ve ardından düzenlemek istediğiniz özellikleri aralarına virgül koyarak yazınız: ").split(",")
            student = dbmanager.get_student_by_id(txt[0])
            no = student.no
            name = student.name
            surname = student.surname
            birthdate = student.birthdate
            gender = student.gender
            classId = student.classId
            for i in txt[1:]:
                match i:
                    case "no":
                        no = input(f"Numarası {student.no} olan öğrencinin yeni numarasını giriniz: ")
                    case "name":
                        name = input(f"Adı {student.name} olan öğrencinin yeni adını giriniz: ")
                    case "surname":
                        surname = input(f"Soyadı {student.surname} olan öğrencinin yeni soyadını giriniz: ")
                    case "birthdate":
                        birthdate = datetime(*list(map(lambda x: int(x), input(f"Doğum tarihi {student.birthdate} olan öğrencinin yeni doğum tarihini giriniz: ").split("-"))), 0, 0, 0, 0)
                    case "gender":
                        gender = input(f"Cinsiyeti {student.gender} olan öğrencinin yeni cinsiyetini giriniz: ")
                    case "classId":
                        classId = input(f"Sınıf ID numarası {student.classId} olan öğrencinin yeni sınıf ID numarasını giriniz: ")
            dbmanager.edit_student(Student(txt[0], no, name, surname, birthdate, gender, classId))
        case 4:
            id = input("Silmek istediğin öğrencinin ID numarasını giriniz: ")
            student = dbmanager.get_student_by_id(int(id))
            while True:
                print("Silmek istediğin öğrenci bilgileri aşağıdadır.")
                print("ID: {}, No: {}, Name: {}, Surname: {}, Birthdate: {}, Gender: {}, Class ID: {}".format(*(str(student).split(","))))
                cvp1 = input("Silmek istediğinize emin misiniz (E/H): ")
                if cvp1 == 'E':
                    dbmanager.del_student(int(id))
                    break
                elif cvp1 == 'H':
                    print("Silme işleminiz iptal edildi.")
                    break
                else:
                    print("Hatalı cevap !")
        case 5:
            txt = input("Sırasıyla öğretmen id, branş, isim, soyisim, doğum tarihi ve cinsiyeti aralarına virgül koyarak yazınız:")
            txt = txt.split(",")
            for index, data in enumerate(txt):
                txt[index] = data.strip()
            if txt[0] == "None":
                txt[0] = None
            txt[4] = txt[4].split("-")
            for index, data in enumerate(txt[4]):
                txt[4][index] = int(data)
            txt[4] = datetime(*txt[4], 0, 0, 0, 0)
            dbmanager.add_teacher(Teacher(*txt))
        case 6:
            break