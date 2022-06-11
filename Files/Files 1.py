# Dosya açmak veya oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adı, dosya_erişme_modu)
# dosya_erişme_modu parametresi, dosyayı hangi amaçla açtığımızı belirtir.

# "w" (Write): Yazma modu.
# ** Dosyayı konumda oluşturur.
# ** Yazma işlemine geçmeden önce dosya içeriğini siler.
file1 = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile1.txt", "w", encoding="utf-8")
file1.write("Hilmi Güner")
file1.close()

# "a" (Append): Ekleme modu.
# ** Dosyayı konumda oluşturur
# ** İçeriği silmeden, üzerine ekleme yaparak yazım yapar.
file1 = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile1.txt", "a", encoding="utf-8")
file1.write("Eklenmiş metin.")
file1.close()

# "x" (Create): Oluşturma modu. Dosya zaten varsa hata verir.
file2 = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile2.txt", "a", encoding="utf-8")
file2.close()

# "r" (Read): Okuma modu. Dosya konumda yoksa hata verir.
