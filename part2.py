##spin word len greater than 4
def spin_word(sent):
    word=sent.split(' ')
    print(word)
    for id, valu in enumerate(word):
        if (len(valu)>4):
            word[id]=valu[::-1]
    print(word)
    

spin_word('this is sabina')


##find the missing digits
def miss(*bac):
    a=['0','1','2','3','4','5','6','7','8','9']
    for i in bac:
        for j in str(i):
            if j in a:
                a.remove(j)
    print(''.join(a))
miss(12,23,44)

##return smallest word from given string:
def find_shor(s):
  print(min([len(i) for i in  s.split(' ')]))


find_shor("bitcoin take over the world maybe who knows perhaps")


##counting the letter in given string
def count(s):
    dic={}
    fi=''
    for i in s:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
        
    a=''.join([fi+str(dic[key])+key for key in dic.keys()])
    print(a)


count ('adsflsdajflsad')
##display the charater in number

def dec_count(s):
    s1=''
    dig_num=''.join([i if i.isdigit() else ' ' for i in s]).split()
   
    char_num=''.join([i if not i.isdigit() else ' ' for i in s]).split()
    print(dig_num, char_num)
    for id,val in enumerate(char_num):
        for k in range(int(dig_num[id])):
            s1=s1+val
    print(s1)

dec_count('4a5b12w')


##checking narcissistic 
def narcissistic(a):
    return True if (sum([pow(int(i),len(str(a))) for i in str(a)])==a) else False

print(narcissistic(147))


##filtering integer  in given list
def filter_list(l):
    a=[x for x in l if isinstance(x, int)]
    print(a)

filter_list([1,2,'1','b'])

##isograms
def is_isogram(string):
    return len([string.lower().count(i) for i in string])==len(string)

print(is_isogram('Dermatioglyphics'))

##expanded form
def expanded_form(num):
    a=[int(val)*pow(10,len(str(num))-id-1) for id, val in enumerate(str(num))]
    a=[str(i) for i in a if i!=0]
    print( '+'.join(a))


expanded_form(10021)

##make_readable
def make_readable(seconds):
    sec=seconds%60
    min=(seconds/60)%60
    hr=(seconds/120)
    print('%02d:%02d:%02d'%(hr,min,sec))

make_readable(1201)


##max-sequence sum
def max_sequence(a):
    current=0
    max_seq=0
    for i in a:
        current=max(current+i, i)
        max_seq=max(max_seq,current)
    print(max_seq)

max_sequence([-2,1,-3,4,-1,2,1,-5,4])


##length of duplicate_charater
def duplicate_count(text):
    dic={}
    count=0
    for i in text:
        if i not in dic:
            dic[i]=1
        else:
            count=count+1
    print(count)

duplicate_count('adfadsf')

##dig_power
def dig_power(n,p):
    print(sum([pow(int(valu),p+id)for id,valu in enumerate(str(n))]))

dig_power(23432,3)

##finding missing letter in sequence
def miss_letter(a):
    for i in range(ord(a[0]),ord(a[0])+len(a)+1):
        if chr(i) not in a:
            return chr(i)

print(miss_letter(['a','c','d']))

##cake recipe
def cake_recipe(recipe, available):
    a=[]
    for i in recipe.keys():
        if i in available:
            a.append(int(available[i]/recipe[i]))
        else:
            return 0
    return min(a)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cake_recipe(recipe, available))

##prime number between two given number
def giv_num(num1,num2):
    aa=[]
    for i in range(num1,num2):
        flag=0
        for k in range(2,int(i/2)):
            if i%k==0:
                flag=1
                break
        if (flag==0):
            aa.append(i)
    print(aa)
giv_num(3,43)

##give change
def give_change(amount):
    temp=[]
    for i in (100,50,20,10,5,1):
        if amount>i:
            temp.append(amount//i)
            amount=amount%i
        else:
            temp.append(0)
    print(temp[::-1])
give_change(343)

##heavy odd array:
def is_odd_heavy(arr):
    odd,even=[i for i in arr if i%2!=0],[i for i in arr if i%2==0]
    for x in odd:
        for y in even:
            if (x>y):
                print(x,y)
                continue
            else:
                return False
    return len(odd)>0

print(is_odd_heavy([0,2,-19,4,4]))

##sum of two element is equal to given number:
def arry_sum(a,b):
    for i in range(len(a)):
        for j in range(i,(len(a))):
            if a[i]+a[j]==b:
                return (i,j)

print(arry_sum([11,2,8,10],10))

def diamond(n):
    s=[(' '*(int(n/2)-x)+"*"*(2*x+1)+'\n' ) if (n>2 and n%2!=0) else None for x in range(int(n/2)+1) ]
    return ''.join(s+(s[-2::-1])) if None not in s else None

print(diamond(3))


##sum of number of factor of 3 or 5
def solution(number):
    return sum(list(set([i for i in range(number) if (i%3==0 or i%5==0)])))

print(solution(30))

##fibanocci series
def fibonacci(n):
    if n in [0,1]:
        return n
    x=0
    y=1
    for i in range(n-2):
        x,y=y,x+y
    return (y)
print(fibonacci(5))

##find the vowel indices
def vowel_indices(a):
   return  [id+1 for id, v in enumerate(a) if v.lower() in 'aeiou']
print(vowel_indices('asdfljsadf'))

##find the max difference between word in two array 
def max_dif(a,b):
    return max([abs(len(i)-len(j))for i in a for j in b])
s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(max_dif(s1,s2))

##counting uppercase, lowercase ,digit and symbol
def solve(s):
    a=[0,0,0,0]
    for i in s:
        if i.isupper():
            a[0]=a[0]+1
        elif i.islower():
            a[1]=a[1]+1
        elif i.isdigit():
            a[2]=a[2]+1
        else:
            a[3]=a[3]+1
    return(a)

print(solve("Codewars@codewars123.com"))

## square the  none suare no or square root square number;

def square_or_square_root(arr):
    return [int(i**0.5) if int(i**0.5)**2==i else i*i for i in arr]
print(square_or_square_root([4,7,9]))


#count mimimun no of notes in atm 

def solve(n):
    cou=0
    for i in (500,200,100,50,20,10):
        if n>i:
            cou=cou+n//i
            n=n%i
    return cou
print(solve(400))

def produfibino(a):
    x,y=0,1
    while(x*y<a):
        x,y=y,x+y
        if (x*y==a):
            return x,y,True
    return x,y,False
print(produfibino(15))


#valid your sodukho
def valid_solution(board):
   
    fla=sum([1 for sub in board for i in sub if (len(list(set(sub)))==9 and i>0 and i<10)])==81
    if fla:
        transpose=[[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    else:
        return fla
    fla1=sum([1 for sub in transpose for i in sub if (len(list(set(sub)))==9 and i>=1 and i<=9)])==81
    if  fla1:
        for z in range(0,9,3):
            for i in range (9):
                x=(i*3)%9
            
                tem=[]
                for j in range(x,x+3):
                    for k in range(z,z+3):
                        
                        if board[j][k] in tem:
                            return False
                        tem.append(board[j][k])
                if len(tem)!=9:
                    return False
    return True


print(valid_solution([             [5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]))










