import yaml

data_in = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
        'items_quantity': 4,
        'items_ptice': {'computer': '200€-1000€',
                       'printer': '100€-300€',
                       'keyboard': '5€-50€',
                       'mouse': '4€-7€'}
        }

with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(data_in, f_in, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as f_out:
    data_out = yaml.load(f_out)

print(data_in == data_out)