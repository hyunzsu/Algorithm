def solution(new_id):
    res = new_id.lower()
    filtered = []
    for c in res:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):
            filtered.append(c)
    res = ''.join(filtered)
    while '..' in res:
        res = res.replace('..', '.')
    res = res.strip('.')
    if res == '':
        res = 'a'
    if len(res) > 15:
        res = res[:15]
    if res[-1] == '.':
        res = res[:-1]
    while len(res) < 3:
        res += res[-1]
    return res
        