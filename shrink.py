n=int(input("minutes: "));c=[]
while x:=input("chapter (blank=done): "):c+=[(x,float(input(" marks: ")),int(input(" mins: ")))]
g=0
for a,m,t in sorted(c,key=lambda r:-r[1]/r[2]):
    if t<=n:n-=t;g+=m;print("STUDY",a,m,t)
    else:print("SKIP ",a,"-%g marks"%m)
print("got %g of %g marks, %d min spare"%(g,sum(r[1] for r in c),n))
