'''
merge_sort(lst a[p~r], p, r):
    if (p < r):
        q = (p+q) // 2
        merge_sort(a[], p, q)
        merge_sort(a[], q+1, r)
        merge(a, p, q, r)
merge(a, p, q, r):
    i = p
    j = q+1
    int t = 0
    list tmp = []
    while (i<=q and j<=r):
        if (a[i]<a[j]):
            tmp[t++] = a[t++]
        else:
            tmp[t++] = a[j++]
    while (i<=q):
        tmp[t++] = a[i++]
    while (j<=r):
        tmp[t++] = a[j++]
    i = p
    t = 0
    while (i <= r):
        a[i++] = t[t++]
        c++
        if (c==k):
            print(-1)
            exit

int n = input()
int k = input()
int a[] = input()
int tmp[]
int c = 0
merge_sort(a[], 0, n-1)
print(-1)
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
tmp = [0]*n
c = [0]
def merge(a, p, q, r, c):
    i = p
    j = q+1
    t=0
    while(i<=q and j<=r):
        if(a[i]<=a[j]):
            tmp[t] = a[i]
            t+=1
            i+=1
        else:
            tmp[t] = a[j]
            t+=1
            j+=1
    while(i<=q):
        tmp[t] = a[i]
        t+=1
        i+=1
    while(j<=r):
        tmp[t] = a[j]
        t+=1
        j+=1
    i = p
    t = 0
    while (i <= r):
        a[i] = tmp[t]
        c[0] +=1
        if (c[0]==k):
            print(a[i])
            exit()
        i +=1
        t+=1
def merge_sort(a, p, r, c):
    if(p<r):
        q = (p+r)//2
        merge_sort(a, p, q, c)
        merge_sort(a, q+1, r, c)
        merge(a, p, q, r, c)
merge_sort(a, 0, n-1, c)
print(-1)