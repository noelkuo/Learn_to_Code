import random

r = random.randint(1, 100)

while True:
	num = input('請猜數字： ')
	num = int(num)
	if num == r:
		print("恭喜猜對了!")
		break
	elif num > r:
		print("數字太大了!")
	elif num < r:
		print("數字太小了!")



