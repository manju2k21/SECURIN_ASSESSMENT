c={}
def freq(a,b):
    d={}
    for i in range(1,7):
        for j in range(1,7):
            s=i+j 
            if s in d.keys():
                d[s]=d[s]+1 
            else:
                d[s]=1
                c[s]=0
    return d

def check_prob(d,c):
    for i in d.keys():
        if (d[i]/36) != (c[i]/36):
            return False
    return True
    
def undoom_dice(a,b):
    #sum=2 has only one possibility (1,1)-first element of new_a and new_b
    # as 4 is the most spots on a face -last element of new_a
    #the rest elemets are initalized to 1
    
    new_die_a=[1,1,1,1,1,4]
    new_die_b=[1,1,1,1,1,1]
    d=freq(a,b)
    
    #finding new_die_a
    
    for i in range(1):
        for j in range(6):
            s=new_die_a[j]+new_die_b[i]
            while((c[s]+1)>d[s]):
                new_die_a[j]=new_die_a[j]+1 
                s=new_die_a[j]+new_die_b[i]
            c[s]=c[s]+1
   
    
    #finding new_die_b
    
    for i in range(1,6):
        for j in range(6):
            s=new_die_a[j]+new_die_b[i]
            while((c[s]+1)>d[s]):
                new_die_b[i]=new_die_b[i]+1 
                s=new_die_a[j]+new_die_b[i]
            c[s]=c[s]+1
   
   # checking for equal probability between old and new die
    if(check_prob(d,c)):
        print("NEW_DIE_A = ",new_die_a," NEW_DIE_B = ",new_die_b)
    else:
        print("incorrect die")
    
    
    
    
    
print("DIE_A:")    
A=[int(x) for x in  input().split(" ")]
print("DIE_B:")
B=[int(x) for x in  input().split(" ")]
print("\n\n")
undoom_dice(A,B)
print("\n")