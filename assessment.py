#solution for collection of arrays that should return a pair of the given sum in the array


def solve(int):
    a=[10,20,30,40,50,60,90]
    i=0
    l=len(a)-1
    while i<=l:
        
        if(a[i]+a[l]>int):
            l=l-1
        elif(a[i]+a[l]<int):
            i=i+1
        else:
            print(a[i],a[l])
            l=l-1
            i=i+1

solve(100)