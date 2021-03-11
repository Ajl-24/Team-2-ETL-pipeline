import csv 
import transform as tf


file_name = "/workspace/src/2021-02-23-isle-of-wight.csv"

def read_file(file_name = file_name):
    data = []
    #empty_dict = {'date_time': None, 'location': None, 'customer_name': None, 'products': None, 'payment_method': None, 'total': None, 'card_details': None}
    try:
        with open(file_name, mode = 'r') as file:
            # Opens the csv file of file_name
            field_names = ['date_time', 'location', 'customer_name', 'products', 'payment_method', 'total', 'card_details']
            reader = csv.DictReader(file, fieldnames = field_names)
            data = append_to_list(reader,data)
    except Exception as e:
        print('An error occurred when attempting to read the csv file ' + str(e))
        return
    return data

def append_to_list(reader,cached_list):
    for line in reader:
        cached_list.append(dict(line))    
    return cached_list

csv_data = read_file()

iow_data = tf.Transform(csv_data)

# print("Is it working?")
# print(iow_data.data[0])
# iow_data.remove_names()
# print(iow_data.data[0])
# iow_data.remove_card_details()
# print(iow_data.data[0])

