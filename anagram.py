def all_anagrams(filename):
    d={}
    for line in open(filename):
        word=line.strip().lower()
        L=list(word)
        L.sort()
        str=''.join(L)
        if str not in d:
            d[str]=[word]
        else:
            d[str].append(word)
    return d

def filter(d,n):
    a={}
    for word,anagrams in d.items():
            if(len(word)==n):
                a[word]=anagrams
    return(a)

def anagram_setinorder(d):
    t=[]
    for values in d.values():
        if len(values)>1:
            t.append((len(values),values))
    t.sort()
    #for i in t:
        #print(i)
    return t
    

  

D=all_anagrams("words.txt")
    
#print(D)
A=filter(D,3)
#print(A)
    
t=anagram_setinorder(D)
print(t)
