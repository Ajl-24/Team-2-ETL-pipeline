class Transform:
    
    def __init__(self, data):
        self.data = data
        
    def remove_names(self):        
        for order_dict in self.data:
            del order_dict['customer_name']
            
    def remove_card_details(self):
        for order_dict in self.data:
            del order_dict['card_details']         
    