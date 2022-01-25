/*
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
    arr[k] > arr[k + 1] when k is odd, and
    arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
    arr[k] > arr[k + 1] when k is even, and
    arr[k] < arr[k + 1] when k is odd.

Ex:
    Input: arr = [9,4,2,10,7,8,8,1,9]
    Output: 5
*/

/**
 * @param {number[]} arr
 * @return {number}
 */

const checkMax = (acc, max) => acc > max ? acc : max

var maxTurbulenceSize = function(arr) {
    
    if (arr.length === 1) return 1
    
    let max = 1
    let acc = 1
    
    let operation = ''
    
    for (let i = 1; i < arr.length; i++){
        const currentValue = arr[i]
        const previousValue = arr[i-1]
        if (currentValue === previousValue) {
            max = checkMax(acc,max)
            acc = 1
        }
        else {
            if (acc === 1) {
                acc += 1
            }
            else {
                const checkValues = currentValue > previousValue
                if (checkValues && operation === '<' || !checkValues && operation === '>') {
                    acc += 1
                }
                else {
                    max = checkMax(acc,max)
                    acc = 2
                }
            }
            operation = arr[i] > arr[i-1] ? '>' : '<'
        } 
    }
    
    max = checkMax(acc,max)
    
    return max
};

// console.log(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))