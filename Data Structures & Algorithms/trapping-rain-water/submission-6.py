class Solution:
    def trap(self, height: List[int]) -> int:
        waoo=0
        l,r=0,len(height)-1
        lm,rm=0,0
        while l<r:
            if height[l]<height[r]:
                if height[l]>=lm:
                    lm=height[l]
                else:
                    waoo+=lm-height[l]
                l+=1
            else:
                if height[r]>=rm:
                    rm=height[r]
                else:
                    waoo+=rm-height[r]
                r-=1
        return waoo