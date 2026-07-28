# L1_6a_monitor.py - monitor przebiegu testów - pętle

raport = "TC-201;PASS;1.2|TC-202;FAIL;8.5|TC-203;PASS;62.0|TC-204;SKIP;0.0|TC-205;FAIL;3.3|TC-206;PASS;120.7|TC-207;RETRY;5.0|TC-208;PASS;9.1"
wpisy = raport.split("|")

akumulator_wpisow = 0
for wpis in wpisy:
    akumulator_wpisow += 1
print(f"Liczba wpisów w raporcie liczna pętlą: {akumulator_wpisow}")
print(f"Liczba wpisów w raporcie: {len(wpisy)}")

# Część B — jedna pętla, wiele akumulatorów (L1.4, L1.5)
czasy = []
statusy = {}
powolne_testy = []
nieznane = set()
obslugiwane = {"PASS", "FAIL", "SKIP"}

for wpis in wpisy:
    pola_b = wpis.split(";")
    tc_id = pola_b[0].strip()
    status = pola_b[1].strip().upper()
    czas = float(pola_b[2].strip())

    czasy.append(czas)

    if status in statusy:
        statusy[status] += 1
    else:
        statusy[status] = 1

    if status not in obslugiwane:
        nieznane.add(status)

    if czas > 60:
        powolne_testy.append((tc_id, czas))

print(f"Czasy: {czasy}")
print(f"Statusy: {statusy}")
print(f"Nieznane statusy: {nieznane}")
print(f"Powolne testy [czas > 60 sek.]: {powolne_testy}")

# Część C — range i pozycje (L1.2, L1.3)
for i in range(len(wpisy)):
    pola_c = wpisy[i].split(";")
    tc_id = pola_c[0].strip()
    status = pola_c[1].strip().upper()
    print(f"{i} {tc_id} [{status}]")

for i in range(0, len(wpisy), 2):
    print(f"{wpisy[i]}")

# Część D — while z warunkiem (L1.5)    
i = 0
suma = 0
while suma <= 100 and i < len(wpisy):
    pola_d = wpisy[i].split(";")
    czas_d = float(pola_d[2].strip())
    suma += czas_d
    if suma > 100:
        print(f"Przekroczenie wartości 100 sek. pod indeksem: {i} | Suma: {suma}")
        break
    i += 1

# Część E — break i continue (L1.5)
akumulator_tc_id = []
for wpis in wpisy:
    pola_e = wpis.split(";")
    tc_id = pola_e[0].strip()
    status = pola_e[1].strip().upper()
    if status != "PASS":
        continue
    akumulator_tc_id.append(tc_id)
print(f"PASS: {akumulator_tc_id}")

# Część F — podsumowanie
print(f"\n--- PODSUMOWANIE ---")
print(f"Liczba wpisów w raporcie liczna pętlą: {akumulator_wpisow}")
print(f"Statusy: {statusy}")
print(f"Nieznane statusy: {nieznane}")
print(f"Powolne testy [czas > 60 sek.]: {powolne_testy}")
print(f"Suma czasów: {sum(czasy)} sek.")
print(f"Maksymalny czas: {max(czasy)} sek.")

# Część G — bonus (dla chętnych)
suma_time_pass = 0
licznik_tc_pass = 0
for wpis in wpisy:
    pola_g = wpis.split(";")
    status = pola_g[1].strip().upper()
    czas_g = float(pola_g[2].strip())
    if status == "PASS":
        licznik_tc_pass += 1
        suma_time_pass += czas_g
print(f"\n--- BONUS ---")
if licznik_tc_pass > 0:
    print(f"Średnia czasu przypadków o statusie PASS: {(suma_time_pass / licznik_tc_pass):.2f} sek.")
else:
    print(f"Brak przypadków PASS")