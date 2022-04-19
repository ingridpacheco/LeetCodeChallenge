class Solution:
    def calPoints(self, ops: List[str]) -> int:

        sum_numbers = 0
        numbers = []
        for op in ops:
            if op == 'D':
                n = numbers[0] * 2
                numbers.insert(0,n)
                sum_numbers += n
            elif op == 'C':
                n = numbers[0]
                numbers.pop(0)
                sum_numbers -= n
            elif op == '+':
                n = numbers[0] + numbers[1]
                numbers.insert(0,n)
                sum_numbers += n
            else:
                numbers.insert(0,int(op))
                sum_numbers += int(op)
        
        return sum_numbers