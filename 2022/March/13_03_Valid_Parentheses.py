class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # ({}[]){}
        # se for char de fechamento, retira da pilha
        
        chars = []
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                chars.append(c)
            else:
                if len(chars) == 0:
                    return False
                last_char = chars[len(chars) - 1]
                if c ==')' and last_char == '(' or c == '}' and last_char == '{' or c == ']' and last_char == '[':
                    chars.pop()
                else:
                    return False
            
        if len(chars) > 0:
            return False
        
        return True