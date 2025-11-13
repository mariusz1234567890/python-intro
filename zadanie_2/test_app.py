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

# Import konkretnej funkcji convert_date_format z pliku o nazwie app.py, którą chcemy przetestować.
from app import convert_date_format

# Import konkretnej funkcji  is_polindrome z pliku o nazwie app.py, którą chcemy przetestować.
from app import is_polindrome


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

    def test_filter_even_numbers_parametrized(self):
        cases = [([1,2,3,4,5], [2,4]), ([],[]), ([1,3,5], [])]
        for input_list, expected in cases:
            with self.subTest(input_list=input_list):
                self.assertEqual(filter_even_numbers(input_list), expected)

# FUNKCJA KONWERTUJĄCA FORMAT DAT.

    def test_convert_date_format_typical(self):

        # Typowy przypadek: poprawna data
        self.assertEqual(convert_date_format("31-12-2025"), "2025-12-31")

    def test_convert_date_format_invalid(self):

        # Przypadek błędny: zła data
        with self.assertRaises(ValueError):
            convert_date_format("32-12-2025")
    
    def test_convert_date_format_edge(self):
    
        # Przypadek brzegowy: data z zerami
        self.assertEqual(convert_date_format("01-01-2000"), "2000-01-01")


    def test_convert_date_format_parametrized(self):
        # Lista przypadków: (data wejściowa DD-MM-RRRR, oczekiwany wynik RRRR-MM-DD)
        cases = [
            # 1. Typowe/różne daty
            ("15-06-2023", "2023-06-15"),  # Typowa data w środku miesiąca
            ("01-02-2024", "2024-02-01"),  # Pojedyncze cyfry w dniu i miesiącu
            ("31-10-2021", "2021-10-31"),  # Ostatni dzień miesiąca
            
            # 2. Miesiące krótkie (Test brzegowy miesiąca)
            ("30-04-2025", "2025-04-30"),  # Ostatni dzień kwietnia (30-dniowy miesiąc)
            ("28-02-2023", "2023-02-28"),  # Ostatni dzień lutego (zwykły rok)
            
            # 3. Rok przestępny (Kluczowy test brzegowy)
            ("29-02-2024", "2024-02-29"),  # Test, czy data z roku przestępnego (2024) jest poprawna
            
            # 4. Inne brzegi
            ("01-01-1970", "1970-01-01"),  # Data brzegowa historyczna (często używana)
            ("31-12-2099", "2099-12-31"),  # Data brzegowa przyszła
        ]

        for input_date, expected_date in cases:
            with self.subTest(input=input_date):
                self.assertEqual(convert_date_format(input_date), expected_date)

# FUNKCJA SPRAWDZAJĄCA, CZY TEKST JEST POLINDROMEM.

    def test_is_polindrome_typical(self):

        # Przypadek typowy: jest polindromem
        self.assertTrue(is_polindrome("Kobyła ma mały bok"))

        # Przypadek: nie jest polindromem
        self.assertFalse(is_polindrome("Banan"))

        # Przypadek brzegowy: brak znaku lub pojedyńczy znak
        self.assertTrue(is_polindrome(""))
        self.assertTrue(is_polindrome("a"))