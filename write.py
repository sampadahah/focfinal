from datetime import datetime

def write_rent_bill(kitta_no,customer_name, phone_number, address, rent_invoice,rent_duration):
    rental_date = datetime.now().strftime("%Y-%m-%d")
    rental_time=datetime.now().strftime("%H:%M:%S")
    total_amount=0
    for x in rent_invoice:  
          total_amount +=  int(x[4]) #calculating the total amount by summing the net price of each land in the invoice.
    vat_amount=total_amount*0.15
    final_amount=total_amount+vat_amount

   
    bill_top=( f"""

                                                                  Techno Property Nepal                                       
                                                                  Malepatan-5, Pokhara
                            ------------------------------------------------------------------------------------------------
                            Name:{customer_name}                                                             Rental Date:{rental_date}                        
                            Contact Number:{phone_number}                                                    Rental Time:{rental_time}
                            Address:{address}
                            ------------------------------------------------------------------------------------------------
                               Kitta No.  |  City/District  |   Land Faced   |   Anna   |  Rental Duration  |    Price     |
                            ------------------------------------------------------------------------------------------------""")
    
  
    bill_middle=""
    for land_info in rent_invoice:
        kitta_no,location, direction, anna, price = land_info

        kitta_no=land_info[0]
        location = land_info[1]
        direction = land_info[2]
        anna = land_info[3]
        price = land_info[4]

        bill_middle +=(f"""
                            {str(kitta_no):^13} |{location:^17}|{direction:^16}|{str(anna):^10}|{str(rent_duration) + ' months':^19}| {'Rs.'+str(price):^13}|""")

    bill_bottom=(f"""      
                            ------------------------------------------------------------------------------------------------

                                                                                         Total Amount:{total_amount}
                                                                                         VAT(15%):{vat_amount}
                                                                                         Total Amount with VAT:{final_amount}

                            ------------------------------------------------------------------------------------------------""")
        

    rent_bill=bill_top+bill_middle+bill_bottom
    print(rent_bill)
    rent_file=open(f"Rented By {customer_name}.txt","w")
    rent_file.write(rent_bill)
    return(rent_bill)
    

def write_return_bill(customer_name, phone_number, address, return_invoice,rent_duration,fine):
    return_date=datetime.now().strftime("%Y-%m-%d")
    
    total_amount=0
    for x in return_invoice:  
          total_amount += sum(map(int, x[3].split()))  #calculating the total amount by summing the net price of each land in the invoice.
    vat_amount=total_amount*0.15
    if fine<0:
        final_amount=total_amount+vat_amount+fine
    else:
        final_amount=total_amount+vat_amount


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
                       
    billMiddle=f"""
                        {kitta_no} |{locations}|{selected_land_info[2]}|{selected_land_info[3]}|{[rent_duration]}| {selected_land_info[4]}"""

    billButtom = f"""-------------------------------------------------------------------------------------------------

                                                                                Fined Months:{months_late}
                                                                                Fine Amount:{fine}
                                                                                Total Amount:{total_price}
                                                                                VAT(15%):{total_vat}
                                                                                Total Amount with VAT:{final_amount}
                                                                                Total amount for all returned land:{ultimate_total}

                         -----------------------------------------------------------------------------------------------"""
        

    return_bill=billTop+billMiddle+billButtom
    print(return_bill)
    return_file=open(f"Returned By {customer_name}.txt","w")
    return_file.write(return_bill)
    



    