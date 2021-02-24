line1 = []
Allen = 0
Viki = 0
Allen_s = 0
Viki_s = 0
Allen_i = 0
Viki_i = 0
with open('LINE-Viki.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		line1 = line.strip().split(' ')
		if 'Allen' in line1:
			if line1[2] == '貼圖':
				Allen_s += 1
			elif line1[2] == '圖片':
				Allen_i += 1
			else:
				for s in line1[2:]:
					Allen += len(s)
		elif 'Viki' in line1:
			if line1[2] == '貼圖':
				Viki_s += 1
			elif line1[2] == '圖片':
				Viki_i += 1
			else:
				for s in line1[2:]:
					Viki += len(s)
print('Allen说话长度为：', Allen, '贴图数为', Allen_s, '图片数为', Allen_i)
print('Viki说话长度为：', Viki, '贴图数为', Viki_s, '图片数为', Viki_i)



		
