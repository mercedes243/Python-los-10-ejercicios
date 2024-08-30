products_input = input("Enter the products separated by commas: ")

products_list = products_input.split(',')

for product in products_list:
    print(product.strip())
