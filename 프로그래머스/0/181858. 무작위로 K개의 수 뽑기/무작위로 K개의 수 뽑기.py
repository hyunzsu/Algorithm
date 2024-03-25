def solution(arr, k):
	res = []
	for i in arr:
		if i not in res:
			res.append(i)
		if len(res) == k:
			break
	while len(res) < k:
		res.append(-1)
	return res