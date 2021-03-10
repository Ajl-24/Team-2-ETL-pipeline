import csv 
import datetime as dt

file_name = "/workspace/src/2021-02-23-isle-of-wight.csv"

def read_file(file_name = file_name):
    data = []
    empty_dict = {'date_time': None, 'location': None, 'customer_name': None, 'products': None, 'payment_method': None, 'total': None, 'card_details': None}
    try:
        with open(file_name, mode = 'r') as file:
            # Opens the csv file of file_name
            field_names = ['date_time', 'location', 'customer_name', 'products', 'payment_method', 'total', 'card_details']
            reader = csv.DictReader(file, fieldnames = field_names)
            for line in reader:        
                data.append(line)            
    except Exception as e:
        print('An error occurred when attempting to read the csv file ' + str(e))
    
    for item in data:
        print(item) 
    # return data

def append_data(csv_line):
    order = [] #Creates temporary list to be appended to data list
    order.append(csv_line[0]) # Date of order
    order.append(csv_line[1]) # Location of order
    order.append(csv_line[2]) # Customer to order
    order.append(csv_line[3]) # Products of order
    order.append(csv_line[4]) # Method of order (i.e. CASH or CARD)
    order.append(float(csv_line[5])) # Total spent at order
    del csv_line[-1] # Personal card details are deleted
    
    return order

csv_data = read_file()