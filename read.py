# 讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f: 
	for line in f:
		data.append(line.strip())
		count += 1 # count = count +1
		if count % 1000 == 0:  # %用來求餘數 1000的倍數
		    print(len(data))
		    
### 計算留言的平均長度

sum_len = 0
for i in data:
	sum_len = sum_len + len(i)
	print(sum_len)

print('檔案讀取完了，總共有', len(data), '筆資料')
print('留言的平均長度是', sum_len/len(data))