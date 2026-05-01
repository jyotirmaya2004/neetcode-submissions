class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[None]*2*n
        k=0
        
        for i in nums:
            ans[k]=i
            ans[k+n]=i
            k+=1
        return ans
        