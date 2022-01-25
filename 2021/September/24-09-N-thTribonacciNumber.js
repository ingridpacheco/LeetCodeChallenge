// The Tribonacci sequence Tn is defined as follows: 

// T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

// Given n, return the value of Tn.

// Ex:
//  Input: n = 4
//  Output: 4 

/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    
    let memoization = {}
    
    const dp = (num) => {
        if (memoization[num] !== undefined) return memoization[num]
        if (num === 0) return 0
        if ((num === 1) || (num === 2)) return 1
        const res = dp(num - 1) + dp(num - 2) + dp(num - 3)
        memoization[num] = res
        return res
    }
    
    return dp(n)
};