
def getHided():
  a=[11,101,1100]
  b=[1001,101,1010]
  c=[2000,1100,11]
  d=[11,200,1010]
  r = range(0,3)
  tot=0
  for i1 in r:
    for i2 in r:
      for i3 in r:
        for i4 in r:
          tot = a[i1]+b[i2]+c[i3]+d[i4]
          if tot==3212:
            print([i1,i2,i3,i4])


def getPossibe():
  out=[]
  tmp=[]
  for i in range(0,4):
    for add in range(0,4):
      tmp.append((i+add)%4)
    out.append(tmp)
    tmp=[]
    for add in range(0,4):
      tmp.append((i-add)%4)
    out.append(tmp)
    tmp=[]
  return out


def final(a,b,c,d):
  r = getPossibe()

  for i2 in r:
      for i3 in r:
        for i4 in r:
          for index in range(0,4):
            total = a[index]+b[i2[index]] +c[i3[index]] + d[i4[index]]
            if total == 1111:
              if(index ==3):
                print([i2,i3,i4])
                print([a[index],b[i2[index]] ,c[i3[index]] , d[i4[index]]])
              continue
            else:
              break

a=[100,100,1,1000]
b=[100,1000,1,10]
c=[100,10,1000,1]
d=[10,1000,1,10]

a2=[1,100,10,1000]
b2=b
c2=[1000,10,1000,1]
d2=[10,100,1,100]

a3=a2
b3=[1,1000,1000,10]
c3=c
d3=d2
#getHided()
final(a3,b3,c3,d3)