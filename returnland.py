from read import read
from operations import display,calculate_total_amount
from rent import find_selected_land
from write import write_return_bill

# def find_selected_land(data, kitta_no):
#     for row in data:
#         if row[0] == kitta_no:
#             return row


def returnLand():
        while True:
                customer_name = input("Enter your name: ")
                address = input("Enter your address: ")
                phone_number = int(input("Enter your phone number: "))

                if not customer_name.strip() or not phone_number or not address.strip():
                        print("Please provide valid customer name, phone number, and address.")  # Print an error message if any field is empty
                else:
                        break
                
        data=read()
        land_info=[]
        returning=True
        ultimate_total=0

        while returning:
                display() 
                kitta_no = input("Enter the kitta no. of the land you would like to return: ")
                returning_land_info=find_selected_land(data,kitta_no)

                if returning_land_info[-1].strip()=="Not Available":
                        rental_duration=int(input("Enter the period you've rented this land for(in months):"))
                        return_duration=int(input("Enter the period you're returning this land after(in months):"))
                        if (return_duration>rental_duration):
                                months_late=(return_duration-rental_duration)
                                fine=500*months_late
                                print(f"Since you've returned this land late you're fined Rs.{fine}")
                                total_amount, vat_amount, final_amount,fine= calculate_total_amount( int(returning_land_info[4]), rental_duration)
                                ultimate_total += final_amount  # Update ultimate total

                                land_info.append(([returning_land_info[0]],[f"{returning_land_info[1]}, {returning_land_info[2]}"],[rental_duration],([total_amount], vat_amount, final_amount,fine),))
                                write_return_bill(customer_name, phone_number, address, land_info, ultimate_total,returning_land_info,rental_duration)
                        
                        else:
                                print("Returned the land in time without fine added!")

                                while True:
                                        choice = input("Do you want to return another land? (Y/N): ").upper()
                                        if choice == "N":
                                                # write_return_bill(customer_name, phone_number, address, land_info, ultimate_total,returning_land_info,rental_duration)
                                                print( f"Your bill has been issued and saved in {customer_name}.txt. Thank you!")
                                                returning=False
                                
                                        elif choice=="Y":
                                                break

                                        else:
                                                print("Invalid. Please enter 'Y' or 'N; !")


                        # else:
                        #         print("Returned the land in time without fine added!")
                                
                else:
                        print("You havenot rented this land!")

        return kitta_no, returning_land_info,rental_duration,months_late
                              
                       
            