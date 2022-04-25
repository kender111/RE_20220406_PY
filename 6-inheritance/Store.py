class Product:
    def __init__(self, ti, name, price):
        self.ti = ti
        self.name = name
        self.price = price

class ProductStore(Product):
    def __init__(self):
        self.storage = {}
'''
    def add(self, Product, anmount):
        self.product = {'TYPE' : Product.ti, 
                        'NAME' : Product.name, 
                        'PRICE' : Product.price,
                        'ANMOUNT' : anmount}
        print(self.product, end = '\n\n\n')

        for i in self.storage.keys():
            temp_v = 0
            if i == id(Product): 

                for ind in self.product.keys():
                    self.product['ANMOUNT'] += self.anmount
                    #print(ind, self.product)

                for ind in self.product.values():
                    self.product['ANMOUNT'] += self.anmount
        else:
            self.storage[Product] = self.product
'''
    def add(self, Product, anmount):
       print(self.product, end = '\n\n\n')
       for i in self.storage.keys():
            temp_v = 0
            if i == id(Product): 
                for ind in self.product.keys():
                    self.product['ANMOUNT'] += self.anmount
                    #print(ind, self.product)

                for ind in self.product.values():
                    self.product['ANMOUNT'] += self.anmount
        else:
             self.product = {'TYPE' : Product.ti, 
                        'NAME' : Product.name, 
                        'PRICE' : Product.price,
                        'ANMOUNT' : anmount}


    def set_discount(identifier, percent, identifier_type='name'):
        pass

    def sell_product(product_name, amount):
        pass

    def get_income(self):
        pass

    def get_all_products(self):
        return self.storage

    def get_product_info(product_name):
        pass

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.6)
p3 = Product('Еда', 'невкусна', 3)
p4 = Product('Шмотка', 'рвана', 2)
s = ProductStore()
#print(p, p2, p3, p4)

s.add(p, 1000)
s.add(p2, 2000)
s.add(p3, 3000)
#s.add(p4, 4000)
s.add(p, 1)
s.add(p2, 2)
s.add(p3, 3)
#s.add(p4, 4)



'''
#s.sell(‘Ramen’, 10)


assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)'''
