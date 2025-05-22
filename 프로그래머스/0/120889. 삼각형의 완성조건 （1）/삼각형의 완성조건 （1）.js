function solution(sides) {
    const sorted_sides = sides.sort((a, b) => a - b)
    return sorted_sides[2] < sorted_sides[0] + sorted_sides[1] ? 1 : 2
}