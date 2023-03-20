# -*- coding: utf-8 -*-
"""
# Theme: Class,Object and Method 
"""

class Car():
    def __init__(self,model,company,year,price):
        self.model = model
        self.company = company
        self.year = year
        self.price = price
    def get_model(self):
        return self.model
    def get_company(self):
        return self.company
    def get_year(self):
        return self.year
    def get_price(self):
        return self.price
    def info_all(self):
        return f"Model: {self.model}, Company: {self.company}, Year: {self.year}, Price: {self.price}"
    
avto1 = Car("K5","KIA",2009,"$20000")
avto2 = Car("Nexia 2","Chevrolet",2010,"$6000")
avto3 = Car("Vaz 2106","Lada",1995,"$2000")