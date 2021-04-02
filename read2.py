data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: # %-用來求餘數
			print(len(data))
print('檔案讀取完了,總共有' ,len(data) ,'筆資料')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有' ,len(new), '筆留言長度少於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

good = [d for d in data if 'good' in d]
print(good)

bad = ['bad' in d for d in data]
print(bad)

bad = []
for d in data:
	bad.append('bad' in d)

#文字計數
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc: #word有無出現在字典裡
			wc[word] += 1
		else:	
			wc[word] = 1 #增加新的key進wc字典

for word in wc: #每一個word是一個key
	if wc[word] > 1000000:
		print(word, wc[word]) #wc[word]是value

print(len(wc))
print(wc['Jenny'])

while True:
	word = input('Which word would you want to search for ?')
	if word == 'q':
		break
	if word in wc:
		print(word, 'shows for', wc[word], 'times')
	else:
		print('The word is not exist')

print('Thanks for using the query function.')	

