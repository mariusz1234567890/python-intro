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
from app import is_palindrome


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
            # Dla is_valid_email
            'valid_email': 'example@test.com',        # Typowy poprawny email
            'invalid_email': 'exampletest.com',       # Brak @
            'edge_empty': '',                         # Pusty string (brzegowy)

            # Dla calculate_triangle_area
            'typical_base': 10.0,                     # Typowa podstawa (pozytywna)
            'typical_height': 5.0,                    # Typowa wysokość (pozytywna)
            'typical_expected': 25.0,                 # Oczekiwany wynik dla typowego
            'zero_base': 0.0,                         # Brzegowy: zero jako podstawa
            'zero_height': 0.0,                       # Brzegowy: zero jako wysokość
            'zero_expected': 0.0,                     # Oczekiwany wynik dla zera
            'negative_base': -10.0,                   # Błędny: ujemna wartość (dla ValueError)

            # Nowe: Dla filter_even_numbers (przetwarzanie listy – filtracja parzystych)
            'numbers_list_typical': [1, 2, 3, 4, 5],  # Typowa: mieszana, oczekiwane [2, 4]
            'numbers_list_typical_expected': [2, 4],  # Oczekiwany wynik dla typowej
            'numbers_list_empty': [],                 # Brzegowy: pusta lista, oczekiwane []
            'numbers_list_empty_expected': [],        # Oczekiwany wynik dla pustej
            'numbers_list_odd': [1, 3, 5],        # Błędny: same nieparzyste, oczekiwane []
            'numbers_list_odd_expected': [],      # Oczekiwany wynik dla nieparzystych   

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
            'invalid_date_format': 'abc-def-ghi',             # Błędny: całkowicie zły format

            # Dla is_palindrome
            'palindrome_typical': 'Kobyła ma mały bok',  # Typowy: palindrom z spacjami i polskimi znakami
            'non_palindrome': 'Banan',                    # Nie palindrom: prosty tekst
            'edge_empty': '',                             # Brzegowy: pusty string (uznawany za palindrom)
            'edge_single_char': 'a',                      # Brzegowy: pojedynczy znak
            }


    # Czyszczenie po teście: zamknij zasoby, jeśli otwarte w setUp
    def tearDown(self):
        
        pass


    # To jest pojedynczy test (Metoda (funkcja wewnątrz klasy)). Nazwa musi zaczynać się od test_. Sprawdza, czy funkcja poprawnie rozpoznaje poprawny email.
    # self odnosi się do konkretnej instancji obiektu.
    def test_is_valid_email_valid(self):

        # Typowy przypadek: poprawny email
        # Asercja – mechanizm sprawdzający. Tutaj: oczekujemy, że wywołanie funkcji z poprawnym emailem zwróci wartość True. Jeśli nie, test zawiedzie.
        self.assertTrue(is_valid_email(self.test_data['valid_email']))

    def test_is_valid_email_invalid(self):
        # Przypadek braku @.
        # Oczekujemy, że funkcja zwróci False.
        self.assertFalse(is_valid_email(self.test_data['invalid_email']))

    def test_is_valid_email_edge(self):
        # Przypadek brzegowy(edge).
        # Błędne dane: pusty string.
        # Oczekujemy, że funkcja zwróci False.
        self.assertFalse(is_valid_email(self.test_data['edge_empty'])) 


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

# FUNKCJA PRZETWARZAJĄCA LISTĘ DANYCH (SORTOWANIE, FILTRACJA) / DATA LIST PROCESSING FUNCTION 

    def test_filter_even_numbers_typical(self):

        # Typowy przypadek: mieszana lista
        # Używa danych z setUp
        input_list = self.test_data['numbers_list_typical']
        expected = self.test_data['numbers_list_typical_expected']
        self.assertEqual(filter_even_numbers(input_list), expected)
        
        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)
            # self.assertEqual(filter_even_numbers([1,2,3,4,5]), [2,4])

    def test_filter_even_numbers_empty(self):
        
        # Przypadek brzegowy: puste listy
        # Używa danych z setUp

        input_list = self.test_data['numbers_list_empty']
        expected = self.test_data['numbers_list_empty_expected']
        self.assertEqual(filter_even_numbers(input_list), expected)
        
        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)    
            # self.assertEqual(filter_even_numbers([]),[])

    def test_filter_even_numbers_all_odd(self):

        # Przypadek błędny: same nieparzyste
        # Używa danych z setUp

        input_list = self.test_data['numbers_list_odd']
        expected = self.test_data['numbers_list_odd_expected']
        self.assertEqual(filter_even_numbers(input_list), expected)
            
        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)
            # self.assertEqual(filter_even_numbers([1,3,5]), [])


    def test_filter_even_numbers_parametrized(self):
        # Parametryzowany: mieszanie danych z setUp
        cases = [
            (self.test_data['numbers_list_typical'], self.test_data['numbers_list_typical_expected']),
            (self.test_data['numbers_list_empty'], self.test_data['numbers_list_empty_expected']),
            (self.test_data['numbers_list_odd'], self.test_data['numbers_list_odd_expected'])
        ]
        for input_list, expected in cases:
            with self.subTest(input_list=input_list):
                self.assertEqual(filter_even_numbers(input_list), expected)

    # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)
            # def test_filter_even_numbers_parametrized(self):
            #     cases = [([1,2,3,4,5], [2,4]), ([],[]), ([1,3,5], [])]
            #     for input_list, expected in cases:
            #         with self.subTest(input_list=input_list):
            #             self.assertEqual(filter_even_numbers(input_list), expected)

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

        # Używa danych z setUp zamiast hardcoded (pozostawione dla celów edukacyjno-porównawczych)            
            # def test_convert_date_format_valid_parametrized(self):
            #     cases = [
            #         ("31-12-2023", "2023-12-31"),  # Typowy: koniec roku
            #         ("01-01-2000", "2000-01-01"),  # Brzegowy: początek wieku
            #         ("29-02-2024", "2024-02-29")   # Brzegowy: rok przestępny
            #     ]
            #     for input_date, expected in cases:
            #         with self.subTest(input_date=input_date):
            #             self.assertEqual(convert_date_format(input_date), expected)

            # def test_convert_date_format_invalid_parametrized(self):
            #     cases = [
            #         "32-12-2023",  # Nieprawidłowy dzień
            #         "29-02-2023",  # Nieprzestępny rok
            #         "abc-def-ghi"  # Całkowicie błędny format
            #     ]
            #     for input_date in cases:
            #         with self.subTest(input_date=input_date):
            #             with self.assertRaises(ValueError):
            #                 convert_date_format(input_date)


# FUNKCJA SPRAWDZAJĄCA, CZY TEKST JEST PALINDROMEM.

    def test_is_palindrome_typical(self):
            # Przypadek typowy: jest palindromem
        self.assertTrue(is_palindrome(self.test_data['palindrome_typical']))

    def test_is_palindrome_not(self):
            # Przypadek: nie jest palindromem
        self.assertFalse(is_palindrome(self.test_data['non_palindrome']))

    def test_is_palindrome_edge(self):
            # Przypadek brzegowy: brak znaku lub pojedynczy znak
        self.assertTrue(is_palindrome(self.test_data['edge_empty']))
        self.assertTrue(is_palindrome(self.test_data['edge_single_char']))

    
    def test_is_palindrome_true_parametrized(self):
        cases = [
            (self.test_data['palindrome_typical'], True),
            (self.test_data['edge_empty'], True),
            (self.test_data['edge_single_char'], True),
            ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(is_palindrome(text), expected)

# def test_is_palindrome_false_parametrized(self):
#         cases = [
#             (self.test_data['non_palindrome'], False)
#         ]
#         for text, expected in cases:
#             with self.subTest(text=text):
#                 self.assertEqual(is_palindrome(text), expected)