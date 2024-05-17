def LRU(sekwecja, wielosc_ramki):
    bledy = 0
    ramki = []
    for odwolanie in sekwecja: 
        if odwolanie not in ramki: #sprawdzenie dana wartosc znajduje sie w ramce
            bledy += 1
            if (wielosc_ramki == len(ramki)):
                ramki.pop(0) #usuniecie ostatniej wartosci
            ramki.append(odwolanie) #dodanie najnowszej
        else:
            ramki.remove(odwolanie)
            ramki.append(odwolanie)
    print("Ilość błęów dla algorytmu LRU:    ", bledy, round((bledy/len(sekwecja))*100, 3), "%")
    return bledy