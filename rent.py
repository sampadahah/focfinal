from operations import display
from write import write_rent_bill
from read import read


rent_invoice= []    #creating an empty list to store rent invoice information
def find_selected_land(data, kitta_no):
    for row in data:
        if row[0] == kitta_no:
            return row

# def update(selected_land_info):
#        file=open('land.txt','r')
#        replaced=selected_land_info[-1].replace("Available","Not Available")
#        file.close()

#        file=open('land.txt','r')
#        file.writelines(replaced)
#        file.close()




def rentLand():
        while True:
                customer_name = input("Enter your name: ")
                address = input("Enter your address: ")
                phone_number = int(input("Enter your phone number: "))

                if not customer_name.strip() or not phone_number or not address.strip():
                        print("Please provide valid customer name, phone number, and address.")  # Print an error message if any field is empty
                else:
                        break   #exiting loop if valid name, phone number and address is entered



        data=read()
        rent=True

        while rent:  
                display() 
                kitta_no = input("Enter the kitta no. of the land you would like to rent: ")
                selected_land_info = find_selected_land(data, kitta_no)

                if selected_land_info[-1].strip() == " Not Available":
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

                
                        location=selected_land_info[1] 
                        direction=selected_land_info[2]     
                        anna=selected_land_info[3]
                        price=selected_land_info[4]*rent_duration
                                

                        rent_invoice.append([location,direction,anna,price])
                        print(rent_invoice)
                        
                        while True:
                                choice = input("Do you want to rent another land? (Y/N): ").upper()
                                if choice=="Y":
                                       break  #exiting the inner loop and continuing with the renting process

                                elif choice == "N":
                                        rent=False   #setting 'rent' to false to exit the outer loop
                                        print( f"Your bill has been issued and saved in {customer_name}.txt. Thank you!")
                                        write_rent_bill(kitta_no,customer_name, phone_number, address,rent_invoice,rent_duration) 
                                        break

                                else:
                                        print("Invalid. Please enter 'Y' or 'N; !")
                                                        
        # return kitta_no, selected_land_info,rent_duration




        # if any(
        #     row[0] == kitta_no for row in data[0:]):  # Check if kitta_no exists in data
        #     selected_land_info =row for row in data if row[0] == kitta_no
        #     if selected_land_info[-1].strip() == "Not Available":
        #         print("This selected_land_info is not available. Please choose another one.")
        #     else:
        #         return kitta_no, selected_land_info
        # else:
        #     print("Invalid kitta no. Please enter a valid kitta number.")


    
    
   


    # #return customer_name, phone_number, address



    