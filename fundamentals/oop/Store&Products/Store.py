class Store:
    
    def __init__(self,name="FarmHouse",product_list=None):
        self.name=name
        if product_list is None:
            self.product_list=[]
        else:
            self.product_list=product_list
    def add_product(self,new_product):
        self.product_list.append(new_product)
    
    def sell_product(self,id):
        print(self.product_list[id].name)
        self.product_list.remove(self.product_list[id])
    def inflation(self, percent_increase):
        for a in self.product_list:
            a.update_price(percent_increase,True)
    def set_clearance(self,category,percent_discount):
        for a in self.product_list:
            if a.category==category: 
                a.update_price(percent_discount,False)

class Product:
    def __init__(self, name, price, category):
        self.name=name
        self.price=price
        self.category=category

    def update_price(self, percent_change, is_increased):
        if is_increased==True:
            self.price = self.price*(1+percent_change)
            return self.price
        else:
            self.price = self.price*(1-percent_change)
            return self.price
    def print_info(self):
        print(f'name: {self.name}  category: {self.category}  price: {self.price}')

Dublin=Store()

Apple=Product('apple',10,"fruit")
Banana=Product('banana',5,"fruit")
Strawberry=Product('strawberry',3,"fruit")
Lettuce=Product('lettuce',4,"vegetable")
Dublin.add_product(Apple)
Dublin.add_product(Banana)
Dublin.add_product(Strawberry)
Dublin.add_product(Lettuce)
print(Dublin.product_list)
# Dublin.inflation(0.1)
Dublin.set_clearance('fruit',0.5)

# Apple.update_price(0.05,True)
# Banana.update_price(0.05,False)
print(Apple.price)
print(Banana.price)
print(Strawberry.price)
print(Lettuce.price)
