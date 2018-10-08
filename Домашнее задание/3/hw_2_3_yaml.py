import yaml
from pprint import pprint

def read_yaml(filename:str):
	with open(filename) as fh:
		readed_file = yaml.load(fh)
	pprint(readed_file)
	return readed_file


def main():
	readed_file = read_yaml('file.yaml')

	with open('file_writed.yaml', 'w') as fh:
		yaml.dump(readed_file, fh, default_flow_style = False, allow_unicode = True)

	readed_file_again = read_yaml('file_writed.yaml')
	
	# Данный способ сравнения подсмотрел у Вас, Андрей.
	print(readed_file == readed_file_again)

if __name__ == '__main__':
	main()