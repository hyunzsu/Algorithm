def solution(new_id):
    answer = new_id.lower()
    filtered = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):
            filtered.append(c)
    answer = ''.join(filtered)
    print(answer)