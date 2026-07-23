while True:
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan GENAP")
    else:
        print(f"{angka} adalah bilangan GANJIL")

    while True:
        lanjut = input("Ingin cek angka lain? y/n?: ")
        if lanjut.lower() == "y":
            break
        elif lanjut.lower() == "n":
            print("Program selesai.")
            raise SystemExit
        else:
            print("Input tidak valid. Silakan jawab y atau n.")