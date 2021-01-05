products = [] # create a new list

# 2-D list
# insert a list into the first list


while True:
	name = input('Please enter the name of the item: ')
	if name == 'q': # quit
		break
	price = input('Please enter the price of this item: ')
	product = [] # new list
	product.append(name)
	product.append(price)
	# product = [name, price]
	products.append(product)
	# products.append([name, price])

print(products)

for p in products:
	print('The price of', p[0], 'is', p[1], 'dollar!')