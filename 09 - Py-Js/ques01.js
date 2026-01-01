function quadratic_roots(a, b, c) {
    console.log("eqn", `${a}x^2 + ${b}x + ${c}`)
    let d = b ** 2 - 4 * a * c
    let r1 = (-b + Math.sqrt(d)) / 2 * a
    let r2 = (-b - Math.sqrt(d)) / 2 * a

    if (d < 0) return
    else if (d > 0) {
        console.log(`root1 = ${r1} and root2 = ${r2}`)
    }
    else console.log(`repeated root: ${r1}`)
}

quadratic_roots(1, -5, 6)
quadratic_roots(1, -4, 4)