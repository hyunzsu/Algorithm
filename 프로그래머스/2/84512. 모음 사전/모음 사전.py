def solution(word):
	res = 0
	for i, n in enumerate(word):
		res += (5 ** (5 - i) - 1) / (5 - 1) * 'AEIOU'.index(n) + 1
	return res