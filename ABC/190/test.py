import itertools
import functools
import operator

N, M = map(int, input().split())
A, B= [], []
for m in range(M):
    a, b =  map(int, input().split())
    A.append(a)
    B.append(b)
K = int(input())
C, D = [], []
for k in range(K):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

CD = [C,D]
CD = list(zip(*CD))
iteration = []
for k in range(2**(K)):
    iteration.append([int(n) for n in list(str(bin(k))[2:].zfill(K))])

candidate = []
for i in iteration:
    candidate.append([ cd[a] for a, cd in zip(i, CD)]) 

b_list = []
for can in candidate:
    buffer = 0
    for pair in itertools.combinations(can, 2):
        buffer += 0 if pair[0]-pair[1] == 0 else 1
    b_list.append(buffer)
max_valiation = candidate[b_list.index(max(b_list))]

bool_A = []
bool_B = []
for element in max_valiation:
    bool_A.append([1 if a==element else 0 for a in A])
    bool_B.append([1 if a==element else 0 for a in B])
bool_A = list(zip(*bool_A))
bool_B = list(zip(*bool_B))

prod = functools.partial(functools.reduce, operator.mul)
buffer = list(zip(*[[1 if sum(a)>0 else 0 for a in bool_A],[1 if sum(a)>0 else 0 for a in bool_B]]))
print(sum([1 if a[0]+a[1] == 2 else 0 for a in buffer]))