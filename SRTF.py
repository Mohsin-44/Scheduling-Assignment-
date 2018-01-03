a_t=[]
b_t=[]
list=[]
complete=[]
w_t=0
t_a_t=0
print("\tSRTF SCHEDULING ALGO\n")
while True:
    process=int(input("Enter number of processes : "))
    if process<=0:
        continue
    else:
        break
for i in range(process):
    print("Enter arrival time of process %d: " % (i+1),end="")
    at=int(input())
    print("Enter burst time of process %d: " % (i+1),end="")
    bt=int(input())
    while True:
        if at>=0 and bt>0:
            a_t.append(at)
            b_t.append(bt)
            list.append(b_t[i])#another list for remaining burst time
            break
        else:
            print("Enter positive time")
            print("Enter arrival time of process %d: " % (i+1),end="")
            at=int(input())
            print("Enter burst time of process %d: " % (i+1),end="")
            bt=int(input())            
list.append(max(b_t)*2000)#STORES A RANDOM SENTINAL VALUE
c_time=min(a_t)
p_exec=0
print ("\nProcess\t Waiting Time\tTurn Around Time")
while p_exec<process:
    minimum=process
    i=0        
    while i<process:
        if list[i]>0 and a_t[i]<=c_time and list[i]<list[minimum]:
            minimum=i
        i+=1       
    list[minimum]-=1
    if list[minimum]==0:
        e_t=c_time+1
        complete.append([])
        complete[p_exec]=["P"+str(minimum+1),e_t-b_t[minimum]-a_t[minimum],e_t-a_t[minimum]]#index [i][0]=Process# , index [i][1]=W_Time ,index [i][2]=Turn_A_T
        p_exec+=1
        w_t+=complete[p_exec-1][1]
        t_a_t+=complete[p_exec-1][2]
    c_time+=1
complete.sort()
for i in range(process):
    print(complete[i][0],"\t\t",complete[i][1],"\t\t",complete[i][2])
print ("\nAverage waiting time = %.2f"%(w_t/process))
print ("Average Turnaround time = %.2f"%(t_a_t/process))
del (a_t,b_t,list,complete)
