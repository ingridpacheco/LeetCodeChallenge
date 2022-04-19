class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        arr.sort()
        
        missing = {}
        result = 0

        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j] in missing:
                    result += missing[arr[j]]
                
                missing_number = target - arr[i] - arr[j]
                
                if missing_number in missing:
                    missing[missing_number] += 1
                else:
                    missing[missing_number] = 1
            missing = {}
                    
        return result % (pow(10,9) + 7)