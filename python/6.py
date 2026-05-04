# Decision Matrix untuk Rekomendasi Program
def rekomendasi_program(usia, minat, pengalaman):
    if usia < 18:
        return "Terlalu muda untuk program ini"

    if minat == "coding":
        if pengalaman >= 2:
            return "Bootcamp Advanced Programming"
        elif pengalaman >= 1:
            return "Bootcamp Intermediate"
        else:
            return "Coding Fundamentals"

    elif minat == "data":
        if pengalaman >= 1:
            return "Data Science Bootcamp"
        else:
            return "Data Analytics Basics"

    elif minat == "design":
        return "UI/UX Design Program"

    else:
        return "Eksplorasi minat dulu ya!"


# Test dengan berbagai kombinasi
test_cases = [
    (19, "coding", 3),
    (22, "data", 0),
    (17, "coding", 1),
    (25, "design", 2),
    (20, "music", 1),
]

print("=== Hasil Rekomendasi ===")
for i, (usia, minat, exp) in enumerate(test_cases, 1):
    hasil = rekomendasi_program(usia, minat, exp)
    print(f"{i}. Usia {usia}, Minat {minat}, Exp {exp} tahun")
    print(f"   Rekomendasi: {hasil}\n")

# Coba buat fungsi sendiri di bawah ini!
