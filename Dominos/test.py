import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pizzapi-master'))

from pizzapi import *

if __name__ == "__main__":
    mode = sys.argv[1].lower()
    items = sys.argv[2:]
    
    who = Customer('Small', 'Foot', 'smallfoot@osiris.cyber.nyu.edu')
    where_to = Address('370 Jay St', 'Brooklyn', 'NY', '11201')
    where_from = where_to.closest_store()

    menu = where_from.get_menu()
    
    if mode in ('l', 'list'):
        print(menu.display())
    
    elif mode in ('s', 'search'):
        for item in items:
            print('?q=' + item)
            menu.search(Name=item)
    
    elif mode in ('o', 'order'):
        order = Order(store=where_from, customer=who, address=where_to)
        
        for i in range(0, len(items), 2):
            if items[i] == 'i':
                order.add_item(items[i + 1])
            elif items[i] == 'c':
                order.add_coupon(items[i + 1])
        
        # for item in items:
        #     order.add_item(item)
        
        # print("Enter in credit card details")
        # credit.number = input('Number:')
        # credit.expiration = input('Expiration Date:')
        # credit.cvv = input('CVV:')
        # credit.zip = input('Zip:')
        # number = input('Number:')
        # expiration = input('Expiration Date:')
        # cvv = input('CVV:')
        # zip = input('Zip:')
        credit = PaymentObject('1234567890123456', '0123', '012', '01234')
        result = order.pay_with(credit)
        
        print(result['Status'] == 1)
        result.pop('Order')
        print(result)

