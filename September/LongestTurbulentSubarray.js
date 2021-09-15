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