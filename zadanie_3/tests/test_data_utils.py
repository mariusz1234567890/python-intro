# Instalacja modulu do unit testow / Instalation of module to unit tests.

import unittest
print("Moduł 'unittest' jest dostępny.")

# Zainstalowanie pytest komenda w terminalu.
    # py -m pip install pytest


# Zainstalowanie coverage komenda w terminalu.
    # py -m pip install coverage


# Import konkretnej funkcji is_valid_email z pliku o nazwie app.py, którą chcemy przetestować.

# Import konkretnej funkcji filter_even_numbers z pliku o nazwie app.py, którą chcemy przetestować.
from app import filter_even_numbers




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
           
            # Dla filter_even_numbers (przetwarzanie listy – filtracja parzystych)
            'numbers_list_typical': [1, 2, 3, 4, 5],  # Typowa: mieszana, oczekiwane [2, 4]
            'numbers_list_typical_expected': [2, 4],  # Oczekiwany wynik dla typowej
            'numbers_list_empty': [],                 # Brzegowy: pusta lista, oczekiwane []
            'numbers_list_empty_expected': [],        # Oczekiwany wynik dla pustej
            'numbers_list_odd': [1, 3, 5],        # Błędny: same nieparzyste, oczekiwane []
            'numbers_list_odd_expected': [],      # Oczekiwany wynik dla nieparzystych   

            # Inicjalizacja różnych scenariuszy słowników.
            # --- Scenariusz 1: Dwa typowe słowniki bez wspólnych kluczy ---
            'simple_input_1': {'a': 1, 'b': 2},
            'simple_input_2': {'c': 3, 'd': 4},
            'simple_expected': {'a': 1, 'b': 2, 'c': 3, 'd': 4},

            # --- Scenariusz 2: Nakładające się klucze (sprawdzenie nadpisywania) ---
            'overlap_input_1': {'a': 1, 'b': 2, 'c': 3},
            'overlap_input_2': {'b': 99, 'd': 100}, # 'b' zostanie nadpisane
            'overlap_expected': {'a': 1, 'b': 99, 'c': 3, 'd': 100},

            # --- Scenariusz 3: Brzegowe przypadki z pustymi słownikami ---
            'empty': {},
            'non_empty': {'x': 10, 'y': 20},
            
            # Oczekiwane wyniki dla przypadków brzegowych są takie same jak słownik niepusty



            """
            Inicjalizacja danych testowych w konwencji 'input'/'expected'.
            """
            # --- Scenariusz 1: Dwa typowe słowniki bez wspólnych kluczy ---
            'simple_input_1': {'a': 1, 'b': 2},
            'simple_input_2': {'c': 3, 'd': 4},
            'simple_expected': {'a': 1, 'b': 2, 'c': 3, 'd': 4},

            # --- Scenariusz 2: Nakładające się klucze (sprawdzenie nadpisywania) ---
            'overlap_input_1': {'a': 1, 'b': 2, 'c': 3},
            'overlap_input_2': {'b': 99, 'd': 100}, # 'b' zostanie nadpisane przez 99
            'overlap_expected': {'a': 1, 'b': 99, 'c': 3, 'd': 100},

            # --- Scenariusz 3: Brzegowe przypadki z pustymi słownikami ---
            'empty': {},
            'non_empty': {'x': 10, 'y': 20},
            
            # Oczekiwane wyniki dla przypadków brzegowych są takie same jak słownik niepusty
      
            }


    # Czyszczenie po teście: zamknij zasoby, jeśli otwarte w setUp
    def tearDown(self):
        
        pass


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


    # FUNKCJA ŁĄCZENIA SŁOWNIKÓW

    def test_merge_two_simple_dicts(self):
        """Testuje połączenie dwóch standardowych słowników bez wspólnych kluczy."""
        d1 = self.test_data['simple_input_1']
        d2 = self.test_data['simple_input_2']
        expected = self.test_data['simple_expected']
        
        result = merge_dicts(d1, d2)
        self.assertEqual(result, expected)

    def test_merge_with_overlapping_keys(self):
        """Testuje, czy drugi słownik poprawnie nadpisuje klucze."""
        d1 = self.test_data['overlap_input_1']
        d2 = self.test_data['overlap_input_2']
        expected = self.test_data['overlap_expected']
        
        result = merge_dicts(d1, d2)
        self.assertEqual(result, expected)
        
    def test_merge_empty_into_non_empty(self):
        """Testuje połączenie niepustego słownika z pustym."""
        non_empty = self.test_data['non_empty']
        empty = self.test_data['empty']
        
        result = merge_dicts(non_empty, empty)
        self.assertEqual(result, non_empty) 

    def test_merge_non_empty_into_empty(self):
        """Testuje połączenie pustego słownika z niepustym."""
        non_empty = self.test_data['non_empty']
        empty = self.test_data['empty']
        
        result = merge_dicts(empty, non_empty)
        self.assertEqual(result, non_empty) 

    def test_merge_two_empty_dicts(self):
        """Testuje połączenie dwóch pustych słowników."""
        empty = self.test_data['empty']

        result = merge_dicts(empty, empty)
        self.assertEqual(result, {})
