function evenCubes(...num){
    result = []
    for (let n of num) {
        if (n % 2 == 0) {result.push(n**3)}
    }
    return result
}
console.log(evenCubes(9,4,5,6,6,7,8,8,9,9))