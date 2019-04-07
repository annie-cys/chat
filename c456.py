def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines #回傳出來

def convert(lines):
	new = []
	person = None # 虛無
	for line in lines: # 把清單一個一個叫出來
		if line == 'Allen':
			person = 'Allen'
			continue # 跳到下一個迴圈 line = 下一行
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person : # Person 友直
			new.append(person + ' : ' + line )
	return new
def write_file(filename, lines):
	with open (filename, 'w', encoding='utf-8-sig') as f:
		for line in lines: # 一行一行讀取
			f.write(line + '\n') # 寫入


def main():
	lines = read_file('input.txt') #因有回傳 固可處存
	lines = convert(lines) #取代
	write_file('output.txt', lines)



main()