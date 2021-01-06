# check the file if it is exist
import os # operating system

products = []
if os.path.isfile('products_price.csv'): # check the file if is existent isfile()
	print('The file is existent!')
	# products = [] # create a new list
	with open('products_price.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'Items, Price' in line:
				continue # jump to next loop
					 
			name, price = line.strip().split(',') # split to cut the line use everything
			# use strip to remove '\n'
			# From left to right
			# After split will generate a list []
			# name = s[0]
			# price = s[1]
			products.append([name, price])

	print(products)
else:
	print('The file is nonexistent!')



# read file
# products = [] # create a new list

# with open('products_price.csv', 'r', encoding = 'utf-8') as f:
	# for line in f:
	#	if 'Items, Price' in line:
	#		continue # jump to next loop
					 
	#	name, price = line.strip().split(',') # split to cut the line use everything
		# use strip to remove '\n'
		# From left to right
		# After split will generate a list []
		# name = s[0]
		# price = s[1]
	#	products.append([name, price])

#print(products)

# 2-D list
# insert a list into the first list

# input import
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

# print each record
for p in products:
	print('The price of', p[0], 'is', p[1], 'dollar!')


# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# write in csv file
# with open('products_price.txt', 'w') as f:
with open('products_price.csv', 'w', encoding = 'utf-8') as f:
	f.write('Items, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # f.write: write function

# Can not plus integer to string use str() and int()
# use encoding = utf - 8 can write chinese *****








