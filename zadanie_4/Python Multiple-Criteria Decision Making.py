# import wymaganych bilbiotek
import numpy as np
import pymcdm as pm
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm import normalizations as norms

#  KONTEXT BIZNESOWY: PM zarządzający produktem. Próba priorytetyzacji różnych nowych funcjonalności, które chcemy dodać do produktu.

    #  KRYTERIA: 
        # C1: Koszty rozwoju (w tys. zł) – minimalizować
        # C2: Wpływ na retencję użytkową (ocena 1-10) - maksymalizować
        # C3: Czas opracowania (w tygodniach) – minimalizować
        # C4: Potencjalny wzrost przychodu (w % wydajności) – maksymalizować

    #  ALTERNATYWY (features):
        # F1: Integracja z bankami (automatyczne pobieranie transakcji).
        # F2: AI do analizy wydatków (sugestie oszczędności).
        # F3: Moduł inwestycji (tracking portfela).
        # F4: Społecznościowe wyzwania (gamification z przyjaciółmi).

    #   Przykładowe wartości: Na podstawie szacunków PM-a.

# 1 MACIERZ DECYZYJNA (4 alternatywy x 4 kryteria)
    # 2D: wierze = alternatywy
    #     kolumny = kryteria

matrix = np.array([
[50, 8, 6, 15],     # F1
[80, 9, 10, 20],    # F2
[40, 7, 4, 10],     # F3
[60, 6, 8, 12]      # F4
])

# Wyjaśnienie: Np. F1 kosztuje 50 tys. zł, ma wpływ 8/10 na retencję, trwa 6 tygodni, daje 15% wzrostu przychodu.

print("Macierz decyzyjna: \n", matrix)

# 2 ZDEFINIOWANIE WAG

    # Wagi sumują się do 1. 
    # Przykładowe: Koszt 0.2, Wpływ 0.3, Czas 0.2, Przychód 0.3.
    # Context biznesowy: Dostosowane do PM-a: Większy nacisk na przychód i wpływ, mniejszy na koszt/czas.

# Wektor wag (ręcznie przypisanie wartości, suma = 1)

weights = np.array([0.2, 0.3, 0.2, 0.3])
print("Wagi:\n", weights)

# Wektor wag (obliczanie obiektywne metodą entropy) Alternatywa

    # System sprawdza, jak bardzo wartości w danej kolumnie różnią się od siebie: 
    # Mała zmienność = Wysoka entropia: Jeśli w danej kategorii (np. „cena produktu”) wszystkie oferty są niemal identyczne, to ta informacja ma wysoką entropię (duży nieporządek, mało konkretnej wiedzy). Taki wskaźnik nie pomaga w podjęciu decyzji, więc matematycznie jest uznawany za mało istotny.
    # Duża zmienność = Niska entropia: Jeśli ceny produktów bardzo się od siebie różnią, to ta kategoria ma niską entropię. System uznaje, że te dane niosą „dużo informacji”, ponieważ pozwalają wyraźnie odróżnić od siebie badane obiekty.

# entropy_weights = np.weights.entropy(matrix)
# print("Wagi obliczane metodą entropy: \n", entropy_weights)

# 3 ZDEFINIOWANIE TYPÓW KRYTERIÓW

    # -1 dla minimalizacji (koszt, czas), 1 dla maksymalizacji (wpływ, przychód).

# Typy kryteriów 1 = max, -1 = min
types = np.array([-1, 1, -1, 1])
print("Typy: \n", types)

# 4 ETYKIETY ALTERNATYW I KRYTERIÓW DO WYŚWIETLENIA WYNIKÓW

alternatives = ['F1: Integracja z bankami', 'F2: AI analiza', 'F3: Moduł inwestycji', 'F4: Wyzwania społecznościowe']
criteria = ['Koszt (tys. zł)', 'Wpływ na retencję (1-10)', 'Czas (tygodnie)', 'Wzrost przychodu (%)']

# 5 URUCHOMIENIE METODY TOPSIS

    # (Technique for Order Preference by Similarity to Ideal Solution)
    # oblicza odległość od idealnego i najgorszego rozwiązania.

# utworzenie obiektu TOPSIS z normalizacją 
topsis = TOPSIS(normalization_function=norms.minmax_normalization)

# oblicz preferencje (scores) dla alternatyw
topsis_scores = topsis(matrix, weights, types)
print("Scores TOPSIS:\n", topsis_scores)

# ranking: sortuj od najlepszej (najwyższy score) do najgorszej
topsis_ranking = np.argsort(-topsis_scores) + 1 #+1 dla rankingu od 1
print("Ranking TOPSIS od najlepszej: \n", topsis_ranking)

# wyświetl z etykietami dla czytelności
for rank, idx in enumerate(np.argsort(-topsis_scores), 1):
    print(f"Ranking {rank}: {alternatives[idx]} (score: {topsis_scores[idx]:.4f})")


# 6 URUCHOMIENIE METODY SPOTIS

    # SPOTIS (Stable Preference Ordering Towards Ideal Solution) to wariacja TOPSIS z punktem odniesienia.
    # Wymaga definiowania granic (bounds) dla każdego kryterium: [min, max] możliwe wartości.
    # SPOTIS używa stałych granic (bounds) dla każdego kryterium. Te bounds to minimalna i maksymalna dopuszczalna wartość dla kryterium

# Bounds dla SPOTIS: [min, max] dla każdego kryterium

bounds = np.array([
    [0, 100],   # C1: Koszt (0-100 tys. zł)
    [1, 10],    # C2: Wpływ (1-10)
    [1, 12],    # C3: Czas (1-12 tygodni)
    [5, 25]     # C4: Przychód (5-25%)
])

print("Bounds dla SPOTIS: \n", bounds)

#  import metody SPOTIS
from pymcdm.methods import SPOTIS

# utworzenie obiektu SPOTIS
spotis = SPOTIS(bounds=bounds)

# obliczanie preferencji (niższy score = lepszy w SPOTIS)
spotis_scores = spotis(matrix, weights, types)
print("Score SPOTIS: \n", spotis_scores)

# ranking: sortuj od najlepszej (najniższy score) do najgorszej
spotis_scores = np.argsort(spotis_scores) + 1
print("Ranking SPOTIS: (od najlepszej): \n", spotis_scores)

# wyświetlanie z etykietami
for rank, idx in enumerate(np.argsort(spotis_scores), 1):
    print(f"Ranking {rank}: {alternatives[idx]} (score: {spotis_scores[idx] :.4f})")

# 7 URUCHOMIENIE METODY VIKOR

    # Metoda VIKOR (skrót od serbskiego Visekriterijumska Optimizacija I Kompromisno Resenje) to technika wielokryterialnego podejmowania decyzji, której celem jest znalezienie rozwiązania kompromisowego.
    # W przeciwieństwie do prostych rankingów, VIKOR szuka balansu między „maksymalną korzyścią grupy” (ogólnym dobrem) a „minimalnym żalem indywidualnym” (najgorszym parametrem, którego boi się decydent)

# obliczanie preferencji (niższy score = lepszy w VIKOR)
vikor = VIKOR(normalization_function=norms.minmax_normalization)
vikor_scores = vikor(matrix, weights, types) 
print("Score VIKOR: \n", vikor_scores)

# ranking: sortuj od najlepszej (najniższy score) do najgorszej
vikor_ranking = np.argsort(vikor_scores) + 1
print("Ranking VIKOR: (od najlepszej): \n", vikor_scores)

# wyświetlanie z etykietami
for rank, idx in enumerate(np.argsort(vikor_scores), 1):
    print(f"Ranking {rank}: {alternatives[idx]} (score: {vikor_scores[idx] :.4f})")

# Automatyczne porównanie rankingów (korelacja Spearmana)

from scipy.stats import spearmanr  # Dla porównania


topsis_rank = np.argsort(-topsis_scores) + 1  # Konwersja scores na rank (1=best)
spotis_rank = np.argsort(spotis_scores) + 1
vikor_rank = np.argsort(vikor_scores) + 1


corr_ts, _ = spearmanr(topsis_rank, spotis_rank)
print(f"Korelacja Spearmana TOPSIS-SPOTIS: {corr_ts:.4f}")  # Blisko 1 = podobne rankingi

if 'vikor_rank' in locals():  
    corr_tv, _ = spearmanr(topsis_rank, vikor_rank)
    corr_sv, _ = spearmanr(spotis_rank, vikor_rank)
    print(f"Korelacja TOPSIS-VIKOR: {corr_tv:.4f}")
    print(f"Korelacja SPOTIS-VIKOR: {corr_sv:.4f}")


# 8 WIZUALIZAJCA RANKINGÓW (BAR CHART)

import matplotlib.pyplot as plt  # Dla wizualizacji

fig, ax = plt.subplots(figsize=(10, 6))
width = 0.25
ind = np.arange(len(alternatives))
ax.bar(ind - width, topsis_rank, width, label='TOPSIS Rank')
ax.bar(ind, spotis_rank, width, label='SPOTIS Rank')
if 'vikor_rank' in locals():
    ax.bar(ind + width, vikor_rank, width, label='VIKOR Rank')
ax.set_ylabel('Ranking (niższy = lepszy)')
ax.set_title('Porównanie Rankingów Metod MCDM')
ax.set_xticks(ind)
ax.set_xticklabels(alternatives, rotation=45, ha='right')
ax.legend()
plt.tight_layout()
plt.savefig('ranking_comparison.png')  # Zapisz do pliku dla raportu
plt.show()  


# 7 ANALIZA WYNIKÓW

import pandas as pd

# Dataframe z wynikami
results = pd.DataFrame({
    'Alternatives': alternatives,
    'TOPSIS score': topsis_scores,
    'TOPSIS rank': np.argsort(-topsis_scores) +1,
    'SPOTIS score': spotis_scores,
    'SPOTIS rank': np.argsort(spotis_scores) +1
})
print("Wyniki porównawcze: \n", results)

# zapis do CSV do raportu
results.to_csv('mcdm_results.csv', index=False)