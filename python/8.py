# Memecah decision logic menjadi fungsi-fungsi kecil
def check_age_eligibility(age):
    if age < 16:
        return False, "Terlalu muda"
    elif age > 35:
        return False, "Program untuk usia produktif"
    else:
        return True, "Usia sesuai"


def check_academic_requirements(education, gpa):
    if education == "SMA" and gpa >= 7.5:
        return True, "Memenuhi syarat akademik"
    elif education == "S1" and gpa >= 3.0:
        return True, "Memenuhi syarat akademik"
    else:
        return False, "Syarat akademik belum terpenuhi"


def check_technical_readiness(coding_exp, laptop_specs):
    if coding_exp >= 1 and laptop_specs == "high":
        return True, "Siap untuk program advanced"
    elif coding_exp >= 1 or laptop_specs == "medium":
        return True, "Siap untuk program basic"
    else:
        return False, "Perlu persiapan teknis"


def evaluate_candidate(name, age, education, gpa, coding_exp, laptop):
    print(f"\n=== Evaluasi Kandidat: {name} ===")

    # Check setiap kriteria
    age_ok, age_msg = check_age_eligibility(age)
    academic_ok, academic_msg = check_academic_requirements(education, gpa)
    tech_ok, tech_msg = check_technical_readiness(coding_exp, laptop)

    print(f"Usia: {age_msg}")
    print(f"Akademik: {academic_msg}")
    print(f"Teknis: {tech_msg}")

    # Final decision
    if age_ok and academic_ok and tech_ok:
        return "DITERIMA - Semua syarat terpenuhi"
    else:
        return "BELUM DITERIMA - Ada syarat yang belum terpenuhi"


# Test dengan data kandidat
result = evaluate_candidate("Alex", 22, "S1", 3.2, 2, "high")
print(f"Hasil: {result}")

result2 = evaluate_candidate("Budi", 17, "SMA", 8.0, 0, "low")
print(f"Hasil: {result2}")
