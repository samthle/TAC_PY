#by samtcle
def numtobinfunc(n):
  return "{:064b}".format(int(n))

a = int(input())
b = int(input())


anbdif= a ^ b

binfinaldif = numtobinfunc(anbdif)

finalans=0

for i in range(len(binfinaldif)):

  if str(binfinaldif[i])=="1":
    finalans+=1


print(finalans)