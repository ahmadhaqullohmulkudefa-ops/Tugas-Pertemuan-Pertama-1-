def cek_ganjil_genap():
    angka = int(input("Masukkan sebuah angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan GENAP")
    else:
        print(f"{angka} adalah bilangan GANJIL")


def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print(f"Luas persegi panjang = {luas}")


def tampilkan_menu():
    print("\n===== MENU PROGRAM =====")
    print("1. Cek Bilangan Ganjil/Genap")
    print("2. Hitung Luas Persegi Panjang")
    print("3. Keluar")
    print("=========================")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            cek_ganjil_genap()
        elif pilihan == "2":
            hitung_luas_persegi_panjang()
        elif pilihan == "3":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")


main()