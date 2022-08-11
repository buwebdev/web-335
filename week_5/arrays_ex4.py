""" 
    Title: arrays_ex4.py
    Author: Professor Krasso
    Date: 11 August 2022
    Description: Example file for working with Arrays
"""

""" String array """ 
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

""" @method: output.
    @description: Displays an output string.
    @params: house, mascot.
    @returns: formatted string with appended house and mascot values.
"""
def output(house, mascot):
    return "House {0}'s mascot is a {1}".format(house, mascot) 

""" For loop to iterate over the houses array """
for house in houses:
    if house == "Gryffindor":
        print(output("Gryffindor", "Lion"))
    if house == "Hufflepuff":
        print(output("Hufflepuff", "Badger"))
    if house == "Ravenclaw":
        print(output("Ravenclaw", "Eagle"))
    if house == "Slytherin":
        print(output("Slytherin", "Snake"))
    
