class Inventory():
    def __init__(self):
        self.invent = {}

    def addProduct(self, name, quantity=1):
        self.invent[name] = quantity
    
    def removeProduct(self, name):
        if self.searchProduct(name):
            del self.invent[name]
            return True
        else:
            return False
    
    def updateProduct(self, name, quantity):
        if self.searchProduct(name):
            self.invent[name] = quantity
            return True
        else:
            return False
    
    def searchProduct(self, name):
        if name in self.invent:
            return self.invent[name]
        return False

    def printInvent(self):
        if not self.invent:
            print("Empty inventory 😴😴")
        print('''
              ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
''')
        for prod in self.invent:
            print(f"\t\tName : {prod.capitalize()} || Quantity : {self.invent[prod]}")
        print('''
              ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
''')



#MAIN CODE / LOOP RUNS HERE
print('''
      
            Welcome to my world of inventories
      ''')

#Helper functions
def receive(*args):
    ret = []
    for arg in args:
        res = input(f">> Input the {arg} of the product:  ")
        ret.append(res.rstrip().lower())
    return ret if len(ret) > 1 else ret[0]


inventory = Inventory()

while True:

    print('''
    Press 1 to Add item to Inventory
    Press 2 to Remove an item from Inventory
    Press 3 to Update Product quantity
    Press 4 to Search for Product in Inventory
    Press 5 to Explore Inventory
    Press any other keys to exit
''')
    
    res = input(">>>>  ")
    
    if res == "1":
        name, quantity = receive("name", "quantity")
        inventory.addProduct(name, quantity)
        print("Product successfully added to inventory✅\n\n")
    elif res == "2":
        name = receive("name")
        if inventory.removeProduct(name):
            print("Product successfully removed from inventory✅\n\n")
        else:
            print("An error occured while removing product from inventory❌")
    elif res == "3":
        name, quantity = receive("name", "quantity")
        if inventory.updateProduct(name, quantity):
            print("Product successfully updated in inventory✅\n\n")
        else:
            print("An error occured while updating product in inventory❌")
    elif res == "4":
        name = receive("name")
        prod = inventory.searchProduct(name)
        if prod:
            print(f'Product found Name: {name.capitalize()} || Quantity:{prod}')
        else:
            print("Product not available in inventory 😑😑")
    elif res == "5":
        inventory.printInvent()
    else:
        break
    
    