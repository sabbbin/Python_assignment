def T():  
    s=''
    for i in range(7):
        for j in range(5):
            if (i==0):
                s=s+'*'
            elif(j==2):
                s=s+'*'
            else:
                s=s+' '
        s=s+'\n'
    return s
def O():
    r=''
    for i in range(7):
        for j in range(5):
            if (i==0 or i==6):
                if (j==0 or j==4):
                    r=r+' '
                else:
                    r=r+'*'
            elif (j==0 or j==4):
                if (i==0 or i==6):
                    r=r+' '
                else:
                    r=r+'*'
            else:
                r=r+' '
        r=r+'\n'
    return r
def L():
    t=''
    for i in range(7):
        for j in range(5):
            if j==0:
                t=t+'*'
            elif i==6:
                t=t+'*'
            else:
                t=t+' '
        t=t+'\n'
    return t

def C():
    r=''
    for i in range(7):
        for j in range(5):
            if (i==0 or i==6):
                if (j==0 or j==4):
                    r=r+' '
                else:
                    r=r+'*'
            elif (j==0):
                if (i==0 or i==6):
                    r=r+' '
                else:
                    r=r+'*'
            elif (j==4):
                if (i==0 or i==6 or i==2 or i==3 or i==4):
                    r=r+' '
                else:
                    r=r+'*'

            else:
                r=r+' '
        r=r+'\n'
    return r
def H():
    u=''
    for i in range(7):
        for j in range(5):
            if (j==0 or j==4):
                u=u+'*'
            elif(i==3):
                u=u+'*'
            else:
                u=u+' '
        u=u+'\n'
    return u

def D():
    d=''
    for i in range(7):
        for j in range(5):
            if j==0:
                d=d+'*'
            elif (i==0 or i==6):
                if j in [1,2]:
                    d=d+'*'
                else :
                    d=d+' '
            elif (i==1 or i==5):
                if (j==3):
                    d=d+'*'
                else:
                    d=d+' '
            elif  (j==4):
                if (i in [2,3,4]):
                    d=d+'*'
                else:
                    d=d+' '
            else:
                d=d+' '
        d=d+'\n'
    return d

#program begin:
valid_input ='COLDHT'
dic={'C':C(),'O':O(),'L':L(), 'D':D(),'H':H(),'T':T()}
inp= input("enter single word :")
temp=[]
for i in inp:
    if i in valid_input:
        temp.append(i)
fina=''
if (len(temp)>0):
    for i in temp:
        fina=fina+dic[i]
        

else:
    print('plese input valid word')
print(fina)