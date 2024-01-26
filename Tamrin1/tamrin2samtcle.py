#by samtcle
def tabe_jaam_ba_amalkard(x,y):
    while True:
        if y==0:
            break
        tmp = x & y
        x = x ^ y
        y = tmp << 1
    return x


n = int(input())
m = int(input())
javabe_jaam_comp = tabe_jaam_ba_amalkard(n,m)



k = int(input())


if javabe_jaam_comp == k :
    print(javabe_jaam_comp)
    print('YES')


elif javabe_jaam_comp!= k :
    print(javabe_jaam_comp)
    print('NO')

