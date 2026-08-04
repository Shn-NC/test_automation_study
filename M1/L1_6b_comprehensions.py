# L1_6b_comprehensions.py - Comprehensions

# Część A — dane
print(f"--- CZĘŚĆ A ---")
print(f">> Punkt 1\n(nie wyświetlany na ekranie)")
raport = "TC-401;PASS;3.0|TC-402;FAIL;12.0|TC-403;PASS;88.5|TC-404;SKIP;0.0|TC-405;FAIL;5.5|TC-406;PASS;150.0|TC-407;RETRY;7.0|TC-408;PASS;4.2"
wpisy = raport.split("|")

# Część B — list comprehension od podstaw (L1.1, L1.2)
print(f"\n--- CZĘŚĆ B ---")
wszystkie_id = []
for wpis_a in wpisy:
    pola_a = wpis_a.split(";")
    tc_id_a = pola_a[0].strip()
    wszystkie_id.append(tc_id_a)

wszystkie_id_comp = [wpis_b.split(";")[0] for wpis_b in wpisy]

print(f">> Punkt 2\nWszystkie TC ID (pętla z akumulatorem): {wszystkie_id}")
print(f"Wszystkie TC ID (comprehension): {wszystkie_id_comp}")

czasy = [float(wpis_b.split(";")[2]) for wpis_b in wpisy]
print(f"\n>> Punkt 3\nCzasy: {czasy}")

statusy_male = [wpis_b.split(";")[1].lower() for wpis_b in wpisy]
print(f"\n>> Punkt 4\nStatusy (małe): {statusy_male}")

# Część C — comprehension z filtrem (L1.5)
print(f"\n--- CZĘŚĆ C ---")
failed_ids = [wpis_c.split(";")[0] for wpis_c in wpisy if wpis_c.split(";")[1] == "FAIL"]
print(f">> Punkt 5\nTC o statusie FAIL: {failed_ids}")

szybkie = [float(wpis_c.split(";")[2]) for wpis_c in wpisy if float(wpis_c.split(";")[2]) < 10]
print(f"\n>> Punkt 6\nCzasy mniejsze niż 10 sekund: {szybkie}")

dlugie_id = [wpis_c.split(";")[0] for wpis_c in wpisy if float(wpis_c.split(";")[2]) > 60]
print(f"\n>> Punkt 7\nID testów z czasem większym niż 60 sekund: {dlugie_id}")

# Część D — dict i set comprehension (L1.4)
print(f"\n--- CZĘŚĆ D ---")
id_na_status = {wpis_d.split(";")[0]: wpis_d.split(";")[1].upper() for wpis_d in wpisy}
print(f">> Punkt 8\nID testów wraz z ich statusem (słownik): {id_na_status}")

wystepujace_statusy = {wpis_d.split(";")[1] for wpis_d in wpisy}
print(f"\n>> Punkt 9\nWystępujące statusy: {wystepujace_statusy}")

obslugiwane = {"PASS", "FAIL", "SKIP"}
nieobslugiwane = {wpis_d.split(";")[1] for wpis_d in wpisy if wpis_d.split(";")[1] not in {"PASS", "FAIL", "SKIP"}}
print(f"\n>> Punkt 10\nNieobsługiwane statusy: {nieobslugiwane}")

nieobslugiwane_alt = wystepujace_statusy - obslugiwane
print(f"Nieobsługiwane statusy (alternatywna metoda): {nieobslugiwane_alt}")

# Część E — łączenie z tym, co znasz (L1.5, L1.6a)
print(f"\n--- CZĘŚĆ E ---")
if len(czasy) > 0:
    sredni_czas = sum(czasy) / len(czasy)
    print(f">> Punkt 11\nŚredni czas: {sredni_czas}")
else:
    print(f">> Punkt 11\nIlość czasów wynosi 0. Brak możliwości obliczenia średniej.")

passed_ids = [wpis_e.split(";")[0] for wpis_e in wpisy if wpis_e.split(";")[1] == "PASS"]
print(f"\n>> Punkt 12\nIlość TC ze statusem PASS (comprehension): {len(passed_ids)}")

akumulator_tc_id = []
for wpis in wpisy:
    pola_e = wpis.split(";")
    tc_id_e = pola_e[0].strip()
    status_e = pola_e[1].strip().upper()
    if status_e != "PASS":
        continue
    akumulator_tc_id.append(tc_id_e)
print(f"Ilość TC ze statusem PASS (pętla): {len(akumulator_tc_id)}")

# Część F — bonus (dla chętnych)
print(f"\n--- CZĘŚĆ F ---")

lista_krotek = [(wpis_f.split(";")[0], float(wpis_f.split(";")[2])) for wpis_f in wpisy if float(wpis_f.split(";")[2]) > 60]
print(f">> Punkt 13\nLista ID & czas: {lista_krotek}")

print(f"\n>> Punkt 14\n(nie wyświetlany na ekranie)")
# Szczerze mówiąc comprehensions pisze mi się znacznie łatwiej niż pętle w poprzednich lekcjach. Być może dlatego, że wszystko jest w jednym miejscu i nie musze pilnować gdzie jakie i jak definiować elementy oraz głowić się nad składnią i wszystkimi zasadami, które ją określają. Trafiłem oczywiście na problemy ale główna koncepcja wydaje mi się znacznie prostsza, więc trudno mi ocenić, który z napisanych przeze mnie comprehensions jest czytelniejszy jako pętla. Tak jak napisałeś na początku lekcji, gdyby zadania były bardziej złożone (np. zagnieżdżone pętle, albo bardzo długa definicja zmiennej), to rozważył bym rozbicie comprehension na mniejsze, widoczne elementy. Faktyczny problem może się objawić gdy będę musiał czytać comprehensions (a nie je pisać), bo może mi być trudno zdekodować co jest w środku.