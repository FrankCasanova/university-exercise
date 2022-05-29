

products = {

    1: {
        'NAME': 'Super8',
        'PRICE': 400,
        'STOCK': 20
    },

    2: {
        'NAME': 'Oreo',
        'PRICE': 500,
        'STOCK': 20
    },

    3: {
        'NAME': 'Frac',
        'PRICE': 700,
        'STOCK': 20
    },

}


def show_products(products):
    print('\n\n')
    print('{:^20}'.format('PRODUCTS'))
    print('{:^20}'.format('--------'))
    for key, value in products.items():
        print(
            f'id: {key} - Name: {value["NAME"]} - Price: {value["PRICE"]} - Stock: {value["STOCK"]}')


def selection_product(products):
    while True:
        try:
            product_id = int(input('Select product id: '))
            if product_id in products:
                return product_id
            else:
                print('\n\n')
                print('{:^20}'.format('ERROR'))
                print('{:^20}'.format('------'))
                print('\n\n')
                print('Product id not found')
                print('\n\n')
        except ValueError:
            print('\n\n')
            print('{:^20}'.format('ERROR'))
            print('{:^20}'.format('------'))
            print('\n\n')
            print('Product id must be a number')
            print('\n\n')


def buy_a_product(products):
    product_id = selection_product(products)
    product = products[product_id]
    while True:

        product_quantity = int(input('Select product quantity: '))
        if product_quantity <= product['STOCK']:
            money = int(input('Insert money: '))
            if (money * product_quantity) >= product['PRICE']:
                change = money - product['PRICE']
                print('\n\n')
                print('{:^20}'.format('THANK YOU'))
                print('{:^20}'.format('--------'))
                print('\n\n')
                print(f'You bought {product_quantity} {product["NAME"]}')
                print(f'Your change is {change}')
                print('\n\n')
                product['STOCK'] -= product_quantity
                return
            else:
                print('\n\n')
                print('{:^20}'.format('ERROR'))
                print('{:^20}'.format('------'))
                print('\n\n')
                print('You need more money')
                print('\n\n')
        else:
            print('\n\n')
            print('{:^20}'.format('ERROR'))
            print('{:^20}'.format('------'))
            print('\n\n')
            print('Not enough stock')
            print('\n\n')


if __name__ == '__main__':

    sells = 0

    while True:
        print('{:^20}'.format('MAIN MENU'))
        print('{:^20}'.format('--------'))
        print('1 - Show products')
        print('2 - Buy a product')
        print('3 - Exit')
        print('\n\n')
        try:
            option = int(input('Select an option: '))
            if option == 1:
                show_products(products)
            elif option == 2:
                buy_a_product(products)
                sells += 1
            elif option == 3:
                print('Total sells: ', sells)
                break
            else:
                print('\n\n')
                print('{:^20}'.format('ERROR'))
                print('{:^20}'.format('------'))
                print('\n\n')
                print('Option not found')
                print('\n\n')
        except ValueError:
            print('\n\n')
            print('{:^20}'.format('ERROR'))
            print('{:^20}'.format('------'))
            print('\n\n')
            print('Option must be a number')
            print('\n\n')
