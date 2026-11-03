# Jurnal Vibe Coding — Jobsheet 1 
  
Nama: Muhammad Rapianur   NIM: 24554010004   Kelas: Sistem Informasi 
  
| No | Tujuan | Prompt (ringkas) | Hasil AI | Keputusan | Alasan | 
|----|--------|------------------|----------|-----------|--------| 
| 1  | Beranda + formulir nama | Membuat web Flask satu halaman beranda dengan judul 'Halo Sampit!', waktu server saat ini, dan form input nama tanpa database/JS, aman dari XSS. | Menghasilkan berkas app.py, templates/index.html, dan penjelasan cara kerja 5 butir. | Terima | Semua kriteria penerimaan (a)–(d) terpenuhi, aplikasi berjalan normal di localhost:5000, hanya menggunakan pustaka standar, dan terbukti aman dari XSS saat diuji dengan tag <b>tes</b>. |
| 2  | Tambah salam sesuai waktu | Tambahkan fungsi salam_waktu(jam) untuk mengembalikan salam dinamis (pagi, siang, sore, malam) sebelum waktu server tanpa mengubah fitur lain atau menambah paket baru. | Potongan kode fungsi salam_waktu(jam) pada app.py serta pembaruan elemen salam pada templates/index.html. | Terima | Fungsi lolos uji seluruh batas jam (3, 4, 10, 11, 14, 15, 17, 18) di terminal dan sapaan waktu berhasil tampil di beranda sebelum waktu server. |
| 3  | Halaman baru /tentang | Tambahkan rute /tentang yang menampilkan data nama, NIM, kelas, dan kelompok beserta tautan navigasi bolak-balik ke beranda. | Rute /tentang pada app.py, berkas baru templates/tentang.html, dan penambahan tautan link pada templates/index.html. | Terima | Rute dan template berhasil dirender dengan status 200, identitas tampil lengkap, dan tautan navigasi kedua arah berfungsi dengan baik. |
| 4  | Validasi batas karakter di server | Tambahkan pembatasan panjang nama maksimal 50 karakter di sisi server pada app.py untuk mengantisipasi manipulasi maxlength klien. | Penambahan pemotongan string [:50] pada app.py dan atribut maxlength="50" pada form templates/index.html. | Terima | Terbukti berhasil menahan input 80 karakter yang dimanipulasi via Inspect Element menjadi tepat 50 karakter di sisi server. |
| 5  | Eksperimen prompt | Bandingkan hasil keluaran prompt singkat 'Buatkan aplikasi web Halo Sampit' dengan prompt terstruktur Langkah 7. | Analisis perbandingan jumlah berkas, kepatuhan batasan, dan jumlah perbaikan yang diperlukan. | Terima | Prompt terstruktur terbukti jauh lebih efisien, terarah, dan menghasilkan kode yang langsung sesuai spesifikasi tanpa dependensi berlebih. |

---

## Pembahasan Latihan Mandiri

### 1. Bukti & Alasan Mengapa Validasi di Server Tetap Diperlukan (Latihan Mandiri 2)
- **Hasil Percobaan:** Ketika nilai atribut `maxlength="50"` diubah menjadi `80` melalui Inspect Element (F12) lalu dikirim 80 karakter, server Flask tetap memotong masukan menjadi maksimal 50 karakter berkat kode `request.form.get("nama", "").strip()[:50]`.
- **Alasan:** Validasi di sisi klien (HTML/JavaScript) hanya berfungsi untuk kenyamanan pengguna (*user experience*) dan tidak menjamin keamanan karena sangat mudah dimanipulasi melalui Developer Tools ataupun dilewati langsung menggunakan HTTP client (seperti cURL atau Postman). Oleh karena itu, validasi di sisi server merupakan garda pertahanan utama yang mutlak diperlukan untuk memastikan integritas data dan keamanan aplikasi.

### 2. Kesimpulan Eksperimen Prompt dalam Tiga Kalimat (Latihan Mandiri 3)
1. Prompt yang terlalu singkat membuat AI berspekulasi sehingga sering menghasilkan berkas tunggal yang tidak terstruktur atau justru menambahkan pustaka yang tidak diinginkan seperti JavaScript dan basis data.
2. Sebaliknya, prompt terstruktur dengan konteks, batasan, dan format luaran yang jelas menghasilkan struktur kode modular (`app.py` dan `templates/`) yang 100% patuh pada spesifikasi teknis.
3. Dengan demikian, prompt terstruktur secara signifikan memangkas waktu pengujian dan mengurangi kebutuhan revisi kode dalam siklus *vibe coding*.
