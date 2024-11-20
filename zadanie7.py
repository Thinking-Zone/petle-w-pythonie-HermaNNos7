import random


czy_pada = random.choice([True, False])


while True:
    
    odpowiedz = input("Czy pada deszcz? (tak/nie): ").strip().lower()

    
    if odpowiedz == "tak" and czy_pada:
        print("Brawo! Zgadłeś, pada deszcz.")
        break
    elif odpowiedz == "nie" and not czy_pada:
        print("Brawo! Zgadłeś, nie pada deszcz.")
        break
    else:
        print("Nie zgadłeś, spróbuj ponownie!")
