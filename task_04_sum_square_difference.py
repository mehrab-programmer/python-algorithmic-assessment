sn = 0
ss = 0

for n in range(1,101):
    sn += n
    ss += n**2
s_sum = sn ** 2
d = s_sum - ss
print(d)
