class Solution(object):
    def getPermutation(self, n, k):
        from math import factorial
        
        number= list(range(1,n+1))
        k-=1
        result=[]

        for i in range(n,0,-1):
            fact=factorial(i-1)
            index= k//fact
            result.append(str(number[index]))
            number.pop(index)
            k%=fact
        return ''.join(result)
  
        https://leetcode.com/problems/permutation-sequence/
