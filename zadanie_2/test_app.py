# FUNKCJA SPRAWDZAJĄCA POPRAWNOŚĆ E-MAIL / E-MAIL VALIDITY CHECK FUNCTION 


# Instalacja modulu do unit testow / Instalation of module to unit tests.

import unittest
print("Moduł 'unittest' jest dostępny.")

# Zainstalowanie pytest komenda w terminalu.
    # py -m pip install pytest


# Zainstalowanie coverage komenda w terminalu.
    # py -m pip install coverage


# Import konkretnej funkcji is_valid_email z pliku o nazwie app.py, którą chcemy przetestować.
from app import is_valid_email  

# Import konkretnej funkcji calculate_triangle_area z pliku o nazwie app.py, którą chcemy przetestować.
from app import calculate_triangle_area

# Import konkretnej funkcji filter_even_numbers z pliku o nazwie app.py, którą chcemy przetestować.
from app import filter_even_numbers

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


# FUNKCJA DOKONUJĄCA PROSTYCH OBLICZEŃ MATEMATEMATYCZNYCH NP. OBLICZANIA POLA FIGURY / A FUNCTION THAT PERFORMS SIMPLE MATHEMATICAL CALCULATIONS, SUCH AS CALCULATING THE AREA OF A SHAPE.

    def test_calculate_triangle_area_typical(self):
        
        # Typowy przypadek: pozytywne wartości
        self.assertEqual(calculate_triangle_area(10.0, 5.0), 25.0) 
    
    def test_calculate_triangle_area_zero(self):

        # Przypadek brzegowy: zero jest jako podstawa lub wysokość
        self.assertEqual(calculate_triangle_area(0.0, 5.0), 0.0)

    def test_calculate_triangle_area_negative(self):

        # Błędne dane: ujemne wartości
        with self.assertRaises(ValueError):
            calculate_triangle_area(-10.0, 5.0) 

    def test_calculate_triangle_area_parametrized(self):
        cases = [(10.0, 5.0, 25.0), (0.0, 5.0, 0.0), (5.0, 0.0, 0.0)]
        for base, height, expected in cases:
            with self.subTest(base=base, height=height):
                self.assertEqual(calculate_triangle_area(base, height), expected)

# FUNKCJA PRZETWARZAJĄCA LISTĘ DANYCH (SORTOWANIE, FILTRACJA) / DATA LIST PROCESSING FUNCTION 

    def test_filter_even_numbers_typical(self):

        # Typowy przypadek: mieszana lista
        self.assertEqual(filter_even_numbers([1,2,3,4,5]), [2,4])

    def test_filter_even_numbers_empty(self):

        # Przypadek brzegowy: puste listy
        self.assertEqual(filter_even_numbers([]),[])

    def test_filter_even_numbers_all_odd(self):

        # Przypadek błędny: same nieparzyste
        self.assertEqual(filter_even_numbers([1,3,5]), [])