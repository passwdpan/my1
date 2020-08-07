nums=[11,7,15,1,5,8]
target=16
class Solution:
    def towSum(self,nums,target):
        hashmap={}#空字典
        for i in range(len(nums)):
            # print(hashmap.get(target-nums[i]))
            if hashmap.get(target-nums[i]) is not None:#判断目标值-数组元素是否在字典内
                return [hashmap.get(target-nums[i]),i]
            hashmap[nums[i]]=i


if __name__ == '__main__':
    S=Solution()
    t=S.towSum(nums,target)
    print(t)