function solution(money) {
    const x = Math.floor(money / 5500)
    const y = money - (x * 5500)
    return [x, y]
}