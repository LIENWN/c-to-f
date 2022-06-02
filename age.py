driving = input('你有開過車嗎呵呵?')
if driving != '有' and driving != '沒有':
	print('你只能輸入 有/沒有 掰掰')
	raise SystemExit

age = input('how old are u?')

if driving == '有':
	if int(age) >= 18:
		print('你通過拉！')
	else:
		print('奇怪你怎麼會開過車車')
elif driving == '沒有':
	if int(age) >= 18:
		print('去考駕照吧！')
	else:
		print('過幾年在考吧（再拉幹）')
