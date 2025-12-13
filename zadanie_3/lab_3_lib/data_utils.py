# FUNKCJA PRZETWARZAJĄCA LISTĘ DANYCH (SORTOWANIE, FILTRACJA) / DATA LIST PROCESSING FUNCTION 
#  Cel: Filtruje parzyste liczby z listy (przetwarzanie list).

def filter_even_numbers(numbers: list[int]) -> list[int]:
    
    """Filtruje parzyste liczby z listy."""
    #  Iteruje przez każdą liczbę (num) w wejściowej liście numbers.
    #  Warunek filtrowania: Sprawdza, czy reszta z dzielenia liczby num przez 2 jest równa 0. Jest to definicja liczby parzystej.
    return [num for num in numbers if num % 2 == 0]

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """    Łączy dwa słowniki.

    Args:
        dict1 (dict): Pierwszy słownik.
        dict2 (dict): Drugi słownik.

    Returns:
        dict: Połączony słownik.
    """
    return {**dict1, **dict2}