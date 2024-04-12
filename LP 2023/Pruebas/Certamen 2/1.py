n=int(input())
l=[]
for i in range (n):
    email=input()
    tld=email.split(".")
    l.append(tld[len(tld)-1])

tld=max(l,key=l.count)
a=l.count(tld)

print(tld,"-",a)