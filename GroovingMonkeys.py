

def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


def lcm(a,b):   
    lc=(int(a*b/gcd(a,b)))

    return lc


def turns(mon,n):
    i=0
    final=1
    while(i<n):
        pos=i
        count=0
        while(True):
            if(mon[pos]!=pos+1 and mon[pos]!=0):
                temp=pos
                pos=mon[pos]-1
                mon[temp]=0
                count+=1
            else:
                break
        if(final>count and count!=0):
            final=lcm(final,count)
        elif(count!=0):
            final=lcm(count,final)

        i+=1
    return final


n=int(input())
mon=list(map(int,input().split()))
print(turns(mon,n))
