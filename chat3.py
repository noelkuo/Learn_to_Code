
lines = []
with open('Line2.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ') #先處理空格
	# 時間長度是固定的
	time = s[0][:5]
	name = s[0][5:]
	print(name)