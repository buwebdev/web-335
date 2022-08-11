""" 
    Title: method_ex2.py
    Author: Professor Krasso
    Date: 11 August 2022
    Description: Example file for creating methods in Python.
"""

def tax_amount(billTotal):
    return billTotal * .08

print('Subtotal: $19.46\nTax (8%): ${0:.2f}\nTotal: {1:.2f}'.format(tax_amount(19.43), (19.46 + tax_amount(19.43))))