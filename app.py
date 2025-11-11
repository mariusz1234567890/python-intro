# FUNKCJA SPRAWDZAJĄCA POPRAWNOŚĆ E-MAIL / THE FUNCTION OF CHECKING VALIDITY OF EMAIL 

# ! Metodolodia TDD: test najpierw -> potem kod minimalny -> refaktoryzacja / Metodology of TDD: first test -> minimal code -> refactor of code



# Wczytuje  `moduł Pythona o nazwie re (skrót od Regular Expressions).
    #  Moduł ten zawiera funkcje do pracy z wyrażeniami regularnymi, które są niezbędne do zaawansowanego przeszukiwania i dopasowywania wzorców w tekście.
import re


#  Definicja funkcji Regex na email

def is_valid_email(email):
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














# Funkcja dokonująca prostych obliczeń matematycznych (np. obliczanie pola figury).

# Funkcja przetwarzająca listę danych (np. filtracja, sortowanie).

# Funkcja konwertująca format dat.

# Funkcja sprawdzająca, czy tekst jest palindromem.
