#by samtcle
def tabe_tabdil_binary(n): 
    return "{:032b}".format(int(n))

a = str(input())

b = str(input())

k = int(input())

b = str(tabe_tabdil_binary(int(b)))
a = str(tabe_tabdil_binary(int(a)))

aob64 = str(b)+str(a)
finalans=str()
for i in range(k):
    mehmanx = int(input())

    if aob64[-mehmanx-1]=='1':
        finalans = finalans+'1'
    else:
        finalans = finalans+'0'
tmp=0

while tmp!=(len(finalans)):

    if finalans[tmp]=='1':
        print('yes')
    elif finalans[tmp]=='0':
        print('no')
    tmp+=1