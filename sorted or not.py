#sorted or not
n=int(input())
data=list(map(int,input().split()))
s=data.copy()
k=data.copy()
s.sort()
k.sort()
k.reverse()
if s==data or k==data:
    print("sorted")
else:
    print("not sorted")
