class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)
            else:
                if not stack:
                    return False
                k=stack[-1]
                if k=="(" and i==")":
                    stack.pop()
                elif k=="{" and i=="}":
                    stack.pop()
                elif k=="[" and i=="]":
                    stack.pop()
                else: 
                    return False 

        if not stack:
            return True
        return False
                

        