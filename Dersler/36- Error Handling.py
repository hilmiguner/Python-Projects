# Bir sayıyı sıfıra bölersek "ZeroDivisionError" adlı bir hata alırız.
# Sayı yerine başka bir karakter girersek "ValueError" alırız.
# Bu tarz hata mesajlarını yönetmek için try ve except komutlarını kullanırız.
try:
    print("ZeroDivisionError ve ValueError hatalarının ayrı ayrı işlenmesi")
    x = int(input("Birinci sayıyı giriniz:"))
    y = int(input("İkinci sayıyı giriniz:"))
    print(f"{x} sayısının, {y} sayısına bölümü: {x/y}")
except ZeroDivisionError:
    print("İkinci sayı sıfır olamaz.")
except ValueError:
    print("x ve y matematiksel bir işleme sokulacağı için sayısal değerler almalıdır.")

print(50*"-")

# Bu hataları tek tek yazmak yerine tek bir satıra sokabiliriz.
try:
    print("ZeroDivisionError ve ValueError hatalarının aynı anda işlenmesi")
    x = int(input("Birinci sayıyı giriniz:"))
    y = int(input("İkinci sayıyı giriniz:"))
    print(f"{x} sayısının, {y} sayısına bölümü: {x/y}")
except (ZeroDivisionError, ValueError):
    print("Hatalı bilgi girdiniz.")

print(50*"-")

# Bu şekilde kullandığımızda hangi hatanın bu olaya sebebiyet verdiğini bulmak için;
try:
    print("ZeroDivisionError ve ValueError hatalarının aynı anda işlenmesi ancak hatanın sebebinin belirtilmesi")
    x = int(input("Birinci sayıyı giriniz:"))
    y = int(input("İkinci sayıyı giriniz:"))
    print(f"{x} sayısının, {y} sayısına bölümü: {x/y}")
except (ZeroDivisionError, ValueError) as error:
    print("Hatalı bilgi girdiniz.")
    print(error)

print(50*"-")

# Bütün oluşabilecek hatalara karşı bir komut bloğu yazmak istersek;
print("Oluşabilecek tüm hatalara karşı bir yönetim ve program doğru yazılana kadar çalışacak bir while döngüsü")
while True:
    try:
        x = int(input("Birinci sayıyı giriniz:"))
        y = int(input("İkinci sayıyı giriniz:"))
        print(f"{x} sayısının, {y} sayısına bölümü: {x/y}")
    except:  # Ancak bu kullanımda hangi hatanın aşağıdaki komut bloğunu aktif ettiğini bulamayız.
        print("Hatalı bilgi girdiniz.")
    else:  # Bir hata çıkmazsa aşağıdaki komut bloğu aktif olur.
        break

print(50*"-")

# Spesifik bir hata yerine, tüm hata kodlarını kapsayan "Exception" kodunu kullanabiliriz.
# Ek olarak finally komutunu görüyoruz.
print("Oluşabilecek tüm hatalara karşı bir yönetim ve program doğru yazılana kadar çalışacak bir while döngüsü ve")
print("while döngüsünün devam etmesini sağlayan hatanın açıklanması ve ek olarak finally bloğu")
while True:
    try:
        x = int(input("Birinci sayıyı giriniz:"))
        y = int(input("İkinci sayıyı giriniz:"))
        print(f"{x} sayısının, {y} sayısına bölümü: {x/y}")
    except Exception as error:  # Ancak bu kullanımda hangi hatanın aşağıdaki komut bloğunu aktif ettiğini bulamayız.
        print(f"Hatalı bilgi girdiniz. ({error})")
    else:  # Bir hata çıkmazsa aşağıdaki komut bloğu aktif olur.
        break
    finally:  # Bu komut ne olursa olsun try ve except bloklarından çıktıktan sonra çalışır.
        print("Try ve except sonlandı.")

print(50*"-")
