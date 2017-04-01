
N,M = map(int,raw_input('gimme N,M :').strip().split(' '))

#listN= [int(0) for i in range(N)]   #not use np
listN= [0]*(N+1)   #not use np


for i in range(M):
    a,b,k =  map(int,raw_input('gimme a,b,k :').strip().split(' '))
    listN[a-1]+= k
    listN[b]-= k

#fastest method
maxx=x=0
for i in listN:
    x=x+i
    if maxx<x:
        maxx=x
print maxx
        

##find_max=[]
##for i in range(N):
##    find_max.append(sum(listN[:(i+1)]))
##print max(find_max)

    

####Complexity was O(nm)
##for i in range(M):
##    a,b,k = map(int,raw_input('gimme a,b,k :').strip().split(' '))
##    for j in range(b-a+1):
##        listN[a+j-1]=listN[a+j-1]+k
##print listN
