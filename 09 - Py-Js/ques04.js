function analyze_ch(ch) {
    ch = String(ch)
    if (ch.length != 1) return "Invalid"

    let ltr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let num = "1234567890"

    if (ltr.includes(ch)) return "letter"
    else if (num.includes(ch)) return "number"
    else return "special"
}

function char_case(char) {
    char = String(char)
    if (char.length != 1) return "invalid"
    if (analyze_ch(char) == "letter") {
        if (isupper(char)) return "Upper"
        else return "Lower"
    }
    else return `char is not a letter`
}

function isupper(char) {
    return char == char.toUpperCase()
}

function num_name(n) {
    n = String(n)
    if (n.length != 1) return "invalid"
    if (!"0123456789".includes(n)) return "char is not a number";

    let numbers = {
        '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR',
        '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'
    }
    return numbers[n]
}

function character_operation(character) {
    console.log(analyze_ch(character))
    console.log(char_case(character))
    console.log(num_name(character))
}
character_operation("4")