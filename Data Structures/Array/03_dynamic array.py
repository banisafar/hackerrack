
MINOR = raw_input('seq of 2:')
all_input = (map(int,MINOR.strip().split(' ')))


N = all_input[0]
Q= all_input[1]

lastAns = 0
S=[[] for i in range(N)]   # do not mutiple
for trial in range(Q):
    TT = raw_input('seq of 3:')
    sample = (map(int,TT.strip().split(' ')))

        
    if sample[0]==1:
        xx= ((sample[1]^lastAns)%N)
        S[xx].append(sample[2])

    else:

        xx= ((sample[1]^lastAns)%N)
        number = sample[2]% len(S[xx])
        lastAns = int(S[xx][number])
        print lastAns

