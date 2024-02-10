die_A=[1,2,3,4,5,6]
die_B=[1,2,3,4,5,6]

#1.TOTAL COMBINATION
tot_comb=len(die_A)*len(die_B)

print(f"TOTAL_COMBINATION={tot_comb}\n")


arr={}

#2.possible  combination
print("POSSIBLE_COMBINATION")
for i in range(len(die_A)):
    for j in range(len(die_B)):
        print((die_A[i],die_B[j]),end=" ")
    print("\n")

#2.sum
print("SUM")
for i in range(len(die_A)):
    for j in range(len(die_B)):
        print(die_A[i]+die_B[j],end=" ")
        s=die_A[i]+die_B[j]
        if s in arr.keys():
            arr[s]+=1 
        else:
            arr[s]=1
    print("\n")


#print(arr)

#3.PROBABILITY OF SUM
print("| SUM   || PROBABILITY |")
for i in arr.keys():
    print("| ",i  ,"  || ", round(arr[i]/tot_comb,3)," |")
