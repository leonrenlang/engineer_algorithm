

""" 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。
A 不能视为 14。 """


# 思想：
# 首先排序，如果排序后鬼的数目小于空缺的数目或者存在重复的牌，则False

def isStraight(nums):
    if len(nums) != 5: return False
    nums.sort()
    ghost = 0
    for i in range(len(nums) - 1):
        if nums[i] == 0: 
            ghost += 1
        else:
            if nums[i+1] == nums[i]:
                return False
            ghost -= (nums[i+1] - nums[i] -1)
            if ghost < 0: 
                return False
    return True



