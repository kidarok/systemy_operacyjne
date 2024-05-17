class Proces:
    def __init__(self, nazwa, czas_przyjscia, czas_trwania):
        self.nazwa = nazwa
        self.czas_przyjscia = czas_przyjscia
        self.czas_trwania = czas_trwania
        self.czas_oczekiwania = 0
        self.start = czas_przyjscia
        
    def details(self):
        print("Process: " + self.nazwa + ", przyjscie: " + str(self.czas_przyjscia) +
         ", czas trwania: " + str(self.czas_trwania) + str(self.czas_oczekiwania))
    def __repr__(self):
       return self.nazwa