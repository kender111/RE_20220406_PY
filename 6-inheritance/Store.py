class Product:
    def __init__(self, ti, name, price):
        self.ti = ti
        self.name = name
        self.price = price

class ProductStore(Product):
    def __init__(self):
        self.products  = {}
        self.income = 0

    def add(self, product, amount):
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {'TYPE' : product.ti,  
                                          'price' : product.price,
                                          'amount' : amount}

    def set_discount(identifier, percent, identifier_type='name'):
        if 0 > percent or percent > 100:
            raise ValueError('Некоректне значення знижки')
        
        if identifier_type == 'name':
            if identify in self.products: 
                p = self.products[identify]
                p['price'] = p['price'] * (1 - percent / 100.0)
            else:
                raise ValueError('Не існує ідентифікатора такого типу')
        elif identifier_type == 'type':
            for p in self.products:
                if p['type'] == identify:
                    p['price'] = p['price'] * (1 - percent / 100.0)

    def sell_product(self, product_name, amount):
        if self.products[product_name]['amount'] < amount:
            raise ValueError('Недостатньо товару на складі')
        else:
            self.income +=amount * self.products[product_name]['price']
            self.products[product_name]['amount'] -= amount
            
    def get_income(self):
        return self.income

    def get_all_products(self):
        for p in self.products:
            for n in p:
                print(n, p[n])
        return self.products

    def get_product_info(self, product_name):
        p = self.products[product_name]
        for k in p:
            print(k, p[k])
        return product_name, p['amount']

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.6)

s = ProductStore()


s.add(p, 100)
s.add(p2, 300)



s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)

