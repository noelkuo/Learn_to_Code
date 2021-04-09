# 讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f: 
	for line in f:
		data.append(line.strip())
		count += 1 # count = count +1
		if count % 1000 == 0:  # %用來求餘數 1000的倍數
		    print(len(data))


print(len(data))

# print(data)
print(data[0]) 
print('---------------------')
print(data[1])
