link = 'https://leetcode.com/problems/summary-ranges/description/'

def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        lower= upper = nums[0]
        ret = []
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                if lower==upper:
                    ret.append(str(lower))
                else:
                    ret.append(f'{lower}->{upper}')
                lower=nums[i]
            upper=nums[i]

        if lower==upper:
            ret.append(str(lower))
        else:
            ret.append(f'{lower}->{upper}')               
        return ret