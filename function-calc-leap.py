#參數設為0，使程式不填參數可進入while圈
def is_leap(year=0):
	while True:	
		year = input('請輸入您想查詢是否為閏年或平年的年份： ')
		year = int(year)		
		if year % 400 == 0 and year % 3200 != 0:
			return '閏年'
		elif year % 100 == 0 and year % 400 != 0:
			return '平年'
		elif year % 4 == 0 and year % 100 != 0:
			return '閏年'
		else:
			return '平年'

#加入開關，參數設為True
def on_off(on=True):
	#進入程式
	print(is_leap())
	#進入迴圈		
	while True:	
		on_off = input('如需繼續查詢請輸入 yes/no: ')
		if on_off == 'yes':
			print(is_leap())
		elif on_off == 'no':
			break
			#程式結束
on_off()