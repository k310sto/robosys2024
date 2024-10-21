#!/usr/bin/python3
import sys as st

data = [line.strip() for line in st.stdin] #改行で次の添え字へいくらしい

try:
    print(int(data[1])+int(data[2]))
except:
    print(float(data[1])+float(data[2]))


def tonum(n):
    for n in data[1:]:
        try:
            x += int(n)
        except:
            x += float(n)


print(x)

try:
    nums = [ int(e) for e in data[1:] ]
except:
    nums = [ float(e) for e in data[1:] ]
print(sum(nums))

minus = 0
plus = 0
zero = 0


for z in data[1:]:
	x = float(z)
	if x < 0.0:
		minus += 1
	elif x > 0.0:
		plus += 1
	else:
		zero += 1
print("負：", minus)
print("正：", plus)
print("零：", zero)
#bunsyo = [moji.strip() for moji in data]
#print(bunsyo + "desu")
