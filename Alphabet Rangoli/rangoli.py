n = int(raw_input())
times = (n<<2) - 3
height = (n*2) - 1
a='zyxwvutsrqponmlkjihgfedcba'
bag = list(a[-n:])
bag = "-".join(bag)
bag += bag[::-1][1:]
f1 = (times-1)>>1
print "-"*f1 + bag[0:1] + "-"*f1
for i in range(2,height,2):
    f = (times-(i*2+1))>>1
    print "-"*f + bag[0:i+1] + bag[-i:] + "-"*f
for i in range(height-3,0,-2):
    f = (times-(i*2+1))>>1
    print "-"*f + bag[0:i+1] + bag[-i:] + "-"*f
print "-"*f1 + bag[0:1] + "-"*f1
