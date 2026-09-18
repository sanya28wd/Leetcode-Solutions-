class Solution(object):
    def myPow(self, x, n):
        #a=pow(x,n)
        #return a
        ans=1
        if n==0:
            return 1
        if x==1:
            return 1
        if x==0:
            return 0
        if x==-1 and n%2==0:
             return 1
        if x==-1 and n%2!=0:
             return -1
        if n<0:
            n=-n
            x=1/x
        while(n>0):
            if n%2==1:
                ans=ans*x
            x=x*x
            n/=2
        return ans
