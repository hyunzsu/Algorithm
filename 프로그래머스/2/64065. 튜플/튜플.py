def solution(s):
	data = s[2:-2].split('},{')
	data = sorted(data, key=lambda x: len(x))
	res = []
	for item in data:
		item = list(map(int, item.split(',')))
		for value in item:
			if value not in res:
				res.append(value)
	return res