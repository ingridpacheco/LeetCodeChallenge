class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        if (len(s) == 0 or len(s) == 1):
            return s
        
        count = 0
        
        my_string = list(s)
        shifts.reverse()

        for idx, val in enumerate(shifts):
            count = count + val
            new_count = count
            if (count > 26):
                new_count = count % 26
            pos = len(shifts) - 1 - idx
            number_value = ord(my_string[pos]) + new_count
            while (number_value > 122):
                number_value = (number_value % 122) + 96
            my_string[pos] = chr(number_value)
            
        return ''.join(my_string)