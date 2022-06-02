i = 3 #剩餘機會
while i > 0:
	i = i - 1
	passwd = input('請輸入密碼:')
	if passwd == 'a123456':
		print('登入成功!')
		break
	else:
		print('密碼錯誤!')
		if i > 0:
			print('還有', i,'次機會')
		else:
			print('不要亂登入哦!')
