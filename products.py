products = [] # create a new list

# 2-D list
# insert a list into the first list


while True:
	name = input('Please enter the name of the item: ')
	if name == 'q': # quit
		break
	price = input('Please enter the price of this item: ')
	price = int(price)
	product = [] # new list
	product.append(name)
	product.append(price)
	# product = [name, price]
	products.append(product)
	# products.append([name, price])

print(products)

for p in products:
	print('The price of', p[0], 'is', p[1], 'dollar!')


# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# with open('products_price.txt', 'w') as f:
with open('products_price.csv', 'w', encoding = 'utf-8') as f:
	f.write('Items, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # f.write: write function

# Can not plus integer to string use str() and int()
# use encoding = utf - 8 can write chinese *****








