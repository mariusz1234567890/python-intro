# Instalacja modulu do unit testow / Instalation of module to unit tests.

try:
    import unittest
    print("Moduł 'unittest' jest dostępny.")
except ImportError:
    print("Moduł 'unittest' nie jest dostępny.")

# Zainstalowanie pytest komenda w terminalu.
    # py -m pip install pytest


# Zainstalowanie coverage komenda w terminalu.
    # py -m pip install coverage


# Import konkretnej funkcji is_valid_email z pliku o nazwie app.py, którą chcemy przetestować.
from app import is_valid_email  

# To jest definicja klasy testowej. Musi dziedziczyć po klasie unittest.TestCase. Klasa testowa gromadzi zestaw powiązanych testów.
# W Pythonie klasa jest szablonem (planem, przepisem), na podstawie którego tworzy się obiekty (konkretne instancje). Umożliwia grupowanie danych (atrybutów) i funkcji (metod) w jedną spójną jednostkę.
class TestApp(unittest.TestCase):
    
    # To jest pojedynczy test (Metoda (funkcja wewnątrz klasy)). Nazwa musi zaczynać się od test_. Sprawdza, czy funkcja poprawnie rozpoznaje poprawny email.
    # self odnosi się do konkretnej instancji obiektu.
    def test_is_valid_email_valid(self):

        # Typowy przypadek: poprawny email
        # Asercja – mechanizm sprawdzający. Tutaj: oczekujemy, że wywołanie funkcji z poprawnym emailem zwróci wartość True. Jeśli nie, test zawiedzie.
        self.assertTrue(is_valid_email("example@test.com"))

    def test_is_valid_email_invalid(self):
        # Przypadek braku @.
        # Oczekujemy, że funkcja zwróci False.
        self.assertFalse(is_valid_email("exampletest.com"))

    def test_is_valid_email_edge(self):
        # Przypadek brzegowy(edge).
        # Błędne dane: pusty string.
        # Oczekujemy, że funkcja zwróci False.
        self.assertFalse(is_valid_email("")) 





