def solution(arr):
	result = 0
	# prev = arr
	while True:
		new = []
		for i in arr:
			if i >= 50 and i % 2 == 0:
				i = i // 2
			elif i < 50 and i % 2 != 0:
				i = i * 2 + 1
			new.append(i)

		if arr == new:
			break
		else:
			arr = new 
			result += 1
	return result