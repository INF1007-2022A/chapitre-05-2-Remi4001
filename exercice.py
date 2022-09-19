#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_bill(name, data):
    # INDEX_NAME = 0 inutilisé
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2
    sous_total = 0
    for entry in data:
        sous_total += entry[INDEX_QUANTITY] * entry[INDEX_PRICE]

    taxes = sous_total * 0.15

    return (f"{name}\n"
            f"SOUS TOTAL{sous_total:>11.2f} $\n"
            f"TAXES{taxes:>16.2f} $\n"
            f"TOTAL{sous_total+taxes:>16.2f} $")


def format_number(number, num_decimal_digits):
    str_int_number = ""
    string = ""
    separateur = " "

    # Ne pas garder le "-", on va le rajouter à la fin
    if number < 0:
        str_int_number = str(int(abs(number)))
    else:
        str_int_number = str(int(number))

    # Premiers caractères du nombre
    first_numbers = str_int_number[:len(str_int_number) % 3]
    str_int_number = str_int_number[len(str_int_number) % 3:]
    string = first_numbers

    # Reste de la partie entière
    for i in range(len(str_int_number)//3):
        string += separateur + str_int_number[i*3:i*3+3]

    # enlever l'espace en trop au début si besoin
    if string[0] == separateur:
        string = string[1:]

    # Retourne la partie décimale sans le "0."" au début
    str_dec_number = str(abs(number) % 1)[2:]

    # Ajouter "." aux nombres décimaux
    if number % 1 != 0:
        string += "."

    for i in range(len(str_dec_number)):
        if i < num_decimal_digits:
            if i % 3 == 0 and i != 0:
                string += separateur
            string += str_dec_number[i]

    # Ajouter le signe négatif au besoin
    if number < 0:
        string = "-" + string

    return string


def get_triangle(num_rows):
    border = "+"
    background = " "
    foreground = "A"

    # Première ligne (bordure supérieure)
    string = border * (num_rows * 2 + 1) + "\n"

    # Le Triangle
    for i in range(num_rows):
        string += (border +
                   background * (num_rows - i - 1) +
                   foreground * (i * 2 + 1) +
                   background * (num_rows - i - 1) +
                   border + "\n")

    # Dernière ligne (bordure inférieure)
    string += border * (num_rows * 2 + 1) + "\n"

    return string


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [
          ("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 2))

    print(get_triangle(2))
    print(get_triangle(5))
