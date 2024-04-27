from operations import display,calculate_total_amount
from write import write_rent_bill
from read import read


land_info = []
def find_selected_land(data, kitta_no):
    for row in data:
        if row[0] == kitta_no:
            return row


def rentLand():
        while True:
                customer_name = input("Enter your name: ")
                address = input("Enter your address: ")
                phone_number = int(input("Enter your phone number: "))

                if not customer_name.strip() or not phone_number or not address.strip():
                        print("Please provide valid customer name, phone number, and address.")  # Print an error message if any field is empty
                else:
                        break



        data=read()
        rent=True
        ultimate_total=0
        while rent:  
                display() 
                kitta_no = input("Enter the kitta no. of the land you would like to rent: ")
                selected_land_info = find_selected_land(data, kitta_no)

                # if selected_land_info is None:
                #         print("Please enter a valid kitta number!")
                #         #else:
                if selected_land_info[-1].strip() == "Not Available":
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
                                
                        total_amount, vat_amount, final_amount = calculate_total_amount( int(selected_land_info[4]), rent_duration)
                        ultimate_total += final_amount  # Update ultimate total

                        land_info.append([selected_land_info[0]],[selected_land_info[1]], [selected_land_info[2]],[selected_land_info[3]],rent_duration,total_amount, vat_amount, final_amount)
                        
                        while True:
                                choice = input("Do you want to rent another land? (Y/N): ").upper()
                                if choice == "N":
                                        write_rent_bill(customer_name, phone_number, address, land_info, ultimate_total)
                                        print( f"Your bill has been issued and saved in {customer_name}.txt. Thank you!")
                                        rent=False
                                        break
                                        
                                elif choice=="Y":
                                        break

                                else:
                                        print("Invalid. Please enter 'Y' or 'N; !")
                                                        
        return kitta_no, selected_land_info,rent_duration




        # if any(
        #     row[0] == kitta_no for row in data[0:]):  # Check if kitta_no exists in data
        #     selected_land_info =row for row in data if row[0] == kitta_no
        #     if selected_land_info[-1].strip() == "Not Available":
        #         print("This selected_land_info is not available. Please choose another one.")
        #     else:
        #         return kitta_no, selected_land_info
        # else:
        #     print("Invalid kitta no. Please enter a valid kitta number.")


    
    
    # while phone_number is None:
    #     try:
    #         phone_number = int(input("Enter your phone number: "))
    #         if phone_number <= 0:
    #             print("Please enter a positive integer for phone number.")
    #             phone_number = None  # Reset to None for retry
                
    #     except ValueError:
    #         print("Invalid input. Please enter a valid integer for phone number.")


    # #return customer_name, phone_number, address



    