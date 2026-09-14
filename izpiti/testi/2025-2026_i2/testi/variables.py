shop5 = [('F', 'Outerwear', 'Coat', 'M', 75, 4.8),
 ('M', 'Clothing', 'Shirt', 'XL', 76, 4.7),
 ('F', 'Clothing', 'Socks', 'M', 43, 3.6),
 ('M', 'Accessories', 'Hat', 'M', 45, 4.4),
 ('F', 'Clothing', 'T-shirt', 'M', 57, 2.8)]

shop10 = [('M', 'Footwear', 'Sneakers', 'M', 20, 2.9),
 ('F', 'Clothing', 'Socks', 'L', 41, 4.3),
 ('M', 'Clothing', 'Sweater', 'L', 85, 3.7),
 ('M', 'Accessories', 'Gloves', 'M', 71, 3.2),
 ('M', 'Clothing', 'T-shirt', 'L', 31, 4.8),
 ('F', 'Outerwear', 'Jacket', 'M', 81, 3.3),
 ('F', 'Accessories', 'Sunglasses', 'L', 38, 3.5),
 ('F', 'Clothing', 'Sweater', 'M', 26, 4.8)]

shop20 = [('M', 'Accessories', 'Scarf', 'L', 39, 3.7),
 ('M', 'Clothing', 'Shirt', 'M', 40, 3.5),
 ('F', 'Clothing', 'Pants', 'M', 20, 4.5),
 ('F', 'Accessories', 'Handbag', 'L', 57, 2.7),
 ('M', 'Footwear', 'Shoes', 'M', 48, 2.9),
 ('M', 'Accessories', 'Jewelry', 'S', 81, 4.2),
 ('M', 'Clothing', 'Pants', 'L', 52, 3.5),
 ('F', 'Accessories', 'Gloves', 'L', 93, 4.4),
 ('F', 'Clothing', 'Blouse', 'M', 83, 3.2),
 ('F', 'Clothing', 'Socks', 'L', 37, 3.3),
 ('F', 'Clothing', 'Skirt', 'L', 90, 2.9),
 ('F', 'Clothing', 'Shirt', 'M', 79, 2.5),
 ('M', 'Footwear', 'Boots', 'M', 25, 3.9),
 ('M', 'Accessories', 'Backpack', 'L', 75, 3.1),
 ('M', 'Accessories', 'Jewelry', 'M', 74, 3.6)]

shop30 = [('M', 'Footwear', 'Boots', 'L', 21, 2.7),
 ('M', 'Clothing', 'T-shirt', 'L', 95, 3.4),
 ('F', 'Outerwear', 'Coat', 'S', 76, 3.6),
 ('F', 'Clothing', 'Blouse', 'M', 25, 2.6),
 ('F', 'Accessories', 'Handbag', 'S', 33, 4.9),
 ('M', 'Footwear', 'Shoes', 'L', 20, 2.6),
 ('M', 'Accessories', 'Backpack', 'XL', 37, 4.1),
 ('M', 'Accessories', 'Sunglasses', 'M', 85, 3.1),
 ('M', 'Accessories', 'Hat', 'M', 96, 3.4),
 ('M', 'Clothing', 'Shirt', 'M', 40, 2.6),
 ('M', 'Footwear', 'Shoes', 'L', 89, 4.6),
 ('M', 'Footwear', 'Shoes', 'M', 26, 4.2),
 ('M', 'Footwear', 'Boots', 'XL', 52, 3.0),
 ('M', 'Clothing', 'Socks', 'L', 35, 4.2),
 ('F', 'Clothing', 'Sweater', 'M', 79, 3.0),
 ('F', 'Clothing', 'Jeans', 'S', 91, 4.1),
 ('M', 'Clothing', 'Skirt', 'L', 25, 4.0),
 ('M', 'Clothing', 'Sweater', 'M', 68, 2.6),
 ('F', 'Footwear', 'Shoes', 'S', 74, 4.8),
 ('F', 'Clothing', 'Jeans', 'M', 60, 3.5),
 ('F', 'Clothing', 'Hoodie', 'M', 88, 3.1),
 ('F', 'Accessories', 'Jewelry', 'L', 74, 4.4)]

slovar5 = {'F': ['Outerwear', 'Clothing', 'Clothing'], 'M': ['Clothing', 'Accessories']}

slovar10 = {'M': ['Footwear', 'Clothing', 'Accessories', 'Clothing'],
 'F': ['Clothing', 'Outerwear', 'Accessories', 'Clothing']}

slovar20 = {'Accessories': ['Scarf', 'Handbag','Jewelry','Gloves','Backpack','Jewelry'],
 'Clothing': ['Shirt', 'Pants', 'Pants', 'Blouse', 'Socks', 'Skirt', 'Shirt'],
 'Footwear': ['Shoes', 'Boots']}

slovar30 = {21: ['Boots'],
 95: ['T-shirt'],
 76: ['Coat'],
 25: ['Blouse', 'Skirt'],
 33: ['Handbag'],
 20: ['Shoes'],
 37: ['Backpack'],
 85: ['Sunglasses'],
 96: ['Hat'],
 40: ['Shirt'],
 89: ['Shoes'],
 26: ['Shoes'],
 52: ['Boots'],
 35: ['Socks'],
 79: ['Sweater'],
 91: ['Jeans'],
 68: ['Sweater'],
 74: ['Shoes', 'Jewelry'],
 60: ['Jeans'],
 88: ['Hoodie']}

slovar30_1 = {'L': ['Boots', 'T-shirt', 'Shoes', 'Shoes', 'Socks', 'Skirt', 'Jewelry'],
 'S': ['Coat', 'Handbag', 'Jeans', 'Shoes'],
 'M': ['Blouse','Sunglasses','Hat','Shirt','Shoes','Sweater','Sweater','Jeans', 'Hoodie'],
 'XL': ['Backpack', 'Boots']}

naj_slovar10 = {'M': ['Footwear', 'Clothing', 'Accessories', 'Clothing'],
 'F': ['Clothing', 'Outerwear', 'Accessories', 'Clothing', 'Accessories']}

naj10 = ('F', ['Clothing', 'Outerwear', 'Accessories', 'Clothing', 'Accessories'])

naj20 = ('Clothing', ['Shirt', 'Pants', 'Pants', 'Blouse', 'Socks', 'Skirt', 'Shirt'])

naj30 = (25, ['Blouse', 'Skirt'])