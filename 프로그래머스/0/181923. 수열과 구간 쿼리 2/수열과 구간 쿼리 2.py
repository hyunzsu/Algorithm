def solution(arr, queries):
	result = []
	for s, e, k in queries:
		temp_list = []
		for i in arr[s:e + 1]:
			if i > k:
				temp_list.append(i)
		result.append(min(temp_list) if temp_list else -1)
	return result