password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會') # i: 變數
		print('無法登入')