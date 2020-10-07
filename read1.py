data = []
sum_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)

for line in data:
	sum_len = sum_len + len(line)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有' ,len(new), '筆留言長度少於100')
print(new[0])
print(new[1])