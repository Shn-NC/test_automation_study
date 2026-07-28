# Analizator raportu — wersja z pętlą (porównaj z L1.5!)

raport = "TC-101;PASS;0.8|TC-102;FAIL;15.2|TC-103;PASS;3.1|TC-104;SKIP;0.0"
wpisy = raport.split("|")

# Akumulatory — tworzone PRZED pętlą
statusy = {}
czasy = []
failed_id = []

# Jedna pętla zamiast czterech powtórzonych bloków
for wpis in wpisy:
    pola = wpis.split(";")
    tc_id = pola[0].strip()
    status = pola[1].strip().upper()
    czas = float(pola[2].strip())

    # 1. akumulator-lista: zbieramy czasy
    czasy.append(czas)

    # 2. akumulator-słownik: zliczamy statusy
    if status in statusy:
        statusy[status] += 1
    else:
        statusy[status] = 1

    # 3. akumulator-lista z filtrem: tylko faile
    if status == "FAIL":
        failed_id.append(tc_id)

print("Statusy:", statusy)
print("Czasy:", czasy)
print("Faile:", failed_id)
print("Suma czasów:", sum(czasy))

# range: numerujemy wpisy od 1
print("\n--- Lista numerowana ---")
for i in range(len(wpisy)):
    print(f"{i + 1}. {wpisy[i]}")
    print(status)

# while + break: znajdź pierwszy fail i zatrzymaj się
print("\n--- Szukam pierwszego faila ---")
i = 0
while i < len(wpisy):
    status = wpisy[i].split(";")[1].strip().upper()
    if status == "FAIL":
        print(f"Pierwszy fail pod indeksem {i}: {wpisy[i]}")
        break
    i += 1