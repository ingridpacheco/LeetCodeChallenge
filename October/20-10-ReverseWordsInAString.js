/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let invertedString = []
    let word = ''
    for (let i = 0; i < s.length; i++) {
        const letter = s[i]
        if (letter.charCodeAt(0) !== 32) {
            word = word + letter
            
            if (i === s.length - 1) invertedString.splice(0,0,word)
        }
        else {
            if (word !== '') {
                invertedString.splice(0,0,word)
                word = ''
            }
        }
    }
    
    return invertedString.join(' ')
};