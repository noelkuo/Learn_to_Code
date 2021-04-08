password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	else:
		print('密碼錯誤!') # i: 變數
		if i > 0:
			print('還有', i, '次機會') # i: 變數
		else:
			print('無法登入')