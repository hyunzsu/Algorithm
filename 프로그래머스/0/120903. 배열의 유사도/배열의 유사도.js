function solution(s1, s2) {
    // 배열을 Set으로 변환하여 교집합 찾기
    const set1 = new Set(s1);
    const set2 = new Set(s2);    
    
    // 교집합 원소 개수 구하기
    let count = 0;
    for (const el of set1) {
        if (set2.has(el)) {
            count++;
        }
    }
    return count;
}