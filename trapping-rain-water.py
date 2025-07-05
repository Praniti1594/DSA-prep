# https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        rmax=lmax=total=0
        n=len(height)
        r=n-1
        l=0

        while(l<r):
            if height[r]<=height[l]:
                if rmax > height[r]:
                    total+= rmax- height[r]
                else:
                    rmax= height[r]
                r=r-1
            else:
                if lmax> height[l]:
                    total+= lmax - height[l]
                else:
                    lmax=height[l]
                l=l+1
        return total

        
