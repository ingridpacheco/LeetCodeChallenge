// Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

// Return the maximum possible length of s.

// Ex:

//   Input: arr = ["un","iq","ue"]
//   Output: 4

/**
 * @param {string[]} arr
 * @return {number}
 */
var maxLength = function(arr) {
    
    if (arr.length === 1)
        return arr[0].length
    
    let res = 0;

    const dp = (idx, cur) => {
        res = Math.max(res, cur.length);
        for (let i = idx; i < arr.length; i++) {
            ((cur+arr[i]).length === new Set([...cur,...arr[i]]).size) && 
            dp(i + 1, cur + arr[i]);
        }
    }

    dp(0, '');
    return res;
};