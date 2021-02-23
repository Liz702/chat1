
def read_and_change_file(filename, output1):
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'Allen' in line:
				person = 'Allen'
				continue
			elif 'Tom' in line:
				person = 'Tom'
				continue
			output1.append(person + ': ' +line.strip())

def write_file(filename, output1):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for output in output1:
			f.write(output + '\n')
def main():
	output1 = []
	read_and_change_file('input.txt', output1)
	print(output1)
	write_file('output1.txt', output1)
main()

