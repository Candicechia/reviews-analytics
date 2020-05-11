data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #每次讀取一行
		data.append(line)
		count += 1 #知道讀取狀態，讓程式每讀10000筆印一次
		if count % 10000 == 0:
			print(len(data))


print(len(data))

print(data[0]) #印出讀第一筆reveiw
