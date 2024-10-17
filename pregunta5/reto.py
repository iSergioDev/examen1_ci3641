import sys
import time
from math import floor, log2, comb

def nara(n,k):
    return round((1/n)*comb(n,k)*comb(n,k-1))

def trib_t(n,a=0,b=1,c=2):
    if n==0:
        return a
    elif n==1:
        return b
    elif n==2:
        return c
    else:
        return trib_t(n-1,b,c,a+b+c)

def maldad(n):
    k=floor(log2(n))
    N_n_k=nara(n, k)
    log_v=floor(log2(N_n_k))
    return trib_t(log_v+1)

def main():
    n = int(sys.argv[1])
    st=time.time()
    r=maldad(n)
    et=time.time()
    t=et-st
    print(f"maldad({n}) = {r}")
    print(f"Execution time = {t:.6f}s")

if __name__=="__main__":
    main()