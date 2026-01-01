function indices(mainstr, substr) {
    if (!mainstr.includes(substr)) return -1
    let ind = [];
    let start = 0;
    while (true) {
        let index = mainstr.indexOf(substr, start)
        if (index == -1) break
        ind.push(index)
        start = index + 1
    }
    return ind
}
console.log(indices("ababababab", "ab"))
