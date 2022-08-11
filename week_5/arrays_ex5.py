""" 
    Title: arrays_ex5.py
    Author: Professor Krasso
    Date: 11 August 2022
    Description: Example file for working with Arrays
"""

""" String Array of Composers """
composers = ["Beethoven", "Bach", "Mozart", "Brahms"]

""" @method: find_composers.
    @description: Iterates over the composer array and returns a matching composer by the name argument.
    @params: name.
    @returns: composer.
"""
def find_composer(name):
    for composer in composers:
        if composer == name:
            return composer

""" @method: display_composers.
    @description: Displays a list of composers.
    @params: none.
    @returns: none.
"""
def display_composers():
    for composer in composers:
        print(composer)

""" Call the methods and output the results. """
print("-- LIST OF COMPOSERS --")
print(display_composers())

print('\n')

print("-- SELECTED COMPOSER --")
print(find_composer("Bach"))