j = 100
plays = 0
p1 = range(j-99, j-3)
p2 = range(j-98, j-2)
p3 = range(j-97, j-1)
p4 = range(j-96, j)
for nums in p1, p2, p3, p4:
    for i in nums:
        print(i)
        