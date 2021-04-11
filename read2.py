# 讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f: 
	for line in f:
		data.append(line) # .strip()
		count += 1 # count = count +1
		if count % 1000 == 0:  # %用來求餘數 1000的倍數
		    print(len(data))
print('檔案讀取完了，總共有', len(data), '筆留言')

### 計算留言的平均長度
sum_len = 0
for i in data:
	sum_len = sum_len + len(i)
	print(sum_len)

print('檔案讀取完了，總共有', len(data), '筆留言')
print('留言的平均長度是', sum_len/len(data))

# 查詢哪些留言小於100個字 -- 篩選
new = []
for j in data:
	if len(j) < 100:
		new.append(j)

print('一共有', len(new), '筆留言長度小於100')
print(new[0])

# 查詢哪些留言有包含 'good' -- 篩選
good = []
for k in data:
	if 'good' in k:
		good.append(k)

print('一共有', len(good), '筆留言包含 good')

# 文字計數
wc = {} # word_count
for d in data:
	words = d.split() # split 預測值是空白鍵
	# break
	for word in words:
		# 檢查字是否有出現過
		if word in wc:
			wc[word] += 1 # 累加出現key的次數
		else:
			wc[word] = 1 # 新增新的key進入 wc 

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	# print(word, '出現過的次數為： ', wc[word])
	if word in wc:
		print(word, '出現過的次數為： ', wc[word])
	else:
		print('這個字沒有出現過!')

print('感謝使用本查詢功能')







 

