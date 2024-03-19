def solution(myString, pat):
	res = 0
	for i, x in enumerate(myString):
		if myString[i:].startswith(pat):
			res += 1
	return res