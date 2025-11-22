# PROGRAM PENETUAN NILAI DAN TEMPAT BILANGAN
# menggunakan fungsi try_except untuk menangani kesalahan (error), jika user input selain angka

# meminta input bilangan dari user
try:
    angka = int(input("\nMasukkan Bilangan:"))

    # penentuan nilai tempat 
    if 0 <= angka <= 999999999:

        #ambil nilai ratusan juta
        ratusanjuta = angka // 100000000
        #hitung sisa setelah ratusan juta diambil
        sisaratusanjuta = angka % 100000000

        #ambil nilai puluhan juta dari sisa ratusan juta
        puluhanjuta = sisaratusanjuta // 10000000
        #hitung sisa setelah puluhan juta diambil
        sisapuluhanjuta = sisaratusanjuta % 10000000

        #ambil nilai jutaan dari sisa puluhan juta
        jutaan = sisapuluhanjuta // 1000000
        #hitung sisa setelah setelah jutaan diambil
        sisajutaan = sisapuluhanjuta % 1000000

        #ambil nilai ratusan ribu dari sisa jutaaan 
        ratusanribu = sisajutaan // 100000
        #hitung sisa setelah ratusanribu diambil
        sisaratusanribu = sisajutaan % 100000

        #ambil nilai puluhan juta puluhan ribu dari sisa raatusan ribu 
        puluhanribu = sisaratusanribu // 10000
        #hitung sisa setelah ratusanribu diambil
        sisapuluhanribu = sisaratusanribu % 10000
    
        # ambil nilai ribuan dari puluhan ribu
        ribuan = sisapuluhanribu // 1000
        # hitung sisa setelah diambil ribuannya
        sisaribuan = sisapuluhanribu % 1000

        # ambil nilai ratusan dari sisa ribuan 
        ratusan = sisaribuan // 100
        # hitung sisa setelah diambil ratusannya
        sisaratusan = sisaribuan % 100

        # ambil nilai ratusan dari sisaribuan
        puluhan = sisaratusan // 10
        # sisa terakhir adalah satuan 
        satuan = sisaratusan % 10
                
        # menampilkan hasil sesuai dengan nilai tempat
        print(f"\nAnda memasukkan bilangan {angka} dimana:")
        print(f"{ratusanjuta} merupakan ratusan juta")
        print(f"{puluhanjuta} merupakan puluhan jutaan")
        print(f"{jutaan} merupakan jutaan")
        print(f"{ratusanribu} merupakan ratusan ribu")
        print(f"{puluhanribu} merupakan puluhan ribu")
        print(f"{ribuan} merupakan ribuan")
        print(f"{ratusan} merupakan ratusan")
        print(f"{puluhan} merupakan puluhan")
        print(f"{satuan} merupakan satuan")

    else:
        print("Harap masukkan bilangan antara 0-999999999 saja.")

except ValueError:
    print("Input tidak valid! Harap masukkan angka saja.")





