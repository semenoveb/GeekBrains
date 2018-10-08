import json, datetime


def write_order_to_json(orders:list):
	with open('orders_new.json', 'w') as fh:
		json.dump(orders, fh, indent = 4, ensure_ascii = False)
	return print('Запись заказа закончена.')

def main():
	orders = list()
	print('Заполните форму заказа.')
	while True:
		item = input('введите товар:')
		if len(item) < 4:
			continue

		try:	
			quantity = int(input('введите количество:'))
			price = float(input('введите цену: '))
		except:
			print('Вы ввели неверные значения, ещё раз!!!')
			continue

		buyer = input('введите ФИО покупателя: ')
		if buyer == None or len(buyer) < 3:
			continue
		
		date_order = datetime.date.today().strftime("%d-%m-%Y")
		
		order = {'item':item,'quantity': quantity, 'price': price, \
			'buyer': buyer, 'date': date_order}
		orders.append(order)

		answer = input('Продолжить? (y/n): ')
		if answer == 'n' or answer == 'N':
			break
	write_order_to_json(orders)

if __name__ == '__main__':
	main()