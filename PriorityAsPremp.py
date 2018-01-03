rem_b_t=[]
list=[]
complete=[]
w_t=0
t_a_t=0
print("\tPRIORITY AS PREMPTIVE SCHEDULING ALGO\n")
minimum=(99999)
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
    print("Enter priority no of process %d: " % (i+1),end="")
    priority=int(input())
    while True:
        if at>=0 and bt>0 and priority>=0:
            list.append([])
            list[i]=["P"+str(i+1),at,bt,priority]
            rem_b_t.append(list[i][2])
            if list[i][1]<minimum:
                minimum=list[i][1]
            break
        else:
            print("Enter positive time")
            print("Enter arrival time of process %d: " % (i+1),end="")
            at=int(input())
            print("Enter burst time of process %d: " % (i+1),end="")
            bt=int(input())
            print("Enter priority no of process %d: " % (i+1),end="")
            priority=int(input())
rem_b_t.append(99999)
c_time=minimum
p_exec=0
print ("\nProcess\t Waiting Time\tTurn Around Time")
while p_exec<process:
    m_priority=99999
    i=0        
    while i<process:
        if rem_b_t[i]>0 and list[i][1]<=c_time and list[i][3]<m_priority:
            maximum=i
            m_priority=list[i][3]
        i+=1       
    rem_b_t[maximum]-=1
    if rem_b_t[maximum]==0:
        e_t=c_time+1
        complete.append([])
        complete[p_exec]=["P"+str(maximum+1),e_t-list[maximum][2]-list[maximum][1],e_t-list[maximum][1]]#index [i][0]=Process# , index [i][1]=W_Time ,index [i][2]=Turn_A_T
        p_exec+=1
        w_t+=complete[p_exec-1][1]
        t_a_t+=complete[p_exec-1][2]
    c_time+=1
complete.sort()
for i in range(process):
    print(complete[i][0],"\t\t",complete[i][1],"\t\t",complete[i][2])
print ("\nAverage waiting time = %.2f"%(w_t/process))
print ("Average Turnaround time = %.2f"%(t_a_t/process))
del (list,complete,rem_b_t)
