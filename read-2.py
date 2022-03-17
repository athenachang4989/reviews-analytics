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

print('總共有', len(data), '則留言')
print('每則留言的平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '則留言小於100個字母')
print(new[0])
print(new[1])