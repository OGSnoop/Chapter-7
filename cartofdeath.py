class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        self.item_total = (self.item_price * self.item_quantity)
        print('%s %i @ $%i = $%i' % (self.item_name, self.item_quantity, self.item_price, self.item_total))
        
    def print_item_description(self):
        print('%s: %s.' % (self.item_name, self.item_description))

class shoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    def add_item(self, ItemToPurchase):
        self.cart_items.append(self.item_name)
    
    def remove_item(self, name):
        joint = ' '.join(self.cart_items)
        index = joint.find(name)
        if index == -1:
            print('Item not found in cart. Nothing removed.')
        else:
            index = self.cart_items.index(name)
            self.cart_items.pop(index)
    
    def modify_item(self, ItemToPurchase):
        joint = ' '.join(self.cart_items)
        index = joint.find(name)
        if index == -1:
            print('Item not found in cart. Nothing modified.')
        else:
            index = self.cart_items.index(name)
    

if __name__ == "__main__":

    print('Item 1')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item1 = ItemToPurchase(name, price, quantity)
    print() 
    print('Item 2')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item2 = ItemToPurchase(name, price, quantity)
    print()
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print('Total: $%s' % (item1.item_total + item2.item_total))
