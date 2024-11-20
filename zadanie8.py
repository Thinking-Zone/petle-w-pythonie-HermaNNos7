licznik_nie = 0

while True:
    odpowiedz = input("Czy pada deszcz? (tak/nie/nie wiem): ").strip().lower()

    if odpowiedz == "tak":
        print(f"Koniec! Odpowiedziałeś 'nie' {licznik_nie} razy.")
        break
    elif odpowiedz == "nie":
        licznik_nie += 1
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Nie rozumiem tej odpowiedzi, spróbuj ponownie!")
