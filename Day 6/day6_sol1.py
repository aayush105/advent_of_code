lines = [l.strip() for l in open("input.txt").readlines()]

times = []
dists = []
l1 = lines[0].split()
l2 = lines[1].split()
for i in l1[1:]:
    times.append(int(i.strip()))
for i in l2[1:]:
    dists.append(int(i.strip()))

total = 1
for i in range(len(times)):
    count = 0
    for j in range(times[i]):
        dist = (j*(times[i]-j))
        if dist > dists[i]:
            count+=1
    total*=count
print(total)