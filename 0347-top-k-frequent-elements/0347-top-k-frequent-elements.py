class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = {}
        freq_list = [ [] for i in range(len(nums)+1) ]
        
        # print(freq_list)
        for n in nums:
            count_dict[n] = 1 + count_dict.get(n,0)
        print(count_dict)
        for key,val in count_dict.items():
            freq_list[val].append(key)
        print(freq_list)
        res = []
        res_ele = 0
        for count_val in range(len(freq_list)-1,0,-1):
            for num in freq_list[count_val]:
                res.append(num)
                if len(res) == k:
                    return res

