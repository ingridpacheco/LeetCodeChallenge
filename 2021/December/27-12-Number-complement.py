class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        bin_num = list(bin(num)[2:])
        
        for i,v in enumerate(bin_num):
            if v == '1':
                bin_num[i] = '0'
            else:
                bin_num[i] = '1'
                
        bin_num = ''.join(bin_num)
        return int(str(bin_num), 2)
        
    def alternate_find_complement(self, num):

        s = str(bin(num))
        sum_num = 0
        num = 1
        for i in s[::-1]:
            if i == "b":
                return sum_num
            elif i =="0":
                sum_num+=num
            num*=2