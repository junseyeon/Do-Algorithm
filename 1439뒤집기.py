
a = input()

zero = []
one = []
start = ''
tmp = ''
for i in a:
    i = int(i)
    if start == i:
        tmp += str(i)
    else:
        if start != '':
            if tmp.count('0') > 0:
                zero.append(tmp)
            else:
                one.append(tmp)
        start = i
        tmp = str(i)
if tmp.count('0') > 0:
    zero.append(tmp)
else:
    one.append(tmp)

print(min(len(zero), len(one)))
