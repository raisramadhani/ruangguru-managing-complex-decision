# Memproses data kandidat dalam batch
daftar_kandidat = [
    {"nama": "Andi", "usia": 22, "nilai": 85, "jurusan": "IT"},
    {"nama": "Budi", "usia": 17, "nilai": 78, "jurusan": "Bisnis"},
    {"nama": "Citra", "usia": 25, "nilai": 65, "jurusan": "IT"},
    {"nama": "Dewi", "usia": 23, "nilai": 92, "jurusan": "Design"},
]

hasil_seleksi = []

for kandidat in daftar_kandidat:
    status = ""

    if kandidat["usia"] < 18:
        status = "Gagal: Usia kurang"
    elif kandidat["nilai"] < 70:
        status = "Gagal: Nilai kurang"
    elif kandidat["jurusan"] == "IT" and kandidat["nilai"] >= 80:
        status = "Lolos: IT Track"
    elif kandidat["nilai"] >= 85:
        status = "Lolos: General Track"
    else:
        status = "Waitlist"

    hasil_seleksi.append({"nama": kandidat["nama"], "status": status})

for hasil in hasil_seleksi:
    print(f"{hasil['nama']}: {hasil['status']}")
