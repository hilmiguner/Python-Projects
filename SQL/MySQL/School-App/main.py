from studentclass import Student

# ---------------------------------------------------------------------------------------
# Tek kayıt eklemek için.
# ahmet = Student("102", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E")
# ahmet.saveStudent()

# Birden fazla kayıt eklemek için.
# ogrenciler = [
#     ("501","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
#     ("502","Ali","Can",datetime(2005, 6, 17),"E"),
#     ("503","Canan","Tan",datetime(2005, 7, 7),"K"),
#     ("504","Ayşe","Taner",datetime(2005, 9, 23),"K"),
#     ("505","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
#     ("506","Ali","Cenk",datetime(2003, 8, 25),"E")
# ]
# Student.saveStudents(ogrenciler)
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
#   Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
Student.get_all_students()

print(100*"*")

#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
Student.get_all_students_specify("no", "name", "surname")

print(100*"*")

#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
Student.get_all_girls_name_surname()

print(100*"*")

#   d- 2003 doğumlu öğrenci bilgilerini alınız. 
Student.get_all_students_by_birthyear(2003)

print(100*"*")

#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
Student.get_students_by_name_and_birthyear("Ali", 2005)

print(100*"*")

#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
Student.get_students_by_including_txt_in_name_or_surname("an")

print(100*"*")

#   g- Kaç erkek öğrenci vardır ?
result = Student.get_student_number_by_gender("E")
if result == -1:
    print("Successfully fetched students but there is no student in database according these filters.")
else:
    print(f"There are total {result[0]} male students.")

print(100*"*")

#   h- Kız öğrencileri harf sırasına göre getiriniz.
Student.get_girls_by_name_order()

print(100*"*")

#   i- Tüm öğrencilerin ilk 5 tanesini getir.
Student.get_students_by_limit(8)

print(100*"*")
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
Student.set_student_by_id(12, no=1050, surname="Güner")

print(100*"*")

#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
Student.set_student_by_gender("K", name="Zeynep")

print(100*"*")
# ---------------------------------------------------------------------------------------