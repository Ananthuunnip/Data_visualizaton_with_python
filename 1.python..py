#palindrom
pnum = 121
ppnum == pnum
p = 0
while pnum !=0:
  temp = pnum % 10
  p = p * 10 + temp
  pnum = pnum//10
if p ==pnum:
  print(p)
else:
  print("not")
