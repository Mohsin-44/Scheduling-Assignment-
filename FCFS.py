f_t=0
s_t=0
w_t=0
t_a_t=0
list=[]
complete=[]
print("\tFCFS SCHEDULING ALGO\n")
while True:
    process=int(input("Enter number of processes : "))
    if process<=0:
        continue
    else:
        break
for i in range(process):
    print("Enter arrival time of process %d: " % (i+1),end="")
    a_t=int(input())
    print("Enter burst time of process %d: " % (i+1),end="")
    b_t=int(input())
    while True:
        if a_t>=0 and b_t>0:
            list.append([])
            list[i]=[a_t,"P"+str(i+1),b_t]#index [i][0]=a_t  , index [i][1]=Process # , index [i][2]=b_t
            break
        else:
            print("Enter positive time")
            print("Enter arrival time of process %d: " % (i+1),end="")
            a_t=int(input())
            print("Enter burst time of process %d: " % (i+1),end="")
            b_t=int(input())
list.sort() #sorts list according to their arrival time
t_consumed=list[0][0]
print("Process \tWaiting Time\tTurn Around Time")
for i in range(process):
    s_t=t_consumed
    f_t=list[i][2]+s_t
    t_consumed=f_t
    complete.append([])
    complete[i]=[list[i][1],s_t-list[i][0],f_t-list[i][0]]#index [i][0]=Process #  , index [i][1]=Waiting time , index [i][2]=Turn Around time 
    w_t+=complete[i][1]
    t_a_t+=complete[i][2]
complete.sort()
for i in range(process):
    print("%s\t \t  %d \t\t  %d"%(complete[i][0],complete[i][1],complete[i][2]))
print("Average Waiting Time = %.2f\nAverage Turn Around Time = %.2f"%(w_t/process,t_a_t/process))
del (list,complete)
