from operations import display,clear
from write import write_rent_bill
from read import read



def find_selected_land(data, kitta_no):
    for row in data:     #iterating over each row in data list
        if row[0] == kitta_no:
            return row    #returning the row that matches the kitta_no selected by the user


def update(selected_land_info):
    file=open('land.txt', 'r') # opening the file in read mode
    lines = file.readlines() # read all the lines

    #to change the availability status of the rented land
    for i, line in enumerate(lines):     #enumerating to get both index and content of each line in the list
        if line.startswith(selected_land_info[0]):
            lines[i] = line.replace("Available", "Not Available")   # replacing "Available" with "Not Available" for the user rented land

    with open('land.txt', 'w') as file:   # opening the file in write mode
        file.writelines(lines)  # writing the modified lines back to the file

    
    return read()  # returning the updated data




def rentLand():
        rent_invoice= []    #creating an empty list to store rent invoice information
        while True:
                customer_name = input("Enter your name: ")
                address = input("Enter your address: ")
                phone_number = int(input("Enter your phone number: "))
                customer_name,address=customer_name.title(),address.title()   #capitalizing first letter of each word
                if not customer_name.strip() or not phone_number or not address.strip():
                        print("Please provide valid customer name, phone number, and address.")  # printing an error message if any field is empty
                else:
                        break   #exiting loop if valid name, phone number and address is entered



        data=read()
        rent=True

        while rent:  
                display() 
                kitta_no = input("Enter the kitta no. of the land you would like to rent: ")
                selected_land_info = find_selected_land(data, kitta_no)   #storing the row in selected_land_info variable

                if selected_land_info[-1].strip() == "Not Available":           #checking the last element of the row 
                        print("This land is not available. Please choose another one.")
                        
                else:
                        print (f"You have selected {selected_land_info[2]} facing land in {selected_land_info[1]}, price Rs.{selected_land_info[4]}")
                        while True:
                                try:
                                        rent_duration = int(input("Enter the rental period in months: "))
                                        if rent_duration <= 0:
                                                print("Please enter a positive integer for duration.")
                                        else:
                                                break  # Exit the loop if valid duration entered
                                except ValueError:
                                        print("Invalid input. Please enter a valid integer for duration.")

                        #extracting information about the rented land from the selected__land_info list and assigning it to individual variables.
                        location=selected_land_info[1] 
                        direction=selected_land_info[2]     
                        anna=selected_land_info[3]
                        price=int(selected_land_info[4])*rent_duration
                                

                        rent_invoice.append([kitta_no,location,direction,anna,price])  #adding details of the rented land to the list
                        update(selected_land_info)              #updating the text file after the user returns the land
                        while True:
                                choice = input("Do you want to rent another land? (Y/N): ").upper()
                                if choice=="Y":
                                       break  #exiting the inner loop and continuing with the renting process

                                elif choice == "N":
                                        rent=False   #setting 'rent' to false to exit the outer loop
                                        print( f"Your bill has been issued and saved in Rented By {customer_name}.txt. Thank you!")
                                        clear()
                                        write_rent_bill(kitta_no,customer_name, phone_number, address,rent_invoice,rent_duration) 
                                        break

                                else:
                                        print("Invalid. Please enter 'Y' or 'N' !")
                                                        






    
    
   





    