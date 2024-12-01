LEN = 1000

list1 = []
list2 = []

# Read list of Values from assets folder

with open('../assets/day1_historian_hysteria.txt') as f:
    for i in range(LEN):
        vals = f.readline().split()
        list1.append(int(vals[0]))
        list2.append(int(vals[1]))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

total_distance = 0

for i in range(LEN):
    total_distance += abs(sorted_list1[i] - sorted_list2[i])

print(total_distance)