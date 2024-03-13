def solution(num_list):
	res = 0
	for i in num_list:
		while i != 1:
			if i % 2 == 0:
				i //= 2
			else:
				i -= 1
				i //= 2
			res += 1
	return res