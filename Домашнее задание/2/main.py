import json

def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r') as f_out:
        data = json.load(f_out)
    with open('orders.json', 'w') as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(data, f_in, indent = 4)
        print(data)

write_order_to_json('printer', '1', '6700', 'Ivanov I.I.', '24.09.2017')