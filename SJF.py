def ReturnIndex(copy,value):
    for i in range(len(copy)):
        if copy[i][0]>value:
            return i-1
    return len(copy)-1
    
print("\tSJF SCHEDULING ALGO\n")
while True:
    process=int(input("Enter number of processes : "))
    if process<=0:
        continue
    else:
        break
list=[]
copy=[]
for i in range(process):
    print("Enter arrival time of process %d: " % (i+1),end="")
    a_t=int(input())
    print("Enter burst time of process %d: " % (i+1),end="")
    b_t=int(input())
    while True:
        if a_t>=0 and b_t>0:
            list.append([])
            list[i]=[a_t,"P"+str(i+1),b_t]#index [i][0]=a_t  , index [i][1]=Process # , index [i][2]=b_t
            copy.append([])
            copy[i]=list[i]
            break
        else:
            print("Enter positive time")
            print("Enter arrival time of process %d: " % (i+1),end="")
            a_t=int(input())
            print("Enter burst time of process %d: " % (i+1),end="")
            b_t=int(input())
copy.sort() #sorts list according to their arrival time
minimum_b_t=list[0][2]
minimum_a_t=list[0][0]
note=0
for j in range(1,process):
    if copy[j][2]<minimum_b_t and copy[j][0]==minimum_a_t:
        minimum_b_t=copy[j][2]
        note=j
a_t=minimum_a_t
s_t=minimum_a_t
f_t=s_t+minimum_b_t
t_consumed=f_t
w_t=[]
t_a_t=[]
for i in range(process):
    w_t.append([])
    t_a_t.append([])
w_t[0]=[copy[note][1],0]
t_a_t[0]=[copy[note][1],t_consumed-a_t]
avgw_t=0
avgt_a_t=t_a_t[0][1]
copy.pop(note)
for i in range(process-1):
    getIndex=ReturnIndex(copy,t_consumed)   
    minimum_b_t=copy[0][2]
    note=0
    for j in range(getIndex+1):
        if copy[j][2]<minimum_b_t:
            minimum_b_t=copy[j][2]
            note=j
    a_t=copy[note][0]
    s_t=t_consumed
    t_consumed+=minimum_b_t
    w_t[i+1]=[copy[note][1],s_t-a_t]
    avgw_t+=w_t[i+1][1]
    t_a_t[i+1]=[copy[note][1],t_consumed-a_t]
    avgt_a_t+=t_a_t[i+1][1]
    copy.pop(note)
print ("Process \t Arrival Time \t Burst Time")
for i in range(process):
    print ("%s \t\t  %s \t\t  %s" %(list[i][1],list[i][0],list[i][2]))
t_a_t.sort()#sorts according to their names
w_t.sort()#sorts according to their names
print("Process \t Waiting Time \t Turn Around Time")
for i in range(process):
    print("%s \t\t  %s \t\t  %s"%(w_t[i][0],w_t[i][1],t_a_t[i][1]))
print("Avg Waiting Time %.2f" % (avgw_t/process))
print("Avg Turn Around Time %.2f" % (avgt_a_t/process))
del (list,copy,w_t,t_a_t)
