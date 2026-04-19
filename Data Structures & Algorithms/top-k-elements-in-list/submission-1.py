class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      set_l = list(set(nums))
      ct_set = []
      for i in set_l:
        ct_set.append(nums.count(i))
      ret=[]
      print(set_l,ct_set)
      while k!=0:
        x=max(ct_set)
        apd=set_l[ct_set.index(x)]
        ret.append(apd)
        set_l.remove(apd)
        ct_set.remove(x)
        k-=1
      return ret  
        