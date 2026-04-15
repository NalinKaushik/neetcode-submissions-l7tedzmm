class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        p1 = 0
        p2 = n-1

        while(True):
            value = numbers[p1] + numbers[p2]
            if value > target:
                p2-=1
            
            elif value < target:
                p1+=1
            
            else:return[p1+1,p2+1]

            


        

