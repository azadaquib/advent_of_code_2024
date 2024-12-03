import re

with open('../assets/day_3_mull_it_over.txt', 'r') as f:
    data_str = f.read()
    total = 0
    mull_list = re.findall(r'mul\(\d+,\d+\)', data_str)
    for mul in mull_list:
        nums = list(map(int, re.findall(r'\d+', mul)))
        total += nums[0] * nums[1]

print(total)
