import math  # impor modul math untuk sqrt dan factorial

a = 25  # titik pusat deret
x = 26  # titik yang dihampiri (bisa diganti)
h = x - a  # selisih x dan pusat
nilai_asli = math.sqrt(x)  # nilai pembanding dari math
hampiran = 0  # penampung jumlah suku deret
for k in range(5):  # orde k = 0 sampai 4
    koef = 1  # awal perkalian turunan ke-k dari akar
    for j in range(k):  # bentuk (1/2)(1/2-1)...(1/2-k+1)
        koef *= (0.5 - j)  # kalikan faktor pangkat turun
    turunan = koef * a ** (0.5 - k)  # nilai f^(k)(a)
    suku = turunan / math.factorial(k) * h ** k  # suku ke-k deret Taylor
    hampiran += suku  # tambahkan suku ke hampiran
    galat = abs(hampiran - nilai_asli)  # galat absolut orde ini
    print(f"P{k}({x}) = {hampiran:.8f}, galat = {galat:.2e}")  # cetak hasil
    if galat < 1e-6:  # cek syarat galat < 10^-6
        print(f"Orde minimal: {k}")  # cetak orde pertama yang memenuhi
        break  # berhenti di orde minimal