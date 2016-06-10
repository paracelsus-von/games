# Enter your code here. Read input from STDIN. Print output to STDOUT

N,D,K = map(int, raw_input().strip().split())

L = []
R = []

for i in range(N):
    lr = map(int, raw_input().strip().split())
    L.append(lr[0])
    R.append(lr[1])

days = []
for day in range(min(L), max(R) + 1):
    days.append(0)


for j in range(K):
    d = int(raw_input())
    counter = 0# Enter your code here. Read input from STDIN. Print output to STDOUT

N,D,K = map(int, raw_input().strip().split())

L = []
R = []

for i in range(N):
    lr = map(int, raw_input().strip().split())
    L.append(lr[0])
    R.append(lr[1])

days = []
for day in range(min(L), max(R) + 1):
    days.append(0)


for j in range(K):
    
    d = int(raw_input())
    counter = 0
    
    for i in range(N):# Enter your code here. Read input from STDIN. Print output to STDOUT

N,D,K = map(int, raw_input().strip().split())

L = []
R = []

for i in range(N):
    lr = map(int, raw_input().strip().split())
    L.append(lr[0])
    R.append(lr[1])

days = []
for day in range(min(L), max(R) + 1):
    days.append(0)


for j in range(K):
    
    d = int(raw_input())
    counter = 0
    
    for i in range(N):
        
        if R[i] + 1 - L[i] >= d:
            if i == 0:
                for k in range(L[0] - 1, R[0]):
                    days[k] = 1
            else:
                 for k in range(L[i] - 1, R[i]):
                        if days[k] == 1:
                            counter = 1
                            break
                        else:
                            continue
                 if counter == 0:
                     for k in range(L[i] - 1, R[i]):
                         days[k] = 1
            counter = 0
    print sum(days)
    for i in range(len(days)):
        days[i] = 0
