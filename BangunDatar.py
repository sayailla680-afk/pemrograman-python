print("\nAPLIKASI PENGHITUNG LUAS DAN KELILING BANGUN DATAR")
name = input ("\nmasukan nama anda: ")
print("Halo", name)
 
daftarbangundatar = ["1. segitiga", "2. lingkaran", "3. persegi", "4. persegi_panjang"]
print(daftarbangundatar)

# menggunakan fungsi(def)
def Segitiga():
    print("Anda memilih segitiga")
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi= float(input("Masukkan tinggi segitiga: "))
    sisi_miring = float(input("Masukkan sisi_miring segitiga: "))
    luas = 0,5 * alas * tinggi
    keliling = alas + tinggi + sisi_miring
    print("Luas Segitiga:", luas)
    print("Keliling Segitiga:",keliling)
def Lingkaran():
    print("Anda memilih Lingkaran")
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    print("Luas Lingkaran:", luas)
    print("Keliling Lingkaran:", keliling)
def Persegi():
    print("Anda memilih persegi")
    sisi = float(input("Masukkan sisi persegi: "))
    luas = sisi * sisi 
    keliling = 4 * sisi
    print("Luas Persegi:", luas)
    print("Keliling Persegi:", keliling)
def Persegi_panjang():
    print("Anda memilih Persegi Panjang")
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    keliling = 2 * (panjang + lebar)
    print("Keliling Persegi Panjang:", keliling)

# Meminta pengguna memilih bangun datar terdaftar yang akan dihitung luas dan kelilingnya
pilih = input("\nSilahkan Pilih Bangun Datar (1-4): ")
if pilih == "1":
    Segitiga()
elif pilih == "2":
    Lingkaran()
elif pilih == "3":
    Persegi()
elif pilih == "4":
    Persegi_panjang() 
else:
    print("\nInput tidak valid. silahan pilih bangun datar dari 1-4.")

# Bertanya ke pengguna mau hitung lagi atau tidak. Kalo ya, program akan jalan lagi
# Kalo tidak, ucapkan terimakasih
# Di sini berlaku perulangan while
while True:
    hitung_lagi = input("\nApakah Anda ingin menghitung lagi? (ya/tidak): ")
    if hitung_lagi == "ya":
        pilih = input("\nSilakan pilih Bangun Datar (1-4): ")
        if pilih == "1":
            Segitiga()
        elif pilih == "2":
            Lingkaran()
        elif pilih == "3":
            Persegi()
        elif pilih == "4":
            Persegi_panjang()
        else:
            print("\nInput tidak valid. Silahkan pilih bangun datar dari 1-4.")
    elif hitung_lagi == "tidak":
        print("Okey, Terima kasih telah menggunakan program ini :")
        break
    else:
        print("Input tidak valid. Silahkan jawab dengan 'ya'atau 'tidak'.")


                      
          
          
          
