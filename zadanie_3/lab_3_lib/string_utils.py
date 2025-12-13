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




# FUNKCJA SPRAWDZAJĄCA, CZY TEKST JEST PALINDROMEM.
# Cel: Sprawdza palindrom (ignoruj spacje, wielkość liter).

def is_palindrome(text):
    """Sprawdza, czy ciąg znaków jest palindromem, ignorując spacje i wielkość liter."""
    
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    # Usunięto pustą linię, która była liczna jako 'missing'
    # Porównanie tekstu z jego odwróconą wersją
    return cleaned_text == cleaned_text[::-1]


# FUNKCJA LICZĄCĄ SŁOWA W TEKŚCIE
"""
    Liczy słowa w tekście.
    Args:        text (str): Tekst do analizy.

    Returns:     int: Liczba słów.
    """
def count_words(text: str) -> int:
    return len(text.split())