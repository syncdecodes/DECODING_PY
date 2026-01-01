function pyramid(rows) {
    
    console.log("Pyramid:")
    for (let i = 1; i <= rows; i++) {
        console.log(" ".repeat(rows - i) + "*".repeat(2 * i - 1))
    }

    console.log("\nReverse pyramid:")
    for (let i = rows; i >= 1; i--) {
        console.log(" ".repeat(rows - i) + "*".repeat(2 * i - 1))
    }
}
pyramid(5)