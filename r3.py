def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip()) #strip 去換行符號
	return lines #回傳出來

def convert(lines):
	person = None # 虛無
	allen_word_count = 0
	allen_sticker_count = 0
	allen_pic_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_pic_count = 0
	for line in lines: # 把清單一個一個叫出來
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_pic_count += 1
			else:
				for m in s[2:]:
					allen_word_count +=	len(m)
		elif name ==  'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_pic_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen說了', allen_word_count, '個字, 傳了' , allen_sticker_count, '個貼圖', '傳了' , allen_pic_count, '個圖片')
	print('viki說了', viki_word_count, '個字, 傳了' , viki_sticker_count, '個貼圖', '傳了' , viki_pic_count, '個圖片')


def write_file(filename, lines):
	with open (filename, 'w', encoding='utf-8-sig') as f:
		for line in lines: # 一行一行讀取
			f.write(line + '\n') # 寫入


def main():
	lines = read_file('-LINE-Viki.txt') #因有回傳 固可處存
	lines = convert(lines) #取代
	#write_file('output.txt', lines)



main()