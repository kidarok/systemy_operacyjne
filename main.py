import generator_danych
import FCFS
import SJF
import FIFO
import LRU

suma_FCFS = 0
suma_SJF = 0
suma_FIFO = 0
suma_LRU = 0
ilosc_serii = 5
ramka = 4

for i in range(ilosc_serii):
    generator_danych.wygeneruj_czasy_trwania(60, 35, 200, str(i + 1))
    generator_danych.wygeneruj_czasy_przyjscia(0, 300, 200, str(i + 1))
    generator_danych.wygeneruj_sekwencje(15, 300, str(i + 1))

    procesy = generator_danych.DANE_Z_PLIKU(str(i + 1))
    sekwencja = generator_danych.SEKWENCJA_Z_PLIKU(str(i + 1))

    czas_fcfs = FCFS.FCFS(procesy)
    czas_sjf = SJF.SJF(procesy)
    print()
    bledy_fifo =FIFO.FIFO(sekwencja, ramka)
    bledy_lru = LRU.LRU(sekwencja, ramka)
    print()

    suma_FCFS += czas_fcfs
    suma_SJF += czas_sjf
    suma_FIFO += bledy_fifo
    suma_LRU += bledy_lru

avg_FCFS = round(suma_FCFS/ilosc_serii, 2)
avg_SJF = round(suma_SJF/ilosc_serii, 2)
avg_FIFO = suma_FIFO/ilosc_serii
avg_LRU = suma_LRU/ilosc_serii

print("Średni czas oczekiwania FCFS", avg_FCFS)
print("Średni czas oczekiwania SJF", avg_SJF)
print()
print("Średnia ilość bledow FIFO", avg_FIFO)
print("Średnia ilość bledow LRU", avg_LRU)