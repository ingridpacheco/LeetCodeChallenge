// Given a palindromic string of lowercase English letters palindrome,
// replace exactly one character with any lowercase English letter so that the resulting string
// is not a palindrome and that it is the lexicographically smallest one possible.

// Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

// A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ,
// a has a character strictly smaller than the corresponding character in b. For example,
// "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character,
// and 'c' is smaller than 'd'.

// Ex:
// Input: palindrome = "abccba"
// Output: "aaccba"

/**
 * @param {string} palindrome
 * @return {string}
 */
var breakPalindrome = function(palindrome) {
    if (palindrome.length === 1) return ''

    let newPalindrome = palindrome.split('')
    
    const len = Math.ceil(palindrome.length/2)
    const base = 97
    let changed = false
    let index = palindrome.length - 1
    
    for (let i = 0; i < len ; i++) {
        let code1 = palindrome.charCodeAt(i)
        let code2 = palindrome.charCodeAt(palindrome.length - 1 - i)

        if (i !== (palindrome.length - 1 - i)) {
            if (code1 > base){
                code1 = base
                changed = true
                newPalindrome[i] = String.fromCharCode(code1)
                break
            }
            else {
                if (code2 > base){
                    code2 = base
                    changed = true
                    newPalindrome[palindrome.length - 1 - i] = String.fromCharCode(code2)
                    break
                }
            }
        }
        
        if (code2 < palindrome.charCodeAt(index)){
            index = palindrome.length - 1 - i
        }
    }
    
    if (!changed) {
        let code = palindrome.charCodeAt(index)
        code += 1
        newPalindrome[index] = String.fromCharCode(code)
    }
    
    return newPalindrome.join('')
};