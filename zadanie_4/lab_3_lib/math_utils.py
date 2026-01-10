# FUNKCJA DOKONUJĄCA PROSTYCH OBLICZEŃ MATEMATEMATYCZNYCH NP. OBLICZANIA POLA FIGURY / A FUNCTION THAT PERFORMS SIMPLE MATHEMATICAL CALCULATIONS, SUCH AS CALCULATING THE AREA OF A SHAPE.
#  Cel: Oblicza pole trójkąta (wzór: (base * height) / 2). Proste obliczenia matematyczne.


def calculate_triangle_area(base: float, height: float) -> float:

    """Oblicza pole trójkąta. Rzuca ValueError dla ujemnych wartości."""
    if base < 0 or height < 0:
        raise ValueError("Podstawa i wysokość nie mogą być ujemne, ale o wartości zero")
    return (base * height) / 2



# FUNKCJA KONWERTUJĄCA FORMAT DAT
""" Konwertuje datę z 'DD-MM-YYYY' na 'YYYY-MM-DD'. """

from datetime import datetime
def convert_date_format(date_str):
    try:
        dt = datetime.strptime(date_str, "%d-%m-%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Niepoprawny wejściowy format daty, oczekiwany jest DD-MM-YYYY")
    


#  FUNCKJA OBLICZAJĄCA PIERWIASTEK KWADRATOWY
"""
    Oblicza pierwiastek kwadratowy.

    Args:            number (float): Liczba nieujemna.

    Returns:         float: Pierwiastek.

    Raises:          ValueError: Jeśli ujemna.
    """
import math
def calculate_square_root(number: float) -> float:
    
    if number < 0:
        raise ValueError("Liczba musi być nieujemna.")
    return math.sqrt(number)