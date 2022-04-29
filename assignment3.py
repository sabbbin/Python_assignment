def inputFun():
    while 1:
        priority=input('Enter your priority: High or Low :  ')
        subject=input('Enter subject of appointment within 30 charaters:  ')
        date1=input('Enter the date of appointment dd/mm/yyyy:  ')
        starttime=input('Enter the Start Time greater than 6:  ')
        endtime=input('Enter the end time less than 23:  ')
        try:
            if isValidDate(date1):
                
                if isValidTime(starttime,endtime):
                    if(len(subject)>1 and len(subject)<31):
                        if priority.lower() in ['low','high']:
                            if (isConcurrentAppointment(date1,starttime)):
                                addRecord(priority,subject,date1,starttime,endtime)
                                showRecord()
                            else:
                                print('already booked')
        except:
            print('given input accourding to instruction ')
        inp=input('Pres any key to add another record else  enter ENd to stop')
        if (inp.lower()=='end'):
            break
   



def isValidDate(date1):
    datecheck=date1.split('/')
    print(datecheck)
    if not (int(datecheck[2])<10000 and int(datecheck[2])>2022):
        
        return False
    if not(int(datecheck[1])<=12 and int(datecheck[1])>=1):
        return False
    if ((int(datecheck[0])>=1 and int(datecheck[0])<=30) and (int(datecheck[1]) in [4,6,9,11] )):
     
        return True
    elif ((int(datecheck[0])>=1 and int(datecheck[0])<=31) and (int(datecheck[1]) in [1,3,5,7,8,10,12] )):
        return True
    elif ( int(datecheck[2])%400 and int(datecheck[2])%4==0 and int(datecheck[2])%100!=0 ):
        if  (datecheck[0]==29) and int(datecheck[1])==2:
            return True
    elif  (int(datecheck[1])==1 and int(datecheck[0])==28):
        return True
    return False

def isValidTime(start, end):
    if not (int(start)<int(end)):
        return False

    if not (int(start)>=7 and int(end)<=22):
        return False
    return True


def showRecord():
    import os.path

    file_exists = os.path.exists('diary.txt')
    if (file_exists):
        print('Priority        Date            start       End     Subject')
        print('---------       -----           -----       ----    --------------------------')
        with open('diary.txt','r') as f:
            for i in f.readlines():
                eachrecord=i.split(' ')
                eachelem=eachrecord[0][:-1].split('\t')
               
                print('{:6s}          {:12s}     {:6s}      {:6s}  {}'.format(eachelem[0],eachelem[1],eachelem[2],eachelem[3],eachelem[4]))
        f.close()
    else:
        print('NO record to show ')
    

def addRecord(priority,subject, date1,starttime,endtime):
    with open ('diary.txt','a') as f:
        l=[priority+'\t',date1+'\t',starttime+'\t',endtime+'\t',subject+'\n']
        f.writelines(l)
    f.close()
    print('succesfult')



def isConcurrentAppointment(date1,starttime):

    import os.path

    file_exists = os.path.exists('diary.txt')
    if (file_exists):
        with open('diary.txt','r') as f:
            for i in f.readlines():
                eachrecord=i.split(' ')
                eachelem=eachrecord[0][:-1].split('\t')
                if eachelem[1]==date1 and starttime==eachelem[2] :
                    return False
            
        f.close()
    return True


def sortRecord():

    import os.path

    file_exists = os.path.exists('diary.txt')
    if (file_exists):
        temp=[]
        with open('diary.txt','r') as f:
            for i in f.readlines():
                eachrecord=i.split(' ')
                eachelem=eachrecord[0][:-1].split('\t')
                temp.append(eachelem)
        f.close()
        while(1):
            sot=input('Do you want to sort the appointments by time or priority ')
            if (sot.lower()=='time'):
                final=sorted(temp, key=lambda x:''.join((x[1].split('/'))[::-1] ))
            elif(sot.lower()=='priority'):
                final=sorted(temp, key=lambda x:x[0])
            print('Priority        Date            start       End     Subject')
            print('---------       -----           -----       ----    --------------------------')
            for i in final:
                print('{:6s}          {:12s}     {:6s}      {:6s}  {}'.format(i[0],i[1],i[2],i[3],i[4]))
            inp=input('Press End to stop or key to continue sorting')
            if (inp.lower()=='end'):
                break

        
        
           
        

      
      


if __name__=='__main__':
    while 1:
        print('------------------------------personal Diary-------------------------------------------')
        print('******************************************************************************************')
        
        choice= input('Press 1 : input appointment record \nPress 2 :input view record in sort order\n press any  to terminate program')
        if choice=='1':
            inputFun()
        elif choice=='2':
            sortRecord()
        else:
            break



    
