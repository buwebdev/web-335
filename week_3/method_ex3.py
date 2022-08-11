""" 
    Title: method_ex3.py
    Author: Professor Krasso
    Date: 11 August 2022
    Description: Example file for creating methods in Python.
"""

def get_name(fname, lname):
    return "{0} {1}".format(fname, lname)

def get_genre(genre):
    return genre

""" Composer variables """
first_name = "Wolfgang"
last_name = "Mozart"
genre = "Classical Music"

""" Output string variable """
output = "Composer: {0}\nGenre: {1}".format(get_name(first_name, last_name), get_genre(genre))

print(output)