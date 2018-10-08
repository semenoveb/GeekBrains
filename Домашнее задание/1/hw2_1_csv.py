import csv

def get_data(filenames = ['info_1.txt', 'info_2.txt', 'info_3.txt']):
	os_prod_list = list()
	os_name_list = list()
	os_code_list = list()
	os_type_list = list()
	main_data = []
	header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
	for filename in filenames:
		with open(filename, 'r', encoding = 'cp1251') as fh:
			for line in fh:
				if header[0] in line:
					line = ' '.join(line.split())
					line = line.split(':')[1].strip()
					os_prod_list.append(line)
				elif header[1] in line:
					line = ' '.join(line.split())
					line = line.split(':')[1].strip()
					os_name_list.append(line)
				elif header[2] in line:
					line = ' '.join(line.split())
					line = line.split(':')[1].strip()
					os_code_list.append(line)
				elif header[3] in line:
					line = ' '.join(line.split())
					line = line.split(':')[1].strip()
					os_type_list.append(line)
		# print(os_prod_list, ' -- ', os_name_list, ' -- ', os_code_list, \
		# ' -- ', os_type_list)
	[main_data.append(data) for data in [header, os_prod_list, os_name_list, os_code_list, os_type_list]]
	print(main_data)
	return main_data

	# return (os_prod_list, os_name_list, os_code_list, os_type_list)
def write_to_csv(main_data:list):
	with open('data_report_home.csv', 'w') as fh:
		writer = csv.writer(fh)
		index = 0
		for row in main_data:
			if index > 0:
				row.insert(0, index)
			writer.writerow(row)
			index += 1
	print('Writing complete.')

def main():
	main_data = get_data()
	write_to_csv(main_data)

if __name__ == '__main__':
	main()
