# L1_4_raport.py - Raporty
surowy_log = "logowanie:PASS:120;koszyk:FAIL:340;platnosc:PASS:210;wylogowanie:PASS:95;koszyk:FAIL:360;rejestracja:PASS:180"

# Część A — parsowanie (powtórka L1.2 stringi + L1.3 listy)
podzielony_log = surowy_log.split(";")          # podzielenie surowych danych (surowy_log) metodą .split używając ";" jako separatora
print(f"Lista wpisów w logu: {podzielony_log}")         # wypisanie na ekran podzielonych danych
print(f"Pozycja 1 na liście: {podzielony_log[0]}")          # wypisanie na ekran pierwszej pozycji z indeksu [0] na liście podzielony_log (pomocnicze)
pozycja_1 = podzielony_log[0].split(":")            # ponowne podzielenie danych metodą .split, tym razem tych stanowiących pierwsze miejsce [0] na liście podzielony_log używając ":" jako separatora i przypisanie do listy pozycja_1
print(f"Podzielona pozycja 1: {pozycja_1}")         # wypisanie na ekran listy po podzieleniu danych (pomocnicze)
nazwa, status, czas = pozycja_1         # rozpakowanie (unpacking) listy na zmienne
czas = int(czas)            # konwersja wartości zmiennej czas na liście pozycja_1 na integer (liczby całkowite)
print(f"Nazwa operacji: {nazwa} | Status operacji [PASS/FAIL]: {status} | Czas operacji [ms]: {czas} ms")           # wypisanie na ekran wartości zmiennych z pierwszej sekcji logu
print(f"Czas operacji + 10 ms: {czas + 10} ms")         # wypisanie na ekran operacji dodania liczby całkowitej, co weryfikuje, czy zmienna 'czas' została poprawnie skonwertowana ze string do integer

# Część B — budowa słownika (dict, nowość) - zadanie niepoprawne //
# BŁĄD: nadpisywanie słownika zamiast uzupełniania
# wyniki = set()
# wyniki = {
#     "logowanie": "PASS", "koszyk": "FAIL", "platnosc": "PASS", "wylogowanie": "PASS", "koszyk": "FAIL", "rejestracja": "PASS"           # tworzenie par 'operacja: status'. "koszyk: FAIL" znajduje się na liście dwukrotnie. Nie jestem pewien, czy powinienem go zostawić (status zostaje nadpisany - w tym przypadku nie ma to znaczenia bo jest taki sam. Czy to był by błąd danych, czy to się jakoś obsługuje?)
# }
# print(f"Czy w słowniku znajduje się klucz 'platnosc'? {'platnosc' in wyniki}")          # wypisanie na ekran wyniku boolean (True/False - w tym przypadku True) dla obecności klucza 'platnosc' w słowniku 'wyniki'
# print(f"Status testu 'nieistniejący': {wyniki.get('nieistniejacy', 'BRAK')}")           # zastosowanie bezpiecznego dostępu na słowniku 'wyniki' metodą .get() z przypisaniem domyślej wartości 'BRAK' dla nieistniejącego klucza 'nieistniejacy'
# wyniki = {
#     "srodowisko": {"nazwa": "staging", "url": "https://staging.sklep.pl"}           # dodanie zagnieżdżonych kluczy do słownika 'wyniki', w których klucz 'srodowisko' posiada klucze': 'nazwa' o wartości 'staging' i 'url' o wartości 'https://staging.sklep.pl'
# }
# print(f"Środowisko: {wyniki['srodowisko']['nazwa']}")           # wypisanie na ekran zagnieżdżonego klucza 'srodowisko' -> 'nazwa' ze słownika 'wyniki'

wyniki = {}         # utworzenie pustego słownika
wyniki = {
    "logowanie": "PASS", "koszyk": "FAIL", "platnosc": "PASS", "wylogowanie": "PASS", "koszyk": "FAIL", "rejestracja": "PASS"           # tworzenie w słowniku par: 'operacja: status'.
}
print(f"Czy w słowniku znajduje się klucz 'platnosc'? {'platnosc' in wyniki}")          # wypisanie na ekran wyniku boolean (True/False - w tym przypadku True) dla obecności klucza 'platnosc' w słowniku 'wyniki'
print(f"Status testu 'nieistniejący': {wyniki.get('nieistniejacy', 'BRAK')}")           # zastosowanie bezpiecznego dostępu na słowniku 'wyniki' metodą .get() z przypisaniem domyślej wartości 'BRAK' dla nieistniejącego klucza 'nieistniejacy'
wyniki["srodowisko"] = {
    "nazwa": "staging", "url": "https://staging.sklep.pl"           # dodanie zagnieżdżonych kluczy do słownika 'wyniki', w których klucz 'srodowisko' posiada klucze': 'nazwa' o wartości 'staging' i 'url' o wartości 'https://staging.sklep.pl'
}
print(f"Środowisko: {wyniki['srodowisko']['nazwa']}")           # wypisanie na ekran zagnieżdżonego klucza 'srodowisko' -> 'nazwa' ze słownika 'wyniki'
print(f"Sprawdzenie zawartości słownika: {wyniki}")           # wypisanie na ekran zawartości słownika 'wyniki'

# Część C — zbiory (set, nowość)
statusy = ["PASS", "FAIL", "PASS", "PASS", "FAIL", "PASS"]
unikalne_statusy = set(statusy)         # utworzenie zbioru 'unikalne_statusy' z listy 'statusy', co automatycznie powoduje usunięcie powtórzeń z listy 'statusy'
print(f"Statusy: {unikalne_statusy} | Ilość unikalnych statusów: {len(unikalne_statusy)}")          # wypisanie na ekran kluczy ze zbioru i policzenie ich metodą len()
testy_smoke = {"logowanie", "platnosc"}
testy_regresja = {"logowanie", "koszyk", "platnosc", "wylogowanie"}
print(f"Testy wspólne dla Smoke testów i testów Regresji: {testy_smoke & testy_regresja}")          # wypisanie na ekran części wspólnej używając operatora (?) '&'
print(f"Testy występujące w testach Regresji ale nie w Smoke testach: {testy_regresja - testy_smoke}")          # wypisanie na ekran części różnej używając operatora (?) '-'
print(f"Wszystkie testy występujące w testach Regresji i Smoke testach: {testy_smoke | testy_regresja}")            # wypisanie na ekran sumy używając operatora (?) '|'

# Część D — synteza (łączy wszystko)
print(f"Ilość testów o statusie PASS: {statusy.count('PASS')} | Ilość testów o statusie FAIL: {statusy.count('FAIL')}")         # wypisanie na ekran ilości testów o statusach PASS i FAILL, przy pomocy .count()
print(f"Suite Regresja: {statusy.count('PASS')} PASS | {statusy.count('FAIL')} FAIL | Środowisko: {wyniki['srodowisko']['nazwa']}")         # wypisanie na ekran ilości testów o statusach PASS i FAILL, przy pomocy .count() oraz nazwy środowiska ze zbioru 'wyniki'