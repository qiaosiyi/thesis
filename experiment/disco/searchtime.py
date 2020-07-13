import math
l = 1000
duishu = 1.819 + 0.006*l

a = math.log(duishu,1.006)

# print a

b = math.log(3072-a,2)


# print b


a = math.log(6,1.006)
# print a
c = 2900
zhishu = 6+math.pow(1.006,c)
b = math.log(zhishu,1.006)
cishu = int(math.log(3072 - b,2))
# print cishu

for c in range(3072):
  zhishu = 6+math.pow(1.006,c)
  b = math.log(zhishu,1.006)
  cishu = int(math.log(3072 - b,2))
  # print c,"\t",cishu 

print math.log(2829359,2)