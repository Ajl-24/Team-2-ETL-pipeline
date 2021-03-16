class Transform:
    
    def __init__(self, data):
        self.raw_data = data
        self.data = data
        self.split_data = []
        
    def remove_names(self):        
        for order_dict in self.data:
            del order_dict['customer_name']
            
    def remove_payment_details(self):
        for order_dict in self.data:
            del order_dict['payment_method']
            del order_dict['card_details']         
    
    def add_id(self):
        for index, order_dict in enumerate(self.data):
            order_dict['id'] = index
    
    def sort_by_id(self):
        sorted_list = sorted(self.data, key = lambda k: k['id'])
        self.data = sorted_list
    
    def seperate_string(self, order_dict):
        products_to_split = order_dict['products']        
        list_products = products_to_split.split(',')        
        for index in range(0, len(list_products), 3):
            temp_dict = order_dict.copy() # Makes a COPY of the original dictionary
            temp_product = list_products[index:(index + 3)] # Asigns relevant information of single product to list 
            string_product = ",".join(temp_product) # Casts list to a string to maintian format 
            temp_dict['products'] = string_product # Overwrites value held at 'products' key into copy of order dictionary
            self.data.append(temp_dict) # Inserts into the same index of the original dictionary in the list   

    def split_products(self):
        data_copy = self.data.copy()
        self.data = []
        
        for index in range(len(data_copy)):                      
            product_list = data_copy[index]['products'].split(',')
            if len(product_list) > 3:                
                order_to_split = data_copy[index]
                thing = self.seperate_string(order_to_split)
            else:
                self.data.append(data_copy[index])
                
    def split_product_price(self):
        for order_dict in self.data:
            product_string =  order_dict['products']
            product_details = product_string.split(',')
            order_dict['product_price'] = product_details[-1]
            if product_details[0] == "":
                order_dict['product'] = product_details[1]
                del order_dict['products']
            else:
                order_dict['product'] = product_details [0] + ' ' + product_details[1]
                del order_dict['products']
                
    def split_date_time(self):
        for order_dict in self.data:
            order_date_time = order_dict['date_time'].split(' ')
            del order_dict['date_time']
            order_dict['date'] = order_date_time[0]
            order_dict['time'] = order_date_time[1]