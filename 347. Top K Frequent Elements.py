class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        s = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        ans = []
        
        for i in range(k):
            ans.append(s[i][0])

        return ans
        