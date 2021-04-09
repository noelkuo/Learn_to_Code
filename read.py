# 讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f: 
	for line in f:
		data.append(line) # .strip()
		count += 1 # count = count +1
		if count % 1000 == 0:  # %用來求餘數 1000的倍數
		    print(len(data))

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