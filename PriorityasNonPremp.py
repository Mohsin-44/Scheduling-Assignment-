list=[]
w_t=0
t_a_t=0
print("\tPRIORITY AS NON-PREMPTIVE SCHEDULING ALGO\n")
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
            list[i]=[at,"P"+str(i+1),bt,priority]
            break
        else:
            print("Enter positive time")
            print("Enter arrival time of process %d: " % (i+1),end="")
            at=int(input())
            print("Enter burst time of process %d: " % (i+1),end="")
            bt=int(input())
            print("Enter priority no of process %d: " % (i+1),end="")
            priority=int(input())
list.sort()
print ("\nProcess\t Waiting Time\tTurn Around Time")
t_consumed=list[0][0]
for i in range(process):
    for j in range(i+1,process):
        if list[i][0]==list[j][0] and list[j][3]<list[i][3]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
    a_t=list[i][0]
    s_t=t_consumed
    t_consumed+=list[i][2]
    f_t=t_consumed
    w_t+=(s_t-a_t)
    t_a_t+=(f_t-a_t)
    print(list[i][1]+"\t   %d\t\t\t%d"%(s_t-a_t,f_t-a_t))
print ("\nAverage waiting time = %.2f"%(w_t/process))
print ("Average Turnaround time = %.2f"%(t_a_t/process))
del (list)
