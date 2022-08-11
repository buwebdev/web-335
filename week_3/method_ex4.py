""" 
    Title: method_ex4.py
    Author: Professor Krasso
    Date: 11 August 2022
    Description: Example file for creating methods in Python.
"""

""" @method: calculateBill.
    @description: Method to calculate the total of a bill. 
    @params: appetizer, beverage, main_course, dessert.
    @returns: Floating point value.
"""
def calculate_bill(appetizer, beverage, main_course, dessert):
    return appetizer + beverage + main_course + dessert

""" @method: calculateTax. 
    @description: Method to calculate the tax for a bill.
    @params: subtotal, tax.
    @returns: Floating point value.
"""
def calculate_tax(subtotal, tax):
    return subtotal * tax

""" @method: calculateTotal.
    @description: Method to calculate the total bill (includes tax).
    @params: subtotal, tax_amount
    @returns: Floating point value.
"""
def calculate_total(subtotal, tax_amount): 
    return subtotal + tax_amount

""" Variables for bill """
appetizer = 7.49
beverage = 26.80
entree = 45.30
dessert = 12.30
tax = .08

""" Variables to hold the values from the above methods. """ 
bill_subtotal = calculate_bill(appetizer, beverage, entree, dessert)
bill_tax = calculate_tax(bill_subtotal, tax)
bill_total = calculate_total(bill_subtotal, bill_tax)

""" Variable to hold the string output. """
output = "Appetizer: {0}\nBeverage: {1}\nMain Course: {2}\nDessert: {3}\nSubtotal: {4:.2f}\nTax: {5:.2f}\nTotal: {6:.2f}".format(appetizer, beverage, entree, dessert, bill_subtotal, bill_tax, bill_total)

print(output)