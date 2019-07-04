
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip()) # 不換行


for line in lines:
	s = line.split(' ') #切完變清單
	name = s[0][5:] #字串可以當清單 #5 取前五個 01234 不包含5
	time = s[0][:5]
	print(name)