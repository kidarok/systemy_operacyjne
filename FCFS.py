def FCFS(procesy):
    procesy_sort = sorted(procesy, key=lambda x: x.czas_przyjscia) 
    ilosc_procesow = len(procesy)
    
    czas = procesy_sort[0].czas_przyjscia
    suma_oczekiwan = 0
    for i in range (ilosc_procesow):
        if (procesy_sort[i].czas_przyjscia > czas):
            czas = procesy_sort[i].czas_przyjscia
        procesy_sort[i].start = czas
        czas = czas + procesy_sort[i].czas_trwania
        if (procesy_sort[i].start != 0):
            procesy_sort[i].czas_oczekiwania = procesy_sort[i].start - procesy_sort[i].czas_przyjscia
            
        suma_oczekiwan = suma_oczekiwan + procesy_sort[i].czas_oczekiwania
    
    sredni_czas_oczekiwania = round(suma_oczekiwan / ilosc_procesow, 3)
    print("Średni czas oczekiwania dla algorytmu FCFS:    ", sredni_czas_oczekiwania)
    return sredni_czas_oczekiwania