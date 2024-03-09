def compmax(a,b):
    if a>b:
        return a
    else:
        return b

def compmin(a,b):
    if a>b:
        return b
    else:
        return a

def convolve(comp_seq,comp_filter):
    len_seq=len(comp_seq)
    len_filter=len(comp_filter)
    N=compmax(len_seq,len_filter)
    N2=len_seq+len_filter-1
    comp_output=[]
    sum1=0
    for n in range(N2):
        for k in range(N2):
            if k<len_filter and 0<=n-k<len_seq:
                sum1+=comp_seq[n-k]*comp_filter[k]
        comp_output.append(sum1)
        sum1=0
    return comp_output

print(convolve([1,2+4j,4,7,9],[3+1j,5]))
                
        
