#1

def flatten(x):
    flat=[]
    for i in x:
        if type(i)==list:
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat
l = [1,'a',['cat'],2,[[[3]],'dog'],4,5]    
print(flatten(l))


#2

def cevir(m):
 m = [i[::-1] for i in m]
 m = m[::-1]
 return m
l=[[1, 2], [3, 4], [5, 6, 7]]
print(cevir(l))
