class Transform:
    
    def __init__(self, data):
        self.raw_data = data
        self.data = data
        
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
            self.data.append(temp_dict) # Append dictionary

    def split_products(self):
        for index, order_dict in enumerate(self.data):
            if order_dict['products'].count(',') > 2:                
                order_to_split = self.data.pop(index)
                thing = self.seperate_string(order_to_split)
                                