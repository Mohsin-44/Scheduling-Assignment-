def GetIndex(arr,time):
    for i in range(len(arr)):
        if arr[i][0]<=time:
            continue
        else:
            return i
    return len(arr)
list=[]
b_t=[]
print("\tRound Robin SCHEDULING ALGO\n")
while True:
    process=int(input("Enter number of processes : "))
    qt=int(input("Enter quantum time of each process : "))
    if process<=0 and wait<=0 and q_t<=0:
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
            list.append([])
            b_t.append([])
            list[i]=[at,"P"+str(i+1),bt]
            b_t[i]=[bt,"P"+str(i+1)]
            break
        else:
            print("Enter positive time")
            print("Enter arrival time of process %d: " % (i+1),end="")
            at=int(input())
            print("Enter burst time of process %d: " % (i+1),end="")
            bt=int(input())
list.sort()
cur_time=0
w_t=0
t_a_t=0
index=0
i=0
print ("\nProcess\t Waiting Time\tTurn Around Time")
while i<len(list):
   time=0
   if(list[i][0]<=cur_time):
       while time!=qt or list[i][2]!=0:
           time+=1
           list[i][2]-=1
           cur_time+=1
           if list[i][2]==0:
               for j in range(len(b_t)):
                   if b_t[j][1]==list[i][1]:
                       print("%s\t\t%d\t\t%d"%(list[i][1],cur_time-list[i][0]-b_t[j][0],cur_time-list[i][0]))
                       w_t+=cur_time-list[i][0]-b_t[j][0]
                       t_a_t+=cur_time-list[i][0]
                       break
           if time==3 and list[i][2]!=0:
               index=GetIndex(list,cur_time)
               list.append([])
               list.insert(index,[list[i][0],list[i][1],list[i][2]])
       i+=1
   else:
        cur_time+=1
print ("\nAverage waiting time = %.2f"%(w_t/process))
print ("Average Turnaround time = %.2f"%(t_a_t/process))
