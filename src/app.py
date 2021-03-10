import csv 
import datetime as dt

file_name = "/workspace/src/2021-02-23-isle-of-wight.csv"

def read_file(file_name = file_name):
    data = []
    try:
        with open(file_name,'r') as file:
            reader = csv.DictReader(file)
            for line in reader:        
                empty_dict = {'date_time': None, 'location': None, 'customer_name': None, 'products': None, 'payment_method': None, 'total': None, 'card_details': None}
                for key, value in line.items():                    
                        empty_dict[key] = value
                data.append(empty_dict)  
    except Exception as e:
        print('An error occurred when attempting to read the csv file ' + str(e))
    
    return data

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