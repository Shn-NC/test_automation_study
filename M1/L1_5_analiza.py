# L1_5_analiza.py - analizator wyników

# Część A — dane i przygotowanie (L1.1, L1.2, L1.3)
raport = "TC-101;PASS;0.8|TC-102;FAIL;15.2|TC-103;PASS;3.1|TC-104;SKIP;0.0|TC-105;FAIL;72.5|TC-106;PASS;9.9|TC-107;BLOCKED;2.0"
wpisy = raport.split("|")
print(f"Liczba wpisów w raporcie: {len(wpisy)}")
czasy = []
failed_id = []
statusy = {}
nieznane_statusy = set()

# Część B — pętla ręczna, bez for (L1.3 + L1.5)
# Zastosowałem if do weryfikacji czy dana z czasem jest liczbą zmiennoprzecinkową i jeśli jest (True), nadaję jej type float w nowej zmiennej
wpis_0 = wpisy[0].split(";")
tc_id_0 = wpis_0[0].strip()
status_0 = wpis_0[1].strip().upper()
czas_txt_0 = wpis_0[2].strip()
if czas_txt_0.replace(".", "", 1).isdigit():
    czas_0 = float(czas_txt_0)
# Wyświetlenie na ekranie wyłączone - użyłem podczas sprawdzania działania kodu
# print(f"Zmienne pod indeksem 0: ID: {tc_id_0} | Status: {status_0} | Czas: {czas_0}s")

wpis_1 = wpisy[1].split(";")
tc_id_1 = wpis_1[0].strip()
status_1 = wpis_1[1].strip().upper()
czas_txt_1 = wpis_1[2].strip()
if czas_txt_1.replace(".", "", 1).isdigit():
    czas_1 = float(czas_txt_1)
# Wyświetlenie na ekranie wyłączone - użyłem podczas sprawdzania działania kodu
# print(f"Zmienne pod indeksem 1: ID: {tc_id_1} | Status: {status_1} | Czas: {czas_1}s")

wpis_2 = wpisy[2].split(";")
tc_id_2 = wpis_2[0].strip()
status_2 = wpis_2[1].strip().upper()
czas_txt_2 = wpis_2[2].strip()
if czas_txt_2.replace(".", "", 1).isdigit():
    czas_2 = float(czas_txt_2)
# Wyświetlenie na ekranie wyłączone - użyłem podczas sprawdzania działania kodu
# print(f"Zmienne pod indeksem 2: ID: {tc_id_2} | Status: {status_2} | Czas: {czas_2}s")

# Część C — klasyfikacja i decyzje (L1.5)
if status_2 == "FAIL" and czas_2 >= 60:
    priorytet = "KRYTYCZNY"
elif status_2 == "FAIL":
    priorytet = "WYSOKI"
elif status_2 == "BLOCKED":
    priorytet = "SREDNI"
elif status_2 == "SKIP":
    priorytet = "NISKI"
else:
    priorytet = "BRAK"
print(f"Priorytet: {priorytet}")

# modyfikacja status_2 na "FAIL" i czas_2 na 80.0 zgodnie z zadaniem
status_2 = "FAIL"
czas_2 = 80.0
if status_2 == "FAIL" and czas_2 >= 60:
    priorytet = "KRYTYCZNY"
elif status_2 == "FAIL":
    priorytet = "WYSOKI"
elif status_2 == "BLOCKED":
    priorytet = "SREDNI"
elif status_2 == "SKIP":
    priorytet = "NISKI"
else:
    priorytet = "BRAK"
print(f"Priorytet: {priorytet}")  # Nowa wartość dla 'priorytet' po zaktualizowaniu zmiennych 'status_2' i 'czas_2'

# przywrócenie poprzednich wartości status_2 i czas_2, zgodnie z zadaniem
status_2 = wpis_2[1].strip().upper()
czas_2 = float(czas_txt_2)

# Część D — agregacja (L1.4 + L1.5)
wpis_3 = wpisy[3].split(";")
wpis_4 = wpisy[4].split(";")
wpis_5 = wpisy[5].split(";")
wpis_6 = wpisy[6].split(";")
tc_id_3 = wpis_3[0].strip()
tc_id_4 = wpis_4[0].strip()
tc_id_5 = wpis_5[0].strip()
tc_id_6 = wpis_6[0].strip()
status_3 = wpis_3[1].strip().upper()
status_4 = wpis_4[1].strip().upper()
status_5 = wpis_5[1].strip().upper()
status_6 = wpis_6[1].strip().upper()
czas_txt_3 = wpis_3[2].strip()
if czas_txt_3.replace(".", "", 1).isdigit():
    czas_3 = float(czas_txt_3)
czas_txt_4 = wpis_4[2].strip()
if czas_txt_4.replace(".", "", 1).isdigit():
    czas_4 = float(czas_txt_4)
czas_txt_5 = wpis_5[2].strip()
if czas_txt_5.replace(".", "", 1).isdigit():
    czas_5 = float(czas_txt_5)
czas_txt_6 = wpis_6[2].strip()
if czas_txt_6.replace(".", "", 1).isdigit():
    czas_6 = float(czas_txt_6)
czasy = [czas_0, czas_1, czas_2, czas_3, czas_4, czas_5, czas_6]
print(f"Czasy [s]: {czasy}")  # Sprawdzenie czy czasy poszczególnych wpisów poprawnie dodały się do listy 'czasy'

if status_0 in statusy:
    statusy[status_0] = statusy[status_0] + 1
else:
    statusy[status_0] = 1
if status_1 in statusy:
    statusy[status_1] = statusy[status_1] + 1
else:
    statusy[status_1] = 1
if status_2 in statusy:
    statusy[status_2] = statusy[status_2] + 1
else:
    statusy[status_2] = 1
if status_3 in statusy:
    statusy[status_3] = statusy[status_3] + 1
else:
    statusy[status_3] = 1
if status_4 in statusy:
    statusy[status_4] = statusy[status_4] + 1
else:
    statusy[status_4] = 1
if status_5 in statusy:
    statusy[status_5] = statusy[status_5] + 1
else:
    statusy[status_5] = 1
if status_6 in statusy:
    statusy[status_6] = statusy[status_6] + 1
else:
    statusy[status_6] = 1
print(f"Statusy: {statusy}")  # Sprawdzenie czy statusy poszczególnych wpisów poprawnie dodały się do słownika 'statusy'

if status_0 == "FAIL":
    failed_id.append(tc_id_0)
if status_1 == "FAIL":
    failed_id.append(tc_id_1)
if status_2 == "FAIL":
    failed_id.append(tc_id_2)
if status_3 == "FAIL":
    failed_id.append(tc_id_3)
if status_4 == "FAIL":
    failed_id.append(tc_id_4)
if status_5 == "FAIL":
    failed_id.append(tc_id_5)
if status_6 == "FAIL":
    failed_id.append(tc_id_6)
print(f"Failed TC_ID: {failed_id}")  # Sprawdzenie czy statusy równe "FAIL" dla poszczególnych wpisów poprawnie dodały się do listy 'failed_id'

obslugiwane = {"PASS", "FAIL", "SKIP"}
if status_0 not in obslugiwane:
    nieznane_statusy.add(status_0)
if status_1 not in obslugiwane:
    nieznane_statusy.add(status_1)
if status_2 not in obslugiwane:
    nieznane_statusy.add(status_2)
if status_3 not in obslugiwane:
    nieznane_statusy.add(status_3)
if status_4 not in obslugiwane:
    nieznane_statusy.add(status_4)
if status_5 not in obslugiwane:
    nieznane_statusy.add(status_5)
if status_6 not in obslugiwane:
    nieznane_statusy.add(status_6)
# Wyświetlenie na ekranie wyłączone - użyłem podczas sprawdzania działania kodu
# print(f"Nieznane statusy: {nieznane_statusy}")

# Wyświetlenie na ekranie wyłączone - użyłem podczas sprawdzania działania kodu
# print(f"Suma czasów [s]: {sum(czasy)}")

print(f"Maksymalny zmierzony czas [s]: {max(czasy)}")

# Część E — decyzja o buildzie (L1.5, truthiness, ternary)
liczba_fail = len(failed_id)
# Wyświetlenie na ekranie wyłączone - użyłem podczas sprawdzania działania kodu i porównania z wynikiem użycia innego mechanizmu
# print(f"Liczba faili: {liczba_fail}")
if liczba_fail >= 2 or nieznane_statusy:
    build_status_0 = "RED"
elif liczba_fail == 1:
    build_status_0 = "YELLOW"
else:
    build_status_0 = "GREEN"
# Wyświetlenie na ekranie wyłączone - użyłem podczas sprawdzania działania kodu i porównania z wynikiem użycia innego mechanizmu
# print(f"Build status: {build_status_0}")

# Tutaj zbudowałem to samo co powyżej (przedstawia takie same wyniki), ale przy użyciu Tenerary (chciałem sprawdzić, czy się da)
build_status_1 = "RED" if liczba_fail >= 2 or nieznane_statusy else "YELLOW" if liczba_fail == 1 else "GREEN"
# Wyświetlenie na ekranie wyłączone - użyłem podczas sprawdzania działania kodu i porównania z wynikiem użycia innego mechanizmu
# print(f"Build status: {build_status_1}")

czy_dlugi_run = "TAK" if sum(czasy) > 100 else "NIE"
liczba_testow = sum(statusy.values())
liczba_testow = int(liczba_testow)

print(f"=== PODSUMOWANIE RUNU ===")
print(f"Build: {build_status_0}")
print(f"Testów: {liczba_testow} | FAIL: {liczba_fail} | Nieznane statusy: {nieznane_statusy}")
print(f"Łączny czas: {sum(czasy)} | Długi run: {czy_dlugi_run}")

# Część F — bonus (dla chętnych)
sredni_czas_testu = sum(czasy) / liczba_testow
czy_w_przedziale = "TAK" if sredni_czas_testu >= 5.0 and sredni_czas_testu <= 20.0 else "NIE"
print(f"Czy średni czas testu mieści się w przedziale [5.0 - 20.0]? {czy_w_przedziale} ({sredni_czas_testu:.2f})")
print(f"Czy różnica pomiędzy 'sum(czasy)' a wartością policzoną z dokładnością do jednego miejsca po przecinku (103.5) jest znimomo mała: {abs(sum(czasy) - 103.5) < 1e-9}")