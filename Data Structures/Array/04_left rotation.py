


ll= raw_input('2 numbers first length, second split:')
arr = (map(int,ll.strip().split(' ')))
Y=arr[1]


xs= raw_input('seq: ')
seq = (map(int,xs.strip().split(' ')))
strseq=map(str,seq[Y:]+seq[:Y])   #convert int to string to use join
print ' '.join(strseq)
