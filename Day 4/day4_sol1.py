lines = [l.strip() for l in open("input.txt").readlines()]
sum=0
for line in lines:
    l = line.split(':')[1]
    # print(l)
    ll = l.split('|')
    # print(ll)
    cn = {int(i) for i in ll[0].split()}
    # print(cn)
    yn = [int(i) for i in ll[1].split()]
    # print(yn)
    tmp=1
    for num in yn:
        if num in cn:
            tmp*=2
    sum+=(tmp//2)
print(sum)