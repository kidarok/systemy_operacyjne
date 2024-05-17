def FIFO(sekwecja, wielosc_ramki):
    ramki = []
    bledy = 0

    for odwolanie in sekwecja: 
        if odwolanie not in ramki: #sprawdzenie dana wartosc znajduje sie w ramce
            bledy += 1
            if (len(ramki) == wielosc_ramki):
                ramki.pop(0) #usuniecie ostatniej wartosci
            ramki.append(odwolanie) #dodanie najnowszej
    print("Ilość błęów dla algorytmu FIFO:    ", bledy, round((bledy/len(sekwecja))*100, 3), "%")
    return bledy