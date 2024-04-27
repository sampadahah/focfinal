import os
from read import read
def display():
    # it reads data from  the text file
    data = read()
    print("-----------------------------------------------------------------------------------------------")
    for row in data: # using for loop so it iterates over each row in the file_data
        print(row[0].ljust(9) + '|', end='') #prints first element of the row and left-align it with a width if 4 characters, followed by a '|'
        for each in row[1:]:
            print(each.ljust(16) + '|', end='') #prints first element of the row and left-align it with a width if 4 characters, followed by a '|'
        print() #Print a new line after printing each row
        print("-----------------------------------------------------------------------------------------------")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Remove the content from the console screen

def calculate_total_amount(price, rent_duration,fine):
    total_amount = price * rent_duration
    vat_amount = 0.15 * total_amount
    final_amount = total_amount + vat_amount+fine
    return total_amount, vat_amount, final_amount,fine