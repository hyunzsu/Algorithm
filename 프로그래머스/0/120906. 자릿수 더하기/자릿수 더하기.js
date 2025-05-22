function solution(n) {
    let answer = 0;
    const string_array = [...String(n)]
    for(let i = 0;i<string_array.length;i++) {
        answer += Number(string_array[i])
    }
    return answer
}