def maximumdistinctstring(string):
    l=len(string)
    if l==0 or l==1:
        print(l)
    maxchar=count(string)
    minimum=l+1
    a={}
    start=0
    a[string[start]]=1
    for i in range(1,l):
        if string[i] in a:
            a[string[i]]+=1
        else:
            a[string[i]]=1
        if len(a)==maxchar:
            while start<i and a[string[start]]>1:
                a[string[start]]-=1
                start+=1
            if minimum>i+1-start:
                minimum=i+1-start
    print(minimum)
 
    
def count(string):
    s={}
    for i in string:
        if i in s:
            s[i]+=1
        else:
            s[i]=1
    return len(s)
    
string=str(input())
maximumdistinctstring(string)
