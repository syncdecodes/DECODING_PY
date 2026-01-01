function str_freq(string){
    freq = {}
    for (let ch of string) {
        if (ch in freq) {freq[ch] += 1}
        else {freq[ch] = 1}
    }
    return freq
}

function replace_ch(string, Old, New){
    string = string.replace(Old, New)
    return string
}

function remove_first_ch(string, ch){
    let index = string.indexOf(ch)
    let removed = string.slice(0, index) + string.slice(index+ 1, string.length)
    return removed
}

function remove_all_ch(string, ch){
    removed = string.replaceAll(ch, "")
    return removed
}

function swap_ch(s1, s2, n){
    if (n <= s1.length && n <= s2.length){
        swapped_s1 = s2.slice(0,n) + s1.slice(n)
        swapped_s2 = s1.slice(0, n)+ s2.slice(n)
    }
    else return "n is larger than the length of one of the strings!"
    return [swapped_s1,swapped_s2]
}

console.log(swap_ch("mamta", "nikku", 5))
