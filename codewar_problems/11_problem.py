def digitize(n: int):
    
    n=str(n)
    l=[]
    for i in n:
        l.append(i)
    number= list(map(int,l))
    number.reverse()
    
    return number