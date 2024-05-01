from read import read
from operations import display,clear
from rent import find_selected_land
from write import write_return_bill

def update(returning_land_info):
    file=open('land.txt', 'r') #opening the file in read mode
    lines = file.readlines() #reading all the lines

    #to change the availability status of the rented land
    for i, line in enumerate(lines):     #enumerating to get both index and content of each line in the list
        if line.startswith(returning_land_info[0]):
            lines[i] = line.replace("Not Available", "Available")   # replacing "Not Available" with "Available" for the user returned land

    with open('land.txt', 'w') as file:   # opening the file in write mode
        file.writelines(lines)  # writing the modified lines back to the file

    
    return read()  # returning the updated data


def returnLand():
        return_invoice=[]  #creating an empty list to store user returned land information
        while True:
                customer_name = input("Enter your name: ")
                address = input("Enter your address: ")
                phone_number = int(input("Enter your phone number: "))

                if not customer_name.strip() or not phone_number or not address.strip():
                        print("Please provide valid customer name, phone number, and address.")  # Print an error message if any field is empty
                else:
                        break
                
        data=read()
        returning=True
        fine,months_late=0,0
        while returning:
                display() 
                kitta_no = input("Enter the kitta no. of the land you would like to return: ")
                returning_land_info=find_selected_land(data,kitta_no)  #storing the row in returning_land_info variable

                if returning_land_info[-1].strip()=="Not Available":  #checking the last element of the row 
                        while True:
                                try:
                                        rent_duration=int(input("Enter the period you've rented this land for(in months):"))
                                        return_duration=int(input("Enter the period you're returning this land after(in months):"))
                                        if rent_duration<= 0 and return_duration<=0:
                                                print("Please enter a positive integer for duration.")
                                        else:
                                                break  # Exit the loop if valid duration entered
                                except ValueError:
                                        print("Invalid input. Please enter a valid integer for duration.")
                        
                        if (return_duration>rent_duration):
                                months_late=(return_duration-rent_duration)
                                fine=500*months_late
                                print(f"Since you've returned this land late you're fined Rs.{fine}")
                               
                        else:
                                print("Returned the land in time without fine added!")
                        
                        # extracting information about the returned land from the returning_land_info list and assigning it to individual variables.               
                        kitta_no=returning_land_info[0]
                        location=returning_land_info[1] 
                        direction=returning_land_info[2]     
                        anna=returning_land_info[3]
                        price=int(returning_land_info[4])*rent_duration

                        return_invoice.append([kitta_no,location,direction,anna,price])  #adding details of the returned land to the list
                        
                        update(returning_land_info)   #updating the text file each time the user returns the land

                        while True:
                                choice = input("Do you want to return another land? (Y/N): ").upper()
                                if choice=="Y":
                                        break   #exiting the inner loop and continuing with the returning process
                                elif choice == "N":
                                        returning=False   #setting 'returning' to false to exit the outer loop
                                        print( f"Your bill has been issued and saved in Returned By {customer_name}.txt. Thank you!")
                                        clear()
                                        write_return_bill(kitta_no,customer_name, phone_number, address, return_invoice,rent_duration,fine,months_late)
                                        break #exiting the outer loop

                                else:
                                        print("Invalid. Please enter 'Y' or 'N; !")
                                
                else:
                        print("You havenot rented this land!")


                              
                       
            
