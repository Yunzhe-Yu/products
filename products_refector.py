import os

# Read file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				if 'Items, Price' in line:
					continue
				name,price = line.strip().split(',')
				products.append([name, price])
	print(products)
	return products

# User input
def user_input(products):
	while True:
		name = input('Please type the name of this item:')
		if name == 'q':
			break
		price = input('Please enter the price of the item:')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

# Print file
def print_product(products):
	for p in products:
		print('The price of', p[0], 'is', p[1], 'dollars!')

# Write file
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('Items, Price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

# Main function
def main():
	filename = 'products.csv'

	if os.path.isfile(filename):
		print('The file is exist!')
		products = read_file(filename)
	else:
		print('Cannot find this file!')

	products = user_input(products)

	print_product(products)

	write_file(filename, products)

main()

#Refector

# Using function

# if os.path.isfile(filename):
# 	print('The file is exist!')
# 	products = read_file('products.csv')
# else:
# 	print('Cannot find this file!')

# products = user_input(products)

# print_product(products)

# write_file('products.csv', products)
