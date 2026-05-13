

def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        rest = target - nums[i]
        if rest in hashmap:
            return [hashmap[rest], i]
        hashmap[nums[i]] = i
    return False






nums = [2,7,11,15]
target = 9


