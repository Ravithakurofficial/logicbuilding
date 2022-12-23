lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
lst2 = []
for ele in lst:
  str(ele)
  m = len(str(ele))
  if m%2 == 0:
    lst2.append(m)   
a=len(lst2)
print("number of even element digits in lst",a)





