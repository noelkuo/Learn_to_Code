products = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # exit
		break
	price = input('請輸入商品價格: ')
	price = int(price) # 轉成整數 非字串

	products.append([name, price])

print(products)

for p in products:
	# print(p) # 個別清單
	# print(p[0]) # 清單的商品名
	print(p[0], '的價格是', p[1], '元') # 清單的商品名


## 檔案儲存
with open('products.csv', 'w', encoding='utf-8') as f: # 無解
	f.write('商品,價格 \n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # str 將數字改成字串
