from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import klasa

def wygeneruj_czasy_trwania(Mu, Sigma, Size, id):
    czas_trwania = random.normal(Mu, Sigma, Size)
    plik = open("czasy_trwania" + id + ".txt", 'w')
    for i in czas_trwania:
        plik.write(str(abs(int(i)))+" ") #zapisuje modul i czesc calkowita aby pozbyc sie ujemnych
    plik.close()

def wygeneruj_czasy_przyjscia(Low, High, Size, id):
    czas_przyjscia = random.uniform(Low,High,Size)
    plik = open("czasy_przyjscia" + id + ".txt", 'w')
    for i in czas_przyjscia:
        plik.write(str(abs(int(i)))+" ") #zapisuje modul i czesc calkowita aby pozbyc sie ujemnych
    plik.close()

def wygeneruj_sekwencje(koniec_przedzialu, ilosc, id):

    plik = open("sekwencja" + id + ".txt", 'w') 
    sekwecja = random.uniform(0, koniec_przedzialu, ilosc)
    for odwolanie in sekwecja:
        plik.write(str(abs(int(odwolanie)))+" ")
    plik.close()

def pokaz_wykresy():
    plt.hist(przyjscie, 20, density=True)
    plt.title('Czasy przyjścia procesów')
    plt.ylabel('Density')
    plt.xlabel('Values')
    plt.show()

    plt.title('Czasy trwania procesów')
    plt.ylabel('Density')
    plt.xlabel('Values')
    sns.distplot(trwanie, hist=False) #tworzenie wykresu
    plt.show()


def DANE_RECZNE():
    procesy = [] #tablica ze wszystkimi procesami (tablica obiekow)
    while True: #podawanie danych
        wejscie = input("Podaj nazwe, czas przyjscia i trwania procesu:  ")
        if (wejscie == "0000"):
            break
        wejscie = wejscie.split(" ")
        procesy.append(klasa.Proces(wejscie[0], int(wejscie[1]), int(wejscie[2]))) #tworzenie tablicy obiektów
    return procesy

def DANE_Z_PLIKU(id):
    procesy = []
    plik = open("czasy_trwania" + id + ".txt", 'r')
    global trwanie
    trwanie = plik.read()
    trwanie = trwanie.strip().split(" ")
    plik.close()
    plik = open("czasy_przyjscia" + id + ".txt", 'r')
    global przyjscie
    przyjscie = plik.read()
    przyjscie = przyjscie.strip().split(" ")
    plik.close()
    for i in range(len(trwanie)):
        procesy.append(klasa.Proces("P"+str(i), int(przyjscie[i]), int(trwanie[i])))
    return procesy

def SEKWENCJA_RECZNE():
    sekwencje = []
    wejscie = input("Podaj kolejne wartosci odwolan po spacji:  ")
    sekwencje = wejscie.split(" ")
    
    return sekwencje

def SEKWENCJA_Z_PLIKU(id):
    sekwencja = []
    plik = open("sekwencja" + id + ".txt", 'r')
    wejscie = plik.read()
    sekwencja = wejscie.strip().split(" ")
    plik.close()

    return sekwencja