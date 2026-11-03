from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Rute utama yang mendukung metode GET (menampilkan) dan POST (mengirim data)
@app.route("/", methods=["GET", "POST"])
def index():
    # Mengambil tanggal dan jam server saat ini menggunakan pustaka standar Python
    waktu_server = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    nama = None

    # Memeriksa apakah ada data form yang dikirim pengguna via POST
    if request.method == "POST":
        # Mengambil input nama dan memangkas spasi kosong di awal/akhir
        nama = request.form.get("nama", "").strip()

    # Mengirim data waktu dan nama ke template HTML
    return render_template("index.html", waktu_server=waktu_server, nama=nama)

if __name__ == "__main__":
    # Menjalankan server aplikasi di http://127.0.0.1:5000/ (localhost)
    app.run(debug=True)

