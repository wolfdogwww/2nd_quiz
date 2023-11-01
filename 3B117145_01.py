x = int(input('請輸入星星數量：'))
llimt=int(x/2)
rlimt=int(x/2)
for i in range (0,x):
    for a in range (0,x):
        if (a >=llimt)&(a<=rlimt):
            print('*',end="")
        else:
            print(" ",end="")
            
    if i>=int(x/2):
        llimt+=1
        rlimt-=1
    else:
        llimt-=1
        rlimt+=1
    print()