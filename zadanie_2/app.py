# FUNKCJA SPRAWDZAJĄCA POPRAWNOŚĆ E-MAIL / E-MAIL VALIDITY CHECK FUNCTION 

# ! Metodolodia TDD: test najpierw -> potem kod minimalny -> refaktoryzacja 
# ! Methodology of TDD: first test -> minimal code -> refactor of code



# Wczytuje  `moduł Pythona o nazwie re (skrót od Regular Expressions).
    #  Moduł ten zawiera funkcje do pracy z wyrażeniami regularnymi, które są niezbędne do zaawansowanego przeszukiwania i dopasowywania wzorców w tekście.
import re


#  Definicja funkcji Regex na email

def is_valid_email(email):

    """Sprawdzanie poprawności napisania e-mail."""
    if email == "" or email is None:
        return False 
   
    # Definicja Wzorca (Wyrażenia Regularnego, Regex)
        # ^	            Początek Ciągu      	        Wymaga, aby dopasowanie rozpoczęło się na początku e-maila.
        # [\w\.-]+	    Nazwa Użytkownika (przed @) 	[...] – dowolny znak z podanego zestawu. \w –         litery, cyfry lub podkreślenie. . – kropka. - – myślnik. + – jeden lub więcej takich znaków.
        # @	            Znak Separatora             	Oczekiwany dosłowny znak małpy, oddzielający nazwę użytkownika od domeny.
        # [\w\.-]+	    Nazwa Domeny (po @)	            Podobne zasady jak dla nazwy użytkownika (np. google w google.com). Wymagane jest jeden lub więcej takich znaków.
        # \.	        Kropka Domeny	                Dosłowny znak kropki. Musi być poprzedzony znakiem ucieczki (\), ponieważ sama kropka w regexie ma specjalne znaczenie (dowolny znak).
        # \w+	        Rozszerzenie Domeny (TLD)	    Jeden lub więcej znaków (litery, cyfry, podkreślenie) na końcu (np. com, pl, net).
        # $	            Koniec Ciągu	                Wymaga, aby dopasowanie zakończyło się na końcu e-maila.
        
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # re.match(pattern, email)	- Dopasowanie Wzorca	
        # Wywołuje funkcję match z modułu re. 
        # Próbuje dopasować pattern do początku ciągu znaków email. 
        # Jeśli dopasowanie się powiedzie, zwraca obiekt MatchObject (wartość "prawdziwą"); 
        # w przeciwnym razie zwraca None (wartość "fałszywą").
    
    # return bool(...)  - Konwersja na Wartość Logiczną
        # Wynik funkcji re.match jest konwertowany na wartość logiczną: *
        # Jeśli zwrócono MatchObject, bool() zmieni go na True (e-mail jest poprawny). 
        # * Jeśli zwrócono None, bool() zmieni go na False (e-mail jest niepoprawny).

    return bool(re.match(pattern, email))





# FUNKCJA DOKONUJĄCA PROSTYCH OBLICZEŃ MATEMATEMATYCZNYCH NP. OBLICZANIA POLA FIGURY / A FUNCTION THAT PERFORMS SIMPLE MATHEMATICAL CALCULATIONS, SUCH AS CALCULATING THE AREA OF A SHAPE.
#  Cel: Oblicza pole trójkąta (wzór: (base * height) / 2). Proste obliczenia matematyczne.


def calculate_triangle_area(base: float, height: float) -> float:

    """Oblicza pole trójkąta. Rzuca ValueError dla ujemnych wartości."""
    if base < 0 or height < 0:
        raise ValueError("Poddstawa i wysokość nie mogą być ujmene, ale o wartości zero")
    return (base * height) / 2


# FUNKCJA PRZETWARZAJĄCA LISTĘ DANYCH (SORTOWANIE, FILTRACJA) / DATA LIST PROCESSING FUNCTION 
#  Cel: Filtruje parzyste liczby z listy (przetwarzanie list).

def filter_even_numbers(numbers: list[int]) -> list[int]:
    
    """Filtruje parzyste liczby z listy."""
    #  Iteruje przez każdą liczbę (num) w wejściowej liście numbers.
    #  Warunek filtrowania: Sprawdza, czy reszta z dzielenia liczby num przez 2 jest równa 0. Jest to definicja liczby parzystej.
    return [nun for nun in numbers if nun % 2 == 0]

# FUNKCJA KONWERTUJĄCA FORMAT DAT
# Cel: Konwertuje datę z 'DD-MM-YYYY' na 'YYYY-MM-DD'.

from datetime import datetime
def convert_date_format(date_str):
    try:
        dt = datetime.strptime(date_str, "%d-%m-%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Niepoprawny wejściowy format daty, oczekiwany jest DD-MM-YYYY")

# FUNKCJA SPRAWDZAJĄCA, CZY TEKST JEST PALINDROMEM.
# Cel: Sprawdza palindrom (ignoruj spacje, wielkość liter).

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]