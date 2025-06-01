# TASK-REPOSITORY 
# Penjelasan Lengkap Flow Proses Script Python: Validasi Input, Cek Tahun Kabisat, dan Hitung Hari dengan Zeller’s Congruence

Berikut penjelasan secara rinci alur proses script Python yang Anda berikan, lengkap dengan fungsi-fungsi yang ada, tujuan masing-masing bagian, dan alasan mengapa fitur tersebut penting. Penjelasan ini dibuat dengan bahasa yang mudah dipahami agar bisa dimengerti setiap langkahnya dengan jelas.

# Struktur Utama Script
Script ini terdiri dari beberapa bagian utama:
1.	Fungsi validasi_input() = untuk meminta dan memvalidasi input tanggal, bulan, dan tahun dari pengguna.
2.	Proses cek tahun kabisat = untuk menentukan apakah tahun tertentu termasuk tahun kabisat atau bukan.
3.	Perhitungan hari menggunakan Zeller’s Congruence = untuk menghitung hari dalam minggu berdasarkan tanggal yang dimasukkan.

# 1. Fungsi validasi_input()

Tujuan: Memastikan input yang dimasukkan oleh pengguna valid dan sesuai dengan batasan yang logis.

Kenapa penting?
- Mencegah error saat program berjalan karena input yang tidak sesuai (misalnya huruf, angka di luar rentang).
- Memudahkan pengguna dengan memberikan pesan kesalahan yang jelas dan meminta input ulang hanya pada bagian yang salah.

Cara kerja:
- Ada tiga loop terpisah untuk tanggal, bulan, dan tahun.
- Setiap input dicek apakah sesuai dengan batasan (tanggal 1-31, bulan 1-12, tahun positif).
- Jika input salah, program akan menampilkan pesan error dan meminta input ulang hanya pada bagian yang salah, tanpa mengulang input yang sudah benar.

# 2. Proses Cek Tahun Kabisat

Tujuan: Menentukan apakah suatu tahun termasuk tahun kabisat atau bukan.

Apa itu tahun kabisat?
Tahun kabisat adalah tahun yang memiliki 366 hari (bukan 365), dengan tambahan 1 hari di bulan Februari (29 Februari).

Aturan kabisat:
Tahun habis dibagi 4 dan tidak habis dibagi 100, atau Tahun habis dibagi 400.

Kenapa penting?
- Informasi ini penting untuk validasi tanggal (misalnya, Februari bisa 28 atau 29 hari).
- Memberikan informasi tambahan kepada pengguna tentang tahun yang dimasukkan dan tahun-tahun di sekitarnya.

Cara kerja:
- Program mengecek 5 tahun, dari 2 tahun sebelum sampai 2 tahun setelah tahun input.
- Untuk setiap tahun, dicek apakah memenuhi aturan kabisat.
- Hasilnya ditampilkan ke pengguna.

# 3. Perhitungan Hari dengan Zeller’s Congruence

Tujuan: Menghitung hari dalam minggu (Senin, Selasa, dst.) berdasarkan tanggal, bulan, dan tahun yang dimasukkan.

Apa itu Zeller’s Congruence?
- Algoritma matematika yang digunakan untuk menentukan hari dalam minggu dari sebuah tanggal tertentu.
- Menggunakan rumus khusus yang mempertimbangkan tahun, bulan, dan tanggal.

Kenapa penting?
- Memberikan informasi hari yang tepat untuk tanggal yang dimasukkan.
- Berguna untuk aplikasi kalender, penjadwalan, dan validasi tanggal.

Penyesuaian bulan dan tahun:
- Januari dan Februari dianggap sebagai bulan ke-13 dan ke-14 tahun sebelumnya untuk memudahkan perhitungan.

Variabel:
- K adalah dua digit terakhir tahun.
- J adalah dua digit pertama tahun (abad).

Hasil h:
Nilai h adalah angka dari 0 sampai 6 yang mewakili hari dalam minggu (Sabtu sampai Jumat).

# 4. Menampilkan Hasil Hari

Tujuan: Mengubah hasil perhitungan h menjadi nama hari yang mudah dimengerti.

Kenapa penting?
- Agar hasil perhitungan dapat dipahami oleh pengguna.
- Memberikan output yang informatif dan user-friendly.

Cara kerja:
- Menggunakan struktur if-elif-else untuk mencocokkan nilai h dengan nama hari.
- Menampilkan hasil akhir berupa tanggal lengkap dan hari dalam minggu.

# Ringkasan Flow Acript
![flow](https://github.com/Farhan-Fadillah/picture_list/blob/b601b5397694e082f0afecca763f0cd74282b4ea/table%20zeellers%20conguerence.png)

# Kesimpulan
Script ini dirancang untuk:
- Memastikan input tanggal valid dan sesuai aturan.
- Memberikan informasi tambahan tentang tahun kabisat di sekitar tahun input.
- Menghitung dan menampilkan hari dalam minggu dari tanggal yang dimasukkan dengan akurat.
Setiap bagian memiliki fungsi yang jelas dan saling melengkapi untuk membuat program yang user-friendly dan fungsional.


