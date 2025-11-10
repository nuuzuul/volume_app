from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# wadah sederhana buat nyimpan riwayat perhitungan
riwayat = []   # setiap item: {"panjang": x, "lebar": y, "tinggi": z, "volume": v}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hitung", methods=["GET", "POST"])
def hitung():
    if request.method == "POST":
        try:
            panjang = float(request.form.get("panjang", 0))
            lebar   = float(request.form.get("lebar", 0))
            tinggi  = float(request.form.get("tinggi", 0))

            volume = panjang * lebar * tinggi

            riwayat.append({
                "panjang": panjang,
                "lebar": lebar,
                "tinggi": tinggi,
                "volume": volume
            })

            # setelah proses, pindah ke halaman hasil
            return redirect(url_for("hasil"))
        except ValueError:
            # kalau input tidak valid, tetap di halaman proses
            return render_template("proses.html", error="Input harus angka!")
    return render_template("proses.html")

@app.route("/hasil")
def hasil():
    return render_template("hasil.html", riwayat=riwayat)

if __name__ == "__main__":
    app.run(debug=True)
