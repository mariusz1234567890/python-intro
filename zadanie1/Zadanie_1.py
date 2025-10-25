import math

# https://www.w3schools.com/python/python_lists.asp
# 2 sztywne listy
list1 = [1, 4, 3, 5, 2]
list2 = [4, 2, 1, 5, 3]

# zbiorcza lista z wynikami
results = []


# https://www.w3schools.com/python/python_try_except.asp
try:
    # https://www.w3schools.com/python/python_conditions.asp
    if len(list1) != len(list2):
        raise ValueError("Listy mają różną długość")



    # polaczenie par z dwoch list i wykonanie dzialania
    for number1, number2 in zip(list1, list2):
        # jesli cyfr z list sa rozne to dodac je do siebie
        if number1 != number2:
            result = number1 + number2
            print(f"{number1} + {number2} = {result}")
        # jesli cyfry nie sa rozne to pomnoczyc je przez siebie
        else:
            result = number1 * number2
    
            print(f"{number1} * {number2} = {result}")
        # dodanie wyniku do nowej listy
        results.append(result)


except ValueError as ve:
    print("błąd wartości: ", ve)


else:
    # jeśli nie ma błędów przystąp do wyświetlania 
    print (f"Wyniki to: {results}")

    # uzycie bioblioteki math
    # https://www.w3schools.com/python/python_math.asp
    min_result = min(results)
    max_result = max(results)


    print(min_result)
    print(max_result)

    