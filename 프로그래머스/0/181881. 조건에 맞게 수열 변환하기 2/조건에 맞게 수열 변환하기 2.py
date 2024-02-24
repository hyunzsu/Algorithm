def solution(arr):
	result = 0
	prev = arr
	while True:
		new = []
		for i in prev:
			if i >= 50 and i % 2 == 0:
				i = i // 2
			elif i < 50 and i % 2 != 0:
				i = i * 2 + 1
			new.append(i)

		if prev == new:
			break
		else:
			prev = new 
			result += 1
	return result