# input

jumlah = int(input("Masukkan Jumlah Mahasiswa: "))

lulus = 0
tidak_lulus = 0

for i in range(jumlah):
    print("\nMahasiswa ke-", i + 1)
    nama = input("Masukkan Nama Mahasiswa: ")
    nilai = int(input("Masukkan Nilai: "))

    if nilai >= 85 and nilai <= 100:
        print("Nilai: A (Sangat Baik)")
        lulus += 1
    elif nilai >= 75 and nilai <= 84:
        print("Nilai: B (Baik)")
        lulus += 1
    elif nilai >= 60 and nilai <= 74:
        print("Nilai: C (Cukup)")
        lulus += 1
    elif nilai >= 0:
        print("Nilai: D (Tidak Lulus)")
        tidak_lulus += 1
    else:
        print("Nilai tidak valid")

    print("Nama:", nama)
    print("Nilai: ", nilai)

print("\n=========== HASIL PENILAIAN ==========")
print("Jumlah Mahasiswa: ", jumlah)
print("Jumlah lulus: ", lulus)
print("Jumlah tidak lulus: ", tidak_lulus)