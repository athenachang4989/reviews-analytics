data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('總共有', len(data), '則留言')
print('每則留言的平均長度是', sum_len/len(data))