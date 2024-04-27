def read():
    try:
        data = []
        column = ['Kitta No.', ' City/District ', ' Land Faced ', ' Anna ', ' Price ', ' Availability ']  
        data.append(column)  # Adding the column headers to the data list.

        file = open('land.txt', 'r')  # Opening the file 'land.txt' in read mode.
        for line in file.readlines():
             data.append(line.rstrip().split(','))  # Parsing each line from the file and appending it to the data list.
        file.close()  # Closing the file after reading.

    
    except FileNotFoundError:
        print(f"Error: File not found!")
        
    return data
