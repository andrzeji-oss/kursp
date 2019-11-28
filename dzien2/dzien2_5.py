#slowniki

products={}
# dodawanie nowego produktu

products["0x111"] = "Pamięć RAM 8 GB"
products["0x112"] = "Pamięć  RAM 16 GB"
products["0x222"] = [1,"PC", "Intel i5 8gen, 700"]
products[None] = "xxx"

# modyfikacja pamięci ram
products["0x112"] += " NEW"
print(products)
print(products.keys())
print(products.values())