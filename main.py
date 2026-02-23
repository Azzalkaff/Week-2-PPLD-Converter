import importlib


modul_yen = importlib.import_module("program.falisha.converter-yen")
modul_dollar = importlib.import_module("program.najla.converter-dollar")
modul_euro = importlib.import_module("program.syahid.converter-euro") 
modul_ringgit = importlib.import_module("program.syaqila.converter-ringgit")


while True:
    print("\n======================================")
    print("    PROGRAM KONVERTER MATA UANG")
    print("======================================")
    print("1. Rupiah ke Yen")
    print("2. Rupiah ke Dollar")
    print("3. Rupiah ke Euro")
    print("4. Rupiah ke Ringgit")
    print("0. Keluar")
    print("======================================")

    pilihan = input("Pilih konversi (1/2/3/4/0): ")

    if pilihan in ["1", "2", "3", "4"]:

        try:
            jumlah_rupiah = float(input("\nMasukkan jumlah uang Rupiah: Rp "))
            
        
            if pilihan == "1":
                hasil = modul_yen.hitung_yen(jumlah_rupiah)
                mata_uang = "Yen"
            elif pilihan == "2":
                hasil = modul_dollar.hitung_dollar(jumlah_rupiah)
                mata_uang = "Dollar"
            elif pilihan == "3":
                hasil = modul_euro.hitung_euro(jumlah_rupiah)
                mata_uang = "Euro"
            elif pilihan == "4":
                hasil = modul_ringgit.hitung_ringgit(jumlah_rupiah)
                mata_uang = "Ringgit"
                
         
            print(f"-> Hasil konversi: {hasil:.2f} {mata_uang}")
            input("Tekan Enter untuk kembali ke menu utama...") 
            
        except ValueError:
           
            print("❌ ERROR: Masukan tidak valid! Harap masukkan angka saja (contoh: 50000 atau 15.5).")
            input("Tekan Enter untuk kembali ke menu utama...")

    elif pilihan == "0":
        print("Keluar dari program. Terima kasih!")
        break

    else:
        print("❌ Pilihan tidak valid. Silakan pilih nomor yang ada di menu.")
        input("Tekan Enter untuk mengulangi...")