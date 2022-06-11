def check_password(psw):
    import re
    if len(psw) < 7:
        raise Exception("Parola en az 7 karakterli olmalı.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir.")
    elif not re.search("[_@$]", psw):
        raise Exception("Parola alpha numeric karakter içermelidir.")
    elif re.search("\s", psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli parola.")
try:
    check_password("19770107")
except Exception as ex:
    print(ex)
