# input

nama = input("Masukkan Nama Mahasiswa: ")

if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama Mahasiswa Tidak Terdaftar!")
    target = 0

if target != 0:
    print("Nama: ", nama)
    print("Target nilai: ", target)

    percobaan = 0
    nilai = 0

    while percobaan < 3 and nilai < target:
        percobaan += 1
        print("\nPercobaan ke-", percobaan)
        nilai = int(input("Masukkan nilai ujian: "))

        if nilai >= target:
            print("Nilai mencapai target!")
        else:
            print("Nilai tidak mencapai target.")

    if nilai >= target:
        print("\n", nama, "lulus!")
        print("Jumlah Percobaan: ", percobaan)
    else:
        print("\n", nama, "tidak lulus!")
        print("Sudah mencapai batas 3 kali percobaan.")