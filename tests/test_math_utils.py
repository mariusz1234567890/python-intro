# Instalacja modulu do unit testow / Instalation of module to unit tests.

import unittest
print("Moduł 'unittest' jest dostępny.")

# Zainstalowanie pytest komenda w terminalu.
    # py -m pip install pytest


# Zainstalowanie coverage komenda w terminalu.
    # py -m pip install coverage


import math
print("Moduł 'math' jest dostępny.")

# Import konkretnej funkcji calculate_triangle_area z pliku o nazwie app.py, którą chcemy przetestować.
from lab_3_lib.math_utils import calculate_triangle_area

# Import konkretnej funkcji convert_date_format z pliku o nazwie app.py, którą chcemy przetestować.
from math_utils import convert_date_format



# To jest definicja klasy testowej. Musi dziedziczyć po klasie unittest.TestCase. Klasa testowa gromadzi zestaw powiązanych testów.
# W Pythonie klasa jest szablonem (planem, przepisem), na podstawie którego tworzy się obiekty (konkretne instancje). Umożliwia grupowanie danych (atrybutów) i funkcji (metod) w jedną spójną jednostkę.
class TestApp(unittest.TestCase):

    def setUp(self):
        # Służy do przygotowania wspólnych danych lub środowiska, które mogą być używane w wielu testach.w
        # To unika powtórzeń (np. zamiast pisać "example@test.com" w każdym teście, definiujesz to raz w setUp i odwołujesz się przez self.).
        # Co to jest?  setUp(self)
            #  to specjalna metoda w klasie dziedziczącej po unittest.TestCase. 
            # Uruchamia się automatycznie przed każdym pojedynczym testem (np. przed test_is_valid_email_valid). 
            # Możesz w niej przygotować dane, obiekty, pliki lub środowisko (np. zmienne, listy, słowniki), które będą używane w testach. 
            # Po teście wszystko jest czyszczone poprzez użycie tearDown()


        self.test_data = {
        # Dla calculate_triangle_area
            'typical_base': 10.0,                     # Typowa podstawa (pozytywna)
            'typical_height': 5.0,                    # Typowa wysokość (pozytywna)
            'typical_expected': 25.0,                 # Oczekiwany wynik dla typowego
            'zero_base': 0.0,                         # Brzegowy: zero jako podstawa
            'zero_height': 0.0,                       # Brzegowy: zero jako wysokość
            'zero_expected': 0.0,                     # Oczekiwany wynik dla zera
            'negative_base': -10.0,                   # Błędny: ujemna wartość (dla ValueError)

            # Dla convert_date_format
            'valid_date_typical': '31-12-2023',              # Typowy: koniec roku
            'valid_date_typical_expected': '2023-12-31',     # Oczekiwany wynik dla typowego
            'valid_date_edge_zero': '01-01-2000',            # Brzegowy: data z zerami
            'valid_date_edge_zero_expected': '2000-01-01',   # Oczekiwany wynik
            'valid_date_leap': '29-02-2024',                 # Brzegowy: rok przestępny
            'valid_date_leap_expected': '2024-02-29',        # Oczekiwany wynik
            'valid_date_current': '14-11-2025',              # Dodatkowy: bieżąca data z kontekstu (w gotowości)
            'valid_date_current_expected': '2025-11-14',     # Oczekiwany wynik
            'invalid_date_day': '32-12-2023',                # Błędny: nieprawidłowy dzień
            'invalid_date_non_leap': '29-02-2023',           # Błędny: nieprzestępny rok
            'invalid_date_format': 'abc-def-ghi',            # Błędny: całkowicie zły format


            #  Dla calculate_square_root
            'typical_input': 16.0,                          # Typowy
            'typical_expected': 4.0,

            'edge_zero_input': 0.0,                          # Brzegowy
            'edge_zero_expected': 0.0,
            
            'large_input': 10000.0,                         # Duża liczba
            'large_expected': 100.0,
            
            'float_input': 2.25,                             # Przecinkowy
            'float_expected': 1.5,

            'negative_input': -4.0,                         # Błędny (ujemna liczba)
            'negative_expected_error_message': "Liczba musi być nieujemna."

            }
        
        # Czyszczenie po teście: zamknij zasoby, jeśli otwarte w setUp
    def tearDown(self):
        
        pass


# FUNKCJA DOKONUJĄCA PROSTYCH OBLICZEŃ MATEMATEMATYCZNYCH NP. OBLICZANIA POLA FIGURY / A FUNCTION THAT PERFORMS SIMPLE MATHEMATICAL CALCULATIONS, SUCH AS CALCULATING THE AREA OF A SHAPE.

    def test_calculate_triangle_area_typical(self):
        
        # Typowy przypadek: pozytywne wartości
        # Używa danych z setUp
        base = self.test_data['typical_base']
        height = self.test_data['typical_height']
        expected = self.test_data['typical_expected']
        self.assertEqual(calculate_triangle_area(base, height), expected)
        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)
             # self.assertEqual(calculate_triangle_area(10.0, 5.0), 25.0) 

    
    def test_calculate_triangle_area_zero(self):

        # Przypadek brzegowy: zero jest jako podstawa lub wysokość
        # Używa danych z setUp
        base = self.test_data['zero_base']
        height = self.test_data['typical_height']    # Mogę mieszać dane w/w
        expected = self.test_data['zero_expected']
        self.assertEqual(calculate_triangle_area(base, height), expected)
        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)
             # self.assertEqual(calculate_triangle_area(0.0, 5.0), 0.0)

    def test_calculate_triangle_area_negative(self):

        # Błędne dane: ujemne wartości
        # Używa danych z setUp
        base = self.test_data['negative_base']
        height = self.test_data['typical_height']
        with self.assertRaises(ValueError):
            calculate_triangle_area(-10.0, 5.0) 

    def test_calculate_triangle_area_parametrized(self):
        
        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)
        cases = [
            (self.test_data['typical_base'], self.test_data['typical_height'], self.test_data['typical_expected']),
            (self.test_data['zero_base'], self.test_data['typical_height'], self.test_data['zero_expected']),
            (self.test_data['typical_base'], self.test_data['zero_height'], self.test_data['zero_expected'])
        ]
                # cases = [(10.0, 5.0, 25.0), (0.0, 5.0, 0.0), (5.0, 0.0, 0.0)]
                # for base, height, expected in cases:
                #     with self.subTest(base=base, height=height):
                #         self.assertEqual(calculate_triangle_area(base, height), expected)

        for base, height, expected in cases:
            with self.subTest(base=base, height=height):
                self.assertEqual(calculate_triangle_area(base, height), expected)


# FUNKCJA KONWERTUJĄCA FORMAT DAT.

    def test_convert_date_format_typical(self):

        # Typowy przypadek: poprawna data
        # Używa danych z setUp zamiast hardcoded
        input_date = self.test_data['valid_date_typical']
        expected = self.test_data['valid_date_typical_expected']
        self.assertEqual(convert_date_format(input_date), expected)

        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)    
            # self.assertEqual(convert_date_format("31-12-2025"), "2025-12-31")

    def test_convert_date_format_invalid(self):

        # Przypadek błędny: zła data
        input_date = self.test_data['invalid_date_day']
        with self.assertRaises(ValueError):
            convert_date_format(input_date)       

         # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)    
            # with self.assertRaises(ValueError):
            #     convert_date_format("32-12-2025")
        
    def test_convert_date_format_edge(self):
    
        # Przypadek brzegowy: data z zerami
        # Używa danych z setUp
        input_date = self.test_data['valid_date_edge_zero']
        expected = self.test_data['valid_date_edge_zero_expected']
        self.assertEqual(convert_date_format(input_date), expected)
        
        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)
            # self.assertEqual(convert_date_format("01-01-2000"), "2000-01-01")

    def test_convert_date_format_valid_parametrized(self):
        # Parametryzowany test dla poprawnych dat: mieszanie danych z setUp
        cases = [
            (self.test_data['valid_date_typical'], self.test_data['valid_date_typical_expected']),  # Typowy: koniec roku
            (self.test_data['valid_date_edge_zero'], self.test_data['valid_date_edge_zero_expected']),  # Brzegowy: początek wieku
            (self.test_data['valid_date_leap'], self.test_data['valid_date_leap_expected']),   # Brzegowy: rok przestępny
            (self.test_data['valid_date_current'], self.test_data['valid_date_current_expected'])  # Dodatkowy: bieżąca data (w gotowości)
        ]
        for input_date, expected in cases:
            with self.subTest(input_date=input_date):
                self.assertEqual(convert_date_format(input_date), expected)

    def test_convert_date_format_invalid_parametrized(self):
        # Parametryzowany test dla niepoprawnych dat: używanie błędnych danych z setUp
        cases = [
            self.test_data['invalid_date_day'],  # Nieprawidłowy dzień
            self.test_data['invalid_date_non_leap'],  # Nieprzestępny rok
            self.test_data['invalid_date_format']  # Całkowicie błędny format
        ]
        for input_date in cases:
            with self.subTest(input_date=input_date):
                with self.assertRaises(ValueError):
                    convert_date_format(input_date)

#  FUNCKJA OBLICZAJĄCA PIERWIASTEK KWADRATOWY

    def test_typical_positive_number(self):
        """Testuje typową, dodatnią liczbę całkowitą."""
        num = self.test_data['typical_input']
        expected = self.test_data['typical_expected']
        result = calculate_square_root(num)
        self.assertEqual(result, expected)

    def test_edge_case_zero(self):
        """Testuje przypadek brzegowy dla zera."""
        num = self.test_data['edge_zero_input']
        expected = self.test_data['edge_zero_expected']
        result = calculate_square_root(num)
        self.assertEqual(result, expected)
        
    def test_large_number(self):
        """Testuje dużą liczbę, aby upewnić się, że typ float działa poprawnie."""
        num = self.test_data['large_input']
        expected = self.test_data['large_expected']
        result = calculate_square_root(num)
        self.assertEqual(result, expected)
        
    def test_float_input(self):
        """Testuje liczbę zmiennoprzecinkową (float)."""
        num = self.test_data['float_input']
        expected = self.test_data['float_expected']
        result = calculate_square_root(num)
        # Używamy assertAlmostEqual dla liczb zmiennoprzecinkowych, 
        # aby uniknąć błędów precyzji, choć w tym przypadku dokładność jest zachowana.
        self.assertAlmostEqual(result, expected)

    def test_negative_number_raises_error(self):
        """
        Testuje, czy podanie ujemnej liczby powoduje podniesienie wyjątku ValueError 
        z poprawną wiadomością.
        """
        num = self.test_data['negative_input']
        expected_msg = self.test_data['negative_expected_error_message']
        
        # assertRaises to menedżer kontekstu, który sprawdza, czy dany blok kodu 
        # podniesie oczekiwany wyjątek.
        with self.assertRaisesRegex(ValueError, expected_msg):
            calculate_square_root(num)