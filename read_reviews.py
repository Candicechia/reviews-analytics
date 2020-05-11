data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #每次讀取一行
		data.append(line)
		
		count += 1 #知道讀取狀態，讓程式每讀10000筆印一次
		if count % 10000 == 0:
			print(len(data))


print('檔案讀取完了, 總共有', len(data), '筆資料')


#計算每筆留言平均長度
total = 0
for rvlong in data:
	total = total + len(rvlong)

average_long = total/len(data)
print('每筆留言平均長度為:', average_long)