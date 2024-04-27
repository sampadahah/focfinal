from datetime import datetime


def write_rent_bill(customer_name, phone_number, address, land_info, ultimate_total):
    rental_date = datetime.now().strftime("%Y-%m-%d")
    rent_bill_file = open( f"Rented By {customer_name}.txt","w") 
    # for info in land_info:
    #     kitta_no, locations, rent_duration, price= info
    #     total_price, total_vat, final_amount = price


    # with open(f"Rented By {customer_name}.txt", "w") as rent_bill_file:
    rent_bill_file.write( f"""

                                                             Techno Property Nepal
                                                             Malepatan-5, Pokhara
                            ------------------------------------------------------------------------------------------------
                            Name:{customer_name}                                                  
                            Contact Number:{phone_number}
                            Address:{address}
                            Date:{rental_date}

                            -------------------------------------------------------------------------------------------------
                            Kitta No.  | City/District  | Land Faced     | Anna         | Rental Duration    | Price        |
                            -------------------------------------------------------------------------------------------------""")
    
    for info in land_info:
        kitta_no, city, land_faced, anna, rent_duration, price= info
        total_price, total_vat, final_amount = price

        rent_bill_file.write(f"""{kitta_no}|{city}|{land_faced}|{anna}|{[rent_duration]}| Rs.{price}""")

        rent_bill_file.write(f"""-------------------------------------------------------------------------------------

                         Total Amount:{total_price}
                         VAT(15%):{total_vat}
                         Total Amount with VAT:{final_amount}
                         Total amount for all selected land:{ultimate_total}

                         -------------------------------------------------------------------------------------""")
        
        
        
    


        # rent_bill_file.write("Rental Bill\n\n")
        # rent_bill_file.write(f"Date and Time: {date_time}\n")
        # rent_bill_file.write(f"Customer Name: {username}\n")
        # rent_bill_file.write(f"Phone Number: {phone_number}\n")
        # rent_bill_file.write(f"Address: {address}\n")

        # bill_file.write("\nVenue Details\n")
        # for info in venues_info:
        #     kitta_no, locations, rental_periods, prices = info
        #     total_price, total_vat, final_amount = prices

        #     bill_file.write(f"Kitta No.: {', '.join(kitta_no)}\n")
        #     bill_file.write(f"Location: {', '.join(locations)}\n")
        #     bill_file.write(
        #         f"Rental Period: {', '.join(str(period) for period in rental_periods)} months\n"
        #     )
        #     bill_file.write(
        #         f"Price (excluding VAT): Rs.{', '.join(str(price) for price in total_price)}\n"
        #     )
        #     bill_file.write(f"VAT (15%): Rs.{total_vat}\n")
        #     bill_file.write(f"Final Amount (including VAT): Rs.{final_amount}\n")
        #     bill_file.write("\n")

        # bill_file.write(
        #     f"Ultimate Total (including VAT) for all venues: Rs.{ultimate_total}\n"
        # )


write_rent_bill()
def write_return_bill(customer_name, phone_number, address,months_late, land_info, ultimate_total,selected_land_info,rent_duration):
    return_date=datetime.now().strftime("%Y-%m-%d")
    kitta_no, locations, rent_duration, amount = land_info
    total_price, total_vat, final_amount,fine = amount


    # with open(f"Rented By {customer_name}.txt", "w") as rent_bill_file:
    billTop = f"""

                                                        Techno Property Nepal
                                                         Malepatan-5, Pokhara
                        +----------------------------------------------------------------------------------+
                        Name:{customer_name}                                                  
                        Contact Number:{phone_number}
                        Address:{address}
                        Date:{return_date}

                        -------------------------------------------------------------------------------------------------
                        Kitta No.  | City/District  | Land Faced     | Anna         | Rental Duration    | Price        |
                        -------------------------------------------------------------------------------------------------"""
                       
    billMiddle=f"""{kitta_no}|{locations}|{selected_land_info[2]}|{selected_land_info[3]}|{[rent_duration]}| {selected_land_info[4]}"""

    billButtom = f"""-------------------------------------------------------------------------------------

                         Fined Months:{months_late}
                         Fine Amount:{fine}
                         Total Amount:{total_price}
                         VAT(15%):{total_vat}
                         Total Amount with VAT:{final_amount}
                         Total amount for all returned land:{ultimate_total}

                         -------------------------------------------------------------------------------------"""
        
    bill=billTop+billMiddle+billButtom

    return_file=open(f"Returned By {customer_name}.txt","w")
    return_file.write(bill)
    return_file.close()



    