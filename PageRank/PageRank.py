import numpy as np

pgno=int(input("Total page"))
#damping factor
d=0.85
count=0
count_link=[]
pg_prob=[]
ct=[]
mat=np.zeros((pgno,pgno))
for i in range (pgno):
	mat[i]=input().split(" ")
for i in range (pgno):
    ct[i]=mat[i].count(1)
print(ct)