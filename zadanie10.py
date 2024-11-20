# Pętla, która przechodzi przez liczby od 1 do 50
for liczba in range(1, 51):
    if liczba % 2 == 0 and liczba % 4 == 0:
        print(liczba, end=",")  
