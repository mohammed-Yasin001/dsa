nums = [1,1,1,2,2,2,2,33,33,4,4,5]

freq_map = {}
for i in range(len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(freq_map)