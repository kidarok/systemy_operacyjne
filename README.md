# Symulacja Algorytmów Planowania Czasu Procesora i Zastępowania Stron

## Opis projektu

Projekt ten implementuje i testuje cztery algorytmy planowania czasu procesora oraz dwa algorytmy zastępowania stron w pamięci. Symulacja została wykonana w języku Python z wykorzystaniem bibliotek takich jak NumPy, Matplotlib i Seaborn.

## Cel projektu

Głównym celem projektu była implementacja następujących algorytmów:

### Algorytmy Planowania Czasu Procesora:
- **FCFS (First Come First Serve)**
- **SJF (Shortest Job First)**

### Algorytmy Zastępowania Stron:
- **FIFO (First In First Out)**
- **LRU (Least Recently Used)**

Dodatkowo, celem było przetestowanie tych algorytmów na różnych zestawach danych oraz analiza wyników.

## Struktura projektu

Projekt jest podzielony na moduły, z których każdy odpowiada za określoną funkcjonalność:

- `klasa.py`: Definiuje klasę `Proces` reprezentującą pojedynczy proces.
- `generator_danych.py`: Generuje czasy przyjścia, czasy trwania procesów oraz sekwencje dostępu do pamięci.
- `FCFS.py`: Implementacja algorytmu FCFS.
- `SJF.py`: Implementacja algorytmu SJF.
- `FIFO.py`: Implementacja algorytmu FIFO.
- `LRU.py`: Implementacja algorytmu LRU.
- `main.py`: Główny plik do uruchamiania symulacji i testowania algorytmów.
