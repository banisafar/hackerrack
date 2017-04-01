N= raw_input('gimme N: ')

string=[]
for i in range(int(N)):
    string.append(raw_input('N lines: '))
print string


Q= raw_input('gimme Q: ')
query=[]
for i in range(int(Q)):
    query.append(raw_input('Q lines: '))
print query

for word in query:
    print string.count(word)
