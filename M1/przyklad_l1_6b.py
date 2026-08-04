raport = "TC-301;PASS;2.1|TC-302;FAIL;9.9|TC-303;PASS;75.0|TC-304;SKIP;0.0|TC-305;FAIL;61.0"
wpisy = raport.split("|")

# --- 1. Lista czasów: pętla vs comprehension ---
czasy_petla = []
for w in wpisy:
    czasy_petla.append(float(w.split(";")[2]))
czasy = [float(w.split(";")[2]) for w in wpisy]
print("z pętli:      ", czasy_petla)
print("comprehension:", czasy)

# --- 2. Filtr: tylko powolne (> 60 s) ---
powolne = [c for c in czasy if c > 60]
print("Powolne:", powolne)

# --- 3. Transformacja + filtr: ID testów FAIL ---
failed_ids = [w.split(";")[0] for w in wpisy if w.split(";")[1] == "FAIL"]
print("Faile:", failed_ids)

# --- 4. Dict comprehension: ID -> czas ---
mapa = {w.split(";")[0]: float(w.split(";")[2]) for w in wpisy}
print("Mapa:", mapa)

# --- 5. Set comprehension: jakie różne statusy występują ---
rozne = {w.split(";")[1] for w in wpisy}
print("Różne statusy:", rozne)