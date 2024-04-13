import random

def lista_n(n,l,l1):
    r=[]
    for i in range(len(l1)):
        if(l1[i]==n):
            r.append(l[i])
    return r


s=input()
w=input()
n=int(input())

l=s.split(".")
pw=[]
num=[]
for i in l:
    l1=i.split(" ")
    for j in range(len(l1)):
        if(l1[j]==w):
            for k in range(1,n+1):
                if(j+k<len(l1)):
                    pw.append(l1[j+k])
                    num.append(k)


fw=w
for i in range(1,n):
    fw+=" "+random.choice(lista_n(i,pw,num))

print(fw)