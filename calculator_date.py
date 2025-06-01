# Program Lengkap: Cek Kabisat dan Hitung Hari dengan Loop

def validasi_input():
    while True:
        # Validasi tanggal
        while True:
            try:
                tanggal = int(input("Masukkan tanggal (1-31): "))
                if 1 <= tanggal <= 31:
                    break
                else:
                    print("Tanggal harus antara 1 dan 31!")
            except ValueError:
                print("Harus masukkan angka!")

        # Validasi bulan
        while True:
            try:
                bulan = int(input("Masukkan bulan (1-12): "))
                if 1 <= bulan <= 12:
                    break
                else:
                    print("Bulan harus antara 1 dan 12!")
            except ValueError:
                print("Harus masukkan angka!")

        # Validasi tahun
        while True:
            try:
                tahun = int(input("Masukkan tahun: "))
                if tahun > 0:
                    break
                else:
                    print("Tahun harus positif!")
            except ValueError:
                print("Harus masukkan angka!")

        # Jika semua input valid, keluar dari loop utama dan kembalikan nilai
        return tanggal, bulan, tahun

# Minta input valid
print("Masukkan tanggal untuk cek hari dan kabisat:")
tanggal, bulan, tahun = validasi_input()

# Cek kabisat untuk rentang tahun
print("\nCek tahun kabisat untuk rentang tahun:")
for i in range(tahun - 2, tahun + 3):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(f"Tahun {i} adalah tahun kabisat!")
    else:
        print(f"Tahun {i} bukan tahun kabisat!")

# Zeller’s Congruence untuk hitung hari
if bulan == 1 or bulan == 2:
    bulan += 12
    tahun -= 1
K = tahun % 100
J = tahun // 100
h = (tanggal + ((13 * (bulan + 1)) // 5) + K + (K // 4) + (J // 4) - 2 * J) % 7
print("\nHasil perhitungan hari:")
if h == 0:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Sabtu!")
elif h == 1:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Minggu!")
elif h == 2:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Senin!")
elif h == 3:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Selasa!")
elif h == 4:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Rabu!")
elif h == 5:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Kamis!")
else:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Jumat!")
