from datetime import datetime

def write_rent_bill(kitta_no,customer_name, phone_number, address, rent_invoice,rent_duration):
    rental_date = datetime.now().strftime("%Y-%m-%d")
    total_amount=0
    for x in rent_invoice:  
          total_amount += sum(map(int, x[3].split()))  #calculating the total amount by summing the net price of each land in the invoice.
    vat_amount=total_amount*0.15
    final_amount=total_amount+vat_amount

   
    bill_top=( f"""

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
    
    
    for i in rent_invoice:

        bill_middle=(f"""   
                            {kitta_no} |     {i[0]}     |     {i[1]}     |    {i[2]}    |{rent_duration}months| Rs.{i[3]}   |""")

    bill_bottom=(f"""      
                            -------------------------------------------------------------------------------------------------

                                                                                                    Total Amount:{total_amount}
                                                                                                    VAT(15%):{vat_amount}
                                                                                                    Total Amount with VAT:{final_amount}

                            -------------------------------------------------------------------------------------------------""")
        

    rent_bill=bill_top+bill_middle+bill_bottom
    print(rent_bill)
    rent_file=open(f"Rented By {customer_name}.txt","w")
    rent_file.write(rent_bill)
    

def write_return_bill(customer_name, phone_number, address,months_late, return_invoice,selected_land_info,rent_duration):
    return_date=datetime.now().strftime("%Y-%m-%d")
    


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
    



    