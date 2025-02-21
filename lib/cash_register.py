class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0  

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity  
        for _ in range(quantity):
            self.items.append(title)  

    def apply_discount(self):
        if self.discount > 0:
            discount = (self.discount / 100) * self.total
            self.total -= discount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def items_list_without_multiples(self):
        return list(set(self.items))  

    def void_last_transaction(self):
        if self.last_transaction > 0:
            self.total -= self.last_transaction
            self.last_transaction = 0  

          
        

    