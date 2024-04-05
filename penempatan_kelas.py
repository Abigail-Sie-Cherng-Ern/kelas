#Atur cara menentukkan penempatan kelas

nama=str(input("Masukkan nama anda:"))
markah=int(input("Masukkan markah anda:"))

#Kategori kelas
if markah <=40:
    print("Anda ditempatkan di kelas Dedikasi")
elif markah <=60:
    print("Anda ditempatkan di kelas Cerdik")
elif markah <=80:
    print("Anda ditempatkan di kelas Bijak")
elif markah >80:
    print("Anda ditempatkan di kelas Amanah")
