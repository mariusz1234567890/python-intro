
# Instalacja modulu do unit testow / Instalation of module to unit tests.

import unittest
print("Moduł 'unittest' jest dostępny.")

# Zainstalowanie pytest komenda w terminalu.
    # py -m pip install pytest


# Zainstalowanie coverage komenda w terminalu.
    # py -m pip install coverage


# Import konkretnej funkcji is_valid_email z pliku o nazwie string_utils, którą chcemy przetestować.
from tests_string_utils import is_valid_email 
# Import konkretnej funkcji  is_polindrome z pliku o nazwie string_utils, którą chcemy przetestować.
from string_utils import is_palindrome
# Import konkretnej fukcji count_words z pliku o nazwie string_utils, którą chcemy przetestować.
from string_utils import count_words



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


            # Dla is_palindrome
            'palindrome_typical': 'Kobyła ma mały bok',  # Typowy: palindrom z spacjami i polskimi znakami
            'non_palindrome': 'Banan',                    # Nie palindrom: prosty tekst
            'edge_empty': '',                             # Brzegowy: pusty string (uznawany za palindrom)
            'edge_single_char': 'a',                      # Brzegowy: pojedynczy znak
            
            
            # Dla count_words 
            'text_simple': "Ala ma kota",                            # Oczekiwane słowa: 3
            'edge_empty': "",                                        # Oczekiwane słowa: 0    
            'text_complex': "Dzień dobry, świecie! Jak się masz?",   # Oczekiwane słowa: 6
            'text_whitespace': "   Dużo spacji   i tu   ",           # Oczekiwane słowa: 3
            'text_numbers': "Mam 3 jabłka i 1 gruszkę",              # Oczekiwane słowa: 5 (zależy jak traktujesz cyfry)
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


    # FUNKCJA LICZĄCĄ SŁOWA W TEKŚCIE

    def test_count_words_simple(self):
            """Testuje liczenie słów w prostym zdaniu."""
            # Używamy assertEqual, aby sprawdzić, czy wynik funkcji jest równy oczekiwanej wartości.
            self.assertEqual(count_words(self.test_data['text_simple']), 3)

    def test_count_words_empty(self):
            """Testuje liczenie słów w pustym tekście."""
            self.assertEqual(count_words(self.test_data['edge_empty']), 0)

    def test_count_words_complex(self):
            """Testuje liczenie słów z interpunkcją."""
            self.assertEqual(count_words(self.test_data['text_complex']), 6) # Dzień, dobry, świecie, Jak, się, masz

    def test_count_words_whitespace(self):
            """Testuje liczenie słów z nadmiarowymi spacjami."""
            self.assertEqual(count_words(self.test_data['text_whitespace']), 3) # Dużo, spacji, i

    def test_count_words_numbers(self):
            """Testuje liczenie słów w tekście zawierającym cyfry."""
            self.assertEqual(count_words(self.test_data['text_numbers'], 5),)   # Mam 3 jabłka i 1 gruszkę

    
    def test_count_words_parametrized(self):
            """Parametryzowany test dla funkcji liczącej słowa."""
            cases = [
                ("Hello world", 2),
                ("", 0),
                (" Jeden ", 1),
                ("Wiele   spacji   pomiędzy słowami", 4),
            ]
            for text, expected_count in cases:
                with self.subTest(text=text):
                    self.assertEqual(count_words(text), expected_count)