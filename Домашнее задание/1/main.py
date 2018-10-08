import re
import csv

def get_data():
    global main_data
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1,4):
        file_name = 'info_%s.txt' % i
        file_obj = open(file_name)
        data = file_obj.read()

        # Получаем список изготовителей системы
        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_mas = os_prod_reg.findall(data)
        os_prod_list.append(os_prod_mas[0].split()[2])

        # Название ОС
        os_name_reg = re.compile(r'Windows\s\S*')
        os_name_mas = os_name_reg.findall(data)
        os_name_list.append(os_name_mas[0])

        # Код продукта
        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_mas = os_code_reg.findall(data)
        os_code_list.append(os_code_mas[0].split()[2])

        # Тип системы
        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_mas = os_type_reg.findall(data)
        os_type_list.append(os_type_mas[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    j = 1
    for i in range(0, 3):
        row_data = []
        row_data.append(j)
        row_data.append(os_prod_list[i])
        row_data.append(os_name_list[i])
        row_data.append(os_code_list[i])
        row_data.append(os_type_list[i])
        main_data.append(row_data)
        j = j + 1

def write_to_csv(out_file):
    get_data()
    with open(out_file, 'w') as f:
        writer = csv.writer(f)
        for row in main_data:
            writer.writerow(row)

out_file = 'data_report.csv'
write_to_csv(out_file)




