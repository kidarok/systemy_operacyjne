def SJF(procesy):
    ilosc_procesow = len(procesy)
    gotowe = []
    aktualny_czas = 0
    suma_oczekiwan = 0
    procesy_sort = sorted(procesy, key=lambda x: x.czas_przyjscia)
    aktualny_czas = procesy_sort[0].czas_przyjscia

    i = 0
    procesy_sort = sorted(procesy, key=lambda x: x.czas_trwania) 
    while procesy_sort:
        if (procesy_sort[i].czas_przyjscia <= aktualny_czas):
            procesy_sort[i].start = aktualny_czas
            aktualny_czas = aktualny_czas + procesy_sort[i].czas_trwania
            if (procesy_sort[i].start != 0):
                procesy_sort[i].czas_oczekiwania = procesy_sort[i].start - procesy_sort[i].czas_przyjscia
            
            suma_oczekiwan += procesy_sort[i].czas_oczekiwania
            gotowe.append(procesy_sort.pop(i))
            i = 0
        else:
            i = i + 1
        if (i >= len(procesy_sort)):
            i = 0
            aktualny_czas = aktualny_czas + 1

    sredni_czas_oczekiwania = round(suma_oczekiwan / ilosc_procesow, 3)
    print("Średni czas oczekiwania dla algorytmu SJF:   ", sredni_czas_oczekiwania)
    return sredni_czas_oczekiwania