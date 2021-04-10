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
print(products[0]) # 大清單的第一格
print(products[0][0]) # 大清單中的第一格 --> 小清單的第一格