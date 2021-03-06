/*
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Ex:
    Input: text = "nlaebolko"
    Output: 1
*/

/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    // text = "nlaebolko"
    // text = "loonbalxballpoon"
    // text = "leetcode"
    
    let indexes = {
        'b': 0,
        'a': 0,
        'l': 0,
        'o': 0,
        'n': 0
    }
    
    for (let i = 0; i < text.length; i++) {
        if (indexes[text[i]] !== undefined) indexes[text[i]] += 1
    }
    
    indexes['l'] = Math.floor(indexes['l']/2)
    indexes['o'] = Math.floor(indexes['o']/2)
    
    const arr = Object.values(indexes);
    return Math.min(...arr);
};