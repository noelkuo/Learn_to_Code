products = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # exit
		break
	price = input('請輸入商品價格: ')
	# p = []
	# p.append(name)
	# p.append(price)

	# p = [name, price]
	# products.append(p)

	products.append([name, price])

print(products)

for p in products:
	# print(p) # 個別清單
	# print(p[0]) # 清單的商品名
	print(p[0], '的價格是', p[1], '元') # 清單的商品名
