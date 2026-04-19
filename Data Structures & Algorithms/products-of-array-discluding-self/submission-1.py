
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(nums)
        re=[]
        x=1
        z=0
        save=nums
        n2=nums
        n3=list(nums)
        if 0 in nums:
            z=1
            print (f"{nums}a")
            if nums.count(0)>1:
                return [0 for _ in range(len(nums))]
            while 0 in n3:
                
                n3.remove(0)


                
                print(f"b{nums}")
        
        print(n2,n3,z)
        
        for n in n3:
            
            x*=n
        
        print(x)
        print(f"nums:{nums}")
        if z !=0:
            
            re=[x for _ in range(len(nums))]
            print(re)
            
            for i,n in enumerate(nums):
                if  n!=0:  
                    re[i]*=0
        else:
            for n in nums:
                re.append(int(x/n))
        return re
    